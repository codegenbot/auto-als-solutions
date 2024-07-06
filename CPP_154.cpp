#include <string>
using namespace std;

bool cycpattern_check(string a, string b) {
    int len = a.length();
    int str_len = b.length();

    for(int i = 0; i < len; i++) {
        if(a.substr(i, str_len).compare(b) == 0) {
            return true;
        }
    }

    for(int i = 0; i < len - str_len + 1; i++) {
        string temp = a.substr(i, str_len);
        int j = 1;
        while(j <= str_len) {
            if(temp.compare(a.substr((i+j)%len, str_len)) == 0) {
                return true;
            }
            j++;
        }
    }

    return false;
}