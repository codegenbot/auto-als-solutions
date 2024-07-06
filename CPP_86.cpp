#include <algorithm>
#include <sstream>

using namespace std;

string anti_shuffle(string s) {
    string result = "";
    istringstream iss(s);
    string word;
    
    while (iss >> word) {
        for (char c : word) {
            result += c;
        }
        
        for (int i = 0; i < word.length(); ++i) {
            if (i > 0) {
                result += ' ';
            }
            char minC = word[0];
            int minIndex = 0;
            
            for (int j = 1; j <= word.length() - i; ++j) {
                if (word[j] < minC) {
                    minC = word[j];
                    minIndex = j;
                }
            }
            
            result += minC;
        }
    }
    
    return result;
}