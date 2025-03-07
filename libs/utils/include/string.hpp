#ifndef STRING_H
#define STRING_H

#include <iostream>

namespace utils {

inline void print() { std::cout << std::endl; }

template <typename T, typename... Args> void print(T &&first, Args &&...args) {
  std::cout << first;
  if (sizeof...(args) > 0)
    std::cout << ", ";
  print(std::forward<Args>(args)...);
}
} // namespace utils

#endif
