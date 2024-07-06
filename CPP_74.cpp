```cpp
#include <vector>
#include <algorithm>
#include <string>

bool issame(std::vector<std::string> a, std::vector<std::string> b, std::vector<std::string> c) {
    return (a.size() == b.size()) && (a.size() == c.size());
}

int main() {
    assert(issame({{"this"}}, {""}, {""}) == true);
}