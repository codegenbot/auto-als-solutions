string anti_shuffle(string s){
    string result = "";
    for(int i=0; i<s.length();i++){
        if(s[i] == ' '){
            result += " ";
        }else{
            string word;
            for(int j=i; j<=s.find(' ', i);j++){
                word += s[j];
            }
            sort(word.begin(), word.end());
            for(int k=0; k<word.length();k++){
                result += word[k];
            }
            i = s.find(' ', i);
        }
    }
    return result;
}