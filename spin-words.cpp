#include <iostream>
#include <string>
using namespace std;

string spinWords(string sentence) {
    string result = "";
    int wordLength = 0;
    
    for (int i = 0; i < sentence.length(); i++) {
        if (sentence[i] == ' ') {
            if (wordLength >= 5)
                for (int j = wordLength - 1; j >= 0; j--)
                    result += sentence[i - wordLength + j];
            else
                result += sentence.substr(i - wordLength, wordLength);
            wordLength = 0;
        } else {
            wordLength++;
        }
    }
    
    if (wordLength >= 5)
        for (int i = wordLength - 1; i >= 0; i--)
            result += sentence[i];
    else
        result = sentence;
    
    return result;
}

int main() {
    string input;
    cout << "Enter a string of words: ";
    getline(cin, input);
    cout << spinWords(input) << endl;
    return 0;
}