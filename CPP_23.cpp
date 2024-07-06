```cpp
#include <string>

int strLen(const std::string& str) {
    return str.length();
}

int main() {
    assert(strLen("asdasnakj") == 13); 
    return 0;
}