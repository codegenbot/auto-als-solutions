string anti_shuffle(string s){
    string result = "";
    for(int i=0; i<s.length(); i++){
        if(s[i] == ' '){
            result += ' ';
            continue;
        }
        string word = "";
        for(int j=i; j<s.length() && s[j] != ' '; j++){
            word += s[j];
            int temp = 0;
            for(char c : word) {
                temp = min(temp, (int)c);
            }
            while(i <= j){
                if(s[i] == temp) {
                    result += s[i];
                    i++;
                    break;
                } else {
                    i++;
                }
            }
        }
    }
    return result;
}