#include <string>

string get_closest_vowel(string word) {
    int left = 0;
    for(int right = word.size() - 1; right >= 0; --right) {
        if(!isvowel(word[right])) continue;
        while(right > left && !isconsonant(word[right-1]))
            right--;
        return string(1, word[right]);
    }
    return "";
}

bool isvowel(char c) {
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
            || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
}

bool isconsonant(char c) {
    return !isvowel(c);
}