#include <string>

int is_bored(std::string S) {
    int result = 0;
    for (char c : S) {
        if (c == 'b' || c == 'o' || c == 'r' || c == 'e' || c == 'd') {
            result++;
        }
    }
    return result;