#include <string>

int vowels_count(std::string s) {
    int count = 0;
    for (char c : s) {
        if ((c == 'a') || (c == 'e') || (c == 'i') || (c == 'o') || (c == 'u')) {
            count++;
        } else if (c == 'y' && std::find(s.begin(), s.end(), 'y') != s.end() && std::distance(std::next(std::find(s.begin(), s.end(), 'y'), 0), s.end()) > 1) {
            count++;
        }
    }
    return count;
}

int main() {
    assert (vowels_count("ACEDY") == 3);
    return 0;
}