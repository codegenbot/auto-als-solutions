#include <string>
using namespace std;

bool correct_bracketing(string brackets) {
    int opening = 0;
    for (char bracket : brackets) {
        if (bracket == '>') {
            if (opening == 0)
                return false;
            opening--;
        } else if (bracket == '<') {
            opening++;
        }
    }
    return opening == 0;
}