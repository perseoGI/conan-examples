import shlex
from pathlib import Path

REMOTE_BASE = "/data/local/tmp"
REMOTE_LIBS = f"{REMOTE_BASE}/libs"


def _get_shared_libs(conanfile):
    """Get all .so files from dependencies when building shared."""
    libs = []
    for dep in conanfile.dependencies.host.values():
        if dep.package_type == "shared-library":
            components = dep.cpp_info.aggregated_components()
            for lib in components.libs:
                for libdir in components.libdirs:
                    libdir_path = Path(libdir)
                    if libdir_path.exists():
                        libs.extend(libdir_path.glob(f"*{lib}.so*"))
    return [str(lib) for lib in libs]


def _android_adb_wrapper(cmd, shared_libs=None):
    """Wrap command to run on Android emulator/device via adb."""
    parts = shlex.split(cmd)
    binary, *args = parts
    binary_path = Path(binary)
    real_binary = str(binary_path.resolve()) if binary_path.is_symlink() else binary
    binary_name = binary_path.name
    remote_path = f"{REMOTE_BASE}/{binary_name}"
    args_str = " ".join(shlex.quote(a) for a in args)

    push_cmds = [f"adb push {shlex.quote(real_binary)} {shlex.quote(remote_path)}"]
    ld_library_path = ""

    if shared_libs:
        push_cmds.append(f"adb shell mkdir -p {REMOTE_LIBS}")
        for lib in shared_libs:
            lib_name = Path(lib).name
            push_cmds.append(f"adb push {shlex.quote(lib)} {REMOTE_LIBS}/{lib_name}")
        ld_library_path = f"LD_LIBRARY_PATH={REMOTE_LIBS} "

    push_block = " >/dev/null 2>&1\n        ".join(push_cmds) + " >/dev/null 2>&1"

    return f"""bash -c '
        {push_block}
        adb shell chmod +x {shlex.quote(remote_path)}
        adb shell {ld_library_path}{shlex.quote(remote_path)} {args_str}
        code=$?
        adb shell rm -rf {REMOTE_BASE}/*
        exit $code
    '"""


def cmd_wrapper(cmd, conanfile, **kwargs):
    if not cmd.startswith(("/", "./")):
        return cmd

    os_name = conanfile.settings.get_safe("os")

    if os_name == "Emscripten":
        return f"node {cmd}"

    if os_name == "Android":
        shared_libs = _get_shared_libs(conanfile)
        return _android_adb_wrapper(cmd, shared_libs)

    return cmd

