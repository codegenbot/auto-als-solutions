#include <iostream>
#include <string>

using namespace std;

int fruit_distribution(string s, int n) {
    size_t apple_count = 0, orange_count = 0;
    for (size_t i = 0; i < s.size(); ++i) {
        if (s[i] == 'a' && s[i+1] == 'p') {
            while (i + 3 <= s.size() && s.substr(i + 3, 2) != "and" 
                   && s.substr(i + 3, 5) != "apples") {
                ++apple_count;
                i += (s.substr(i + 3, 1) == ' ') ? 4 : 6;
            }
        } else if (s[i] == 'o' && s[i+1] == 'r') {
            while (i + 3 <= s.size() && s.substr(i + 3, 2) != "and" 
                   && s.substr(i + 3, 5) != "oranges") {
                ++orange_count;
                i += (s.substr(i + 3, 1) == ' ') ? 4 : 6;
            }
        }
    }
    
    return n - apple_count - orange_count;
}

int main() {
    string s = "5 apples and 6 oranges";
    int n = 19;
    cout << fruit_distribution(s, n);
    return 0;
}