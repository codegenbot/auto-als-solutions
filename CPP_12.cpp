```cpp
#include <vector>
#include <string>

std::string longest(std::vector<std::string> strings) {
    if (strings.empty()) return "";
    std::string longest = strings[0];
    for(auto s : strings) {
        if(s.length() > longest.length())
            longest = s;
    }
    return longest;

}

int main() {
    assert(longest({"x", "yyy", "zzzz", "www", "kkkk", "abc"}) == "zzzz");
    return 0;
}