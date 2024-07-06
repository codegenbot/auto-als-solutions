string get_closest_vowel(string word) {
    for(int i = word.length() - 1; i > 0; --i){
        if(vowel(word[i])){
            int left = i-1;
            while(left >= 0 && !consonant(word[left]))
                left--;
            if(left < 0)
                return "";
            int right = i+1;
            while(right < word.length() && !consonant(word[right]))
                right++;
            if(right == word.length())
                return "";
            return string(1,word[i]);
        }
    }
    return "";
}

bool vowel(char c){
    c = tolower(c);
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

bool consonant(char c){
    c = tolower(c);
    return (!isalpha(c) || vowel(c));
}