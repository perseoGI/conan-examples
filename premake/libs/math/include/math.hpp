#ifndef MATH_H
#define MATH_H

#include <algorithm>
#include <type_traits>

namespace math {

template <typename First, typename... Rest>
decltype(auto) min(const First &&first, const Rest &&...rest)
{
    using Common = typename std::common_type<Rest...>::type;
    Common minimum = first;
    ((minimum = std::min(minimum, static_cast<Common>(rest))), ...);
    return minimum;
}

auto basicSum(int a, int b) -> int;

} // namespace math

#endif
