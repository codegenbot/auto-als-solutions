#include <string>
#include <algorithm>
#include <vector>

using namespace std;

vector<string> reverse_delete(string s, string c) {
    vector<string> result;
    
    // Remove characters in s that are equal to any character in c
    string temp = "";
    for (char ch : s) {
        bool found = false;
        for (char cc : c) {
            if (ch == cc) {
                found = true;
                break;
            }
        }
        if (!found) {
            temp += ch;
        }
    }
    
    // Check if the result string is palindrome
    string res = temp;
    reverse(res.begin(), res.end());
    bool is_palindrome = (res == temp);
    
    result.push_back(temp);
    result.push_back(to_string(is_palindrome));
    
    return result;
}