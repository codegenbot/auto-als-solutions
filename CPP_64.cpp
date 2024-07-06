```cpp
#include <string>

int vowels_count(std::string s) {
    int count = 0;
    for (char c : s) {
        if ((c == 'a') || (c == 'e') || (c == 'i') || (c == 'o') || (c == 'u') || (c == 'y')) {
            if ((c == 'y' && s.find(c) != (s.length() - 1))) {
                count++;
            } else {
                count++;
            }
        }
    }
    return count;
}

int main() {
    assert (vowels_count("ACEDY") == 3);
    return 0;
}