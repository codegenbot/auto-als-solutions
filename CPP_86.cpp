string anti_shuffle(string s){
    string result = "";
    for(int i=0; i<s.length(); i++){
        if(s[i] == ' '){
            result += " ";
            continue;
        }
        char temp[s[i]+1];
        temp[0] = s[i];
        temp[1] = '\0';
        for(int j=s[i]; j<=126; j++){
            temp[1] = (char)j;
            result += temp;
        }
    }
    return result;
}