bool is_palindrome(string text){
    string str = text;
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    for(int i=0; i<str.length()/2; i++){
        if(str[i] != str[str.length()-i-1])
            return false;
    }
    return true;
}