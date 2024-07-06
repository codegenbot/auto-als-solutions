Here is the completed code:

string get_closest_vowel(string word){
    int n = word.size();
    for(int i=n-1; i>=0; --i){
        if(word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u'){
            if(i+1 < n && !isvowel(word[i+1]) && i-1 >= 0 && !isvowel(word[i-1]))
                return string(1,word[i]);
        }
    }
    return "";
}

bool isvowel(char c){
    c = tolower(c);
    if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
        return true;
    return false;
}