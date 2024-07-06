string get_closest_vowel(string word) {
    int n = word.size();
    for (int i = n - 1; i >= 0; --i) {
        if (!isalpha(word[i])) continue;
        if (ispunct(word[i]) || isdigit(word[i])) continue;
        if (word[i] == 'Y' && i > 0 && isupper(word[i-1])) continue;
        if (word[i] == 'y' && i > 0 && isupper(word[i-1])) continue;
        for (int j = i + 1; j < n; ++j) {
            if (!isalpha(word[j])) break;
            if (ispunct(word[j]) || isdigit(word[j])) break;
            if (word[j] == 'Y' && j > 0 && isupper(word[i])) continue;
            if (word[j] == 'y' && j > 0 && isupper(word[i])) continue;
            return string(1, tolower(word[j]));
        }
    }
    return "";
}