#include <string>
#include <cctype>

string get_closest_vowel(string word) {
    int left = 0, right = word.size() - 1;
    bool found = false;
    while (left <= right && !found) {
        if (!isvowel(word[left])) left++;
        else if (!isconsonant(word[right])) right--;
        else found = true;
    }
    for (int i = left; i <= right; i++) {
        if (isvowel(word[i]))
            return string(1, word[i]);
    }
    return "";
}

bool isvowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

bool isconsonant(char c) {
    c = tolower(c);
    return !isvowel(c) && (c >= 'b' && c <= 'z');
}