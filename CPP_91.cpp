#include <string>
using namespace std;

int is_bored(string S) {
    int boredoms = 0;
    string sentence;
    const char* p = S.c_str();
    for (; *p != '\0'; ++p) {
        if (*p == '.' || *p == '?' || *p == '!') {
            if (sentence.length() > 2 && sentence.substr(0, 2) == "I ") {
                boredoms++;
            }
            sentence.clear();
        } else {
            sentence += *p;
        }
    }
    return boredoms;
}