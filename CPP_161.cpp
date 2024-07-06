string solve(string s){
    string result = "";
    for(int i=0; i<s.size(); i++){
        if(isalpha(s[i])){
            char c = tolower(s[i]);
            if(c >= 'a' && c <= 'z')
                c -= ('a' - 'A');
            result += c;
        }
        else
            result += s[i];
    }
    if(result.empty())
        return string(1, '\0');
    return (result[0] == result.back()) ? result.substr(1) + result[0] : result;
}