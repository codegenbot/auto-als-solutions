string solve(string s){
    string result = "";
    for(int i=0; i<s.length(); i++){
        if(isalpha(s[i])){
            char c = s[i];
            if(c >= 'a' && c <= 'z') c -= 32;
            else if(c >= 'A' && c <= 'Z') c += 32;
            result += c;
        }else{
            result += s[i];
        }
    }
    return result;
}