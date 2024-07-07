Here is the solution:

#include <string>
using namespace std;

string spinWords(string input) {
    string output = "";
    string word = "";
    
    for (char c : input) {
        if (c == ' ') {
            if (word.length() >= 5) {
                for (int i = word.length() - 1; i >= 0; --i)
                    output += word[i];
                output += ' ';
            } else
                output += word + ' ';
            word = "";
        } else {
            word += c;
        }
    }
    
    if (word.length() >= 5) {
        for (int i = word.length() - 1; i >= 0; --i)
            output += word[i];
    } else
        output += word;
    
    return output;
}