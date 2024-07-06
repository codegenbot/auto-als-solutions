string anti_shuffle(string s){
    string result = "";
    int i = 0;
    while(i<s.size()){
        if(s[i] == ' '){
            result += ' ';
            i++;
            continue;
        }
        int j = i + 1;
        for(;j<s.size() && s[j] != ''; j++){
            
        }
        string word = s.substr(i, j - i);
        for(int k=word.size()-1; k>=0; k--){
            result += word[k];
        }
        i = j;
    }
    return result;
}