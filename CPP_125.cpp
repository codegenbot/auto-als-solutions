#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

vector<string> split_words(string txt) {
    vector<string> result;
    string word = "";
    
    for (char c : txt) {
        if (!isspace(c)) { // Check if character is a whitespace
            word += c;
        } else if (!word.empty()) {
            result.push_back(word);
            word = "";
        }
    }
    
    if (!word.empty())
        result.push_back(word);
    
    if (result.size() == 0) {
        int count = 0;
        for (char c : txt) {
            if (c >= 'a' && c <= 'z') {
                count += (int)(c - 'a');
                if (count % 2 != 0)
                    result.push_back(to_string(count));
            }
        }
    }
    
    return result;
}