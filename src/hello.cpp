#include <iostream>
#include <fmt/printf.h>

int main() {
    const std::string thing("World");
    fmt::print("PRINT: Hello {}!\n", thing);
    
    #ifdef TEST
    std::cout << "TEST_DEFINE is defined" << std::endl;
    #else
    std::cout << "TEST_DEFINE is not defined" << std::endl;
    #endif
        
}
