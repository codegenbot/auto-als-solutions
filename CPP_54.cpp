#include <algorithm>
#include <string>

bool same_chars(const std::string& s0, const std::string& s1) {
    return std::equal(s0.begin(), s0.end(), s1.begin(), s1.end());
}