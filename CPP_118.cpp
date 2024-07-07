Here is the solution:

string get_closest_vowel(string word) {
    int i = word.size() - 1;
    while (i > 0 && !isVowel(word[i])) {
        --i;
    }
    if (i == 0 || !isVowel(word[i]))
        return "";
    for (; i > 0; --i) {
        if (!isConsonant(word[i-1]) && isVowel(word[i])) {
            return string(1, word[i]);
        }
    }
    return "";
}

bool isVowel(char c) {
    c = tolower(c);
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

bool isConsonant(char c) {
    c = tolower(c);
    return (!isVowel(c));
}