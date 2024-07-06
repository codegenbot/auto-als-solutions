#include <iostream>
#include <string>

string get_closest_vowel(string word) {
    for (int i = 0; i < word.length(); ++i) {
        if (word[i] == 'a' || word[i] == 'e' || word[i] == 'i' ||
            word[i] == 'o' || word[i] == 'u') {
            bool isFound = true;
            for (int j = i + 1; j < word.length(); ++j) {
                if (isVowel(word[j])) {
                    isFound = false;
                    break;
                }
            }
            if (!isFound)
                return string(1, word[i]);
        }
    }
    return "";
}

bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main() {
    string str;
    std::cout << "Enter a word: ";
    std::cin >> str;
    cout << get_closest_vowel(str) << endl;
    return 0;
}