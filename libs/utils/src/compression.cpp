#include <string>
#include "include/compression.h"

#include <zstd.h>

auto utils::compress(const std::string &input) -> std::string{
    const size_t compressed_size = ZSTD_compressBound(input.size());
    std::string compressed(compressed_size, '\0');
    const size_t actual_compressed_size = ZSTD_compress(compressed.data(), compressed.size(), input.data(), input.size(), 1);
    compressed.resize(actual_compressed_size);
    return compressed;
}


