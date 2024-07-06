string remove_vowels(string text){
    string result = "";
    for (char c : text) {
        if (!ispunct(c) && !isupper(c) && !islower(c)) continue;
        bool isVowel = false;
        switch (tolower(c)) {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
                isVowel = true;
                break;
        }
        if (!isVowel) result += c;
    }
    return result;
}