#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;

int main() {
    string input;
    getline(cin, input);
    
    stringstream ss(input);
    string word, result;
    
    while (ss >> word) {
        if (word.length() >= 5) {
            reverse(word.begin(), word.end());
        }
        if (!result.empty()) {
            result += " ";
        }
        result += word;
    }
    
    cout << result << endl;
    return 0;
}