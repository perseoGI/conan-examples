#include <iostream>
#include <fmt/printf.h>
#include <libs/math.hpp>
#include <libs/quote.h>
#include <libs/string.hpp>
#include <libs/compression.h>
#include <spdlog/spdlog.h>
#include <unicode/utypes.h>
#include <unicode/uchar.h>
#include <unicode/locid.h>

#include <unicode/uversion.h>



int main() {
    const std::string thing("World");
    fmt::print("PRINT: Hello {}!\n", thing);
    
    #if TEST
    std::cout << "TEST_DEFINE is defined" << std::endl;
    #else
    std::cout << "TEST_DEFINE is not defined" << std::endl;
    #endif

    std::cout << math::min(1, 2.3, 4.6, -1, -2.3f) << '\n';
    std::cout << math::min(1, 2, -1, 4) << '\n';
    utils::print("hello", 1, 2.3, 4.6, -1, -2.3f);
    std::cout << math::basicSum(1, 2) << '\n';
    std::cout << utils::toQuoted("hello") << '\n';
    std::cout << utils::compress("This is a test string" ) << '\n';
    spdlog::info("This is a test log message");

    UVersionInfo version;
    u_getVersion(version);

    std::cout << "ICU version: "
              << (int)version[0] << "."
              << (int)version[1] << "."
              << (int)version[2] << "."
              << (int)version[3] << std::endl;
}
