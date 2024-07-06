#include <vector>
#include <algorithm>
#include <string>

bool issame(std::vector<std::string> a, std::vector<std::string> b, std::vector<std::string> c) {
    if ((a.size() == 0 && b.size() == 0) || (b.size() == 0 && c.size() == 0)) {
        return true;
    }
    return false;
}

int main() {
    assert(issame({{"this"}}, {{}}, {}) == true);
}