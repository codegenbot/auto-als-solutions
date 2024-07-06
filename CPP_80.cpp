bool is_happy(string s){
    if(s.length() < 3) return false;
    for(int i=0; i<s.length()-2; i++){
        bool distinct = true;
        for(int j=i+1; j<i+4 && j<s.length(); j++){
            if(s[j] == s[i]){
                distinct = false;
                break;
            }
        }
        if(!distinct) return false;
    }
    return true;
}