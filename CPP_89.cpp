string encrypt(string s){
    string result = "";
    for(int i=0; i<s.size(); i++){
        char c = (char)(s[i] + 2*2);
        if(c>'z'){
            c -=26;
        }
        result += c;
    }
    return result;
}