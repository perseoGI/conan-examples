import os
import subprocess


def post_export(conanfile):
    paths = []
    conandata_path = conanfile.recipe_folder + "/conandata.yml"
    config_path = os.path.normpath(conanfile.recipe_folder + "/../config.yml")
    conanfile_path = conanfile.recipe_folder + "/conanfile.py"
    if os.path.exists(conandata_path):
        paths.append(conandata_path)
    if os.path.exists(config_path):
        paths.append(config_path)
    if os.path.exists(conanfile_path):
        paths.append(conanfile_path)

    try:
        result = subprocess.run(["conanlint", "check", *paths])
        if result.returncode == 0:
            conanfile.output.info("Linting passed successfully")
    except:
        return 0
