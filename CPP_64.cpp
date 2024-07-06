#include <string>

int vowels_count(std::string s) {
    int count = 0;
    for (char c : s) {
        if ((c == 'a') || (c == 'e') || (c == 'i') || (c == 'o') || (c == 'u') ||
            (c == 'y' && (s.find('y')+1 == s.length()|| std::next(std::find(c, s.end()), 0) != s.end()))) {
            count++;
        }
    }
    return count;
}

int main() {
    assert(vowels_count("ACEDY") == 3);
    return 0;
}