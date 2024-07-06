#include <cctype>
#include <string>

string remove_vowels(string text) {
    string result = "";
    for (char c : text) {
        if (!isvowel(c)) {
            result += c;
        }
    }
    return result;
}

bool isvowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main() {
    string text;
    cout << "Enter a sentence: ";
    getline(cin, text);
    string result = remove_vowels(text);
    cout << "Sentence without vowels: " << result << endl;
    return 0;
}