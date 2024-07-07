#include <vector>
#include <iostream>
#include <string>

using namespace std;

string spinWords(string sentence) {
    string result = "";
    int i = 0;
    
    while (i < sentence.length()) {
        if (sentence[i] == ' ') {
            result += " ";
            i++;
        } else {
            int j = i + 1;
            while (j <= sentence.length() && sentence[j] != ' ') {
                j++;
            }
            
            string word = sentence.substr(i, j - i);
            
            if (word.length() >= 5) {
                reverse(word.begin(), word.end());
            }
            
            result += word + " ";
            i = j;
        }
    }
    
    return result.substr(0, result.length() - 1);
}

int main() {
    string sentence;
    cout << "Enter a sentence: ";
    getline(cin, sentence);
    cout << "Spin words: " << spinWords(sentence) << endl;
    return 0;
}