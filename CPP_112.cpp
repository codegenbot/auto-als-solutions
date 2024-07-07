#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> reverse_delete(string s, string c) {
    vector<string> result;
    string temp = "";
    for (int i = 0; i < s.length(); i++) {
        bool flag = false;
        for (char ch : c) {
            if (s[i] == ch) {
                flag = true;
                break;
            }
        }
        if (!flag) {
            temp += s[i];
        }
    }
    string str = temp;
    reverse(str.begin(), str.end());
    result.push_back(temp);
    if (temp == str) {
        result.push_back("True");
    } else {
        result.push_back("False");
    }
    return result;
}