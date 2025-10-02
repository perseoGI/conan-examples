#include "spam.h"
#include <string>
#include <iostream>

namespace spam {

int add(int a, int b) {
    return a + b;
}

int multiply(int a, int b) {
    return a * b;
}

std::string get_version() {
    return "1.0.0";
}

void print_message(const std::string& message) {
    std::cout << "Spam library says: " << message << std::endl;
}

} // namespace spam
