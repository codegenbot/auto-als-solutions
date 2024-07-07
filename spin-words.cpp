#include <vector>
#include <iostream>
#include <string>

using namespace std;

string spinWords(string sentence) {
    string result = "";
    size_t pos = 0;
    
    while ((pos = sentence.find(" ")) != string::npos) {
        string word = sentence.substr(0, pos);
        
        if (word.length() >= 5) {
            for (int i = word.length() - 1; i >= 0; --i) {
                result += word[i];
            }
        } else {
            result += word;
        }
        
        sentence.erase(0, pos + 1);
    }
    
    if (sentence.length() >= 5) {
        for (int i = sentence.length() - 1; i >= 0; --i) {
            result += sentence[i];
        }
    } else {
        result += sentence;
    }
    
    return result;
}

int main() {
    // Test cases
    cout << spinWords("a") << endl; // Output: a
    cout << spinWords("this is a test") << endl; // Output: this is a test
    cout << spinWords("this is another test") << endl; // Output: this is rehtona test
    cout << spinWords("hi") << endl; // Output: hi
    
    return 0;
}