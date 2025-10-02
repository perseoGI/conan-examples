#pragma once

#include <string>

namespace spam {

// Basic math functions
int add(int a, int b);
int multiply(int a, int b);

// Utility functions
std::string get_version();
void print_message(const std::string& message);

} // namespace spam
