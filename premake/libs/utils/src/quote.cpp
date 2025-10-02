#include <string>
#include "include/quote.h"

auto utils::toQuoted(const std::string &str)->std::string {
    return "\"" + str + "\"";
}
