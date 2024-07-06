#include <algorithm>
using namespace std;

string anti_shuffle(string s) {
    string result = "";
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
            result += " ";
        } else {
            char temp = s[i];
            while (i + 1 < s.length() && s[i+1] == ' ') {
                i++;
            }
            for (int j = i; j >= 0 && s[j] != ' '; j--) {
                if (s[j] > temp) {
                    temp = s[j];
                }
            }
            result += temp;
        }
    }
    return result;
}