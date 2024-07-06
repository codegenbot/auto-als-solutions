bool is_happy(string s){
    int len = s.length();
    if(len < 3) return false;
    for(int i=0; i<len-2; i++){
        bool found[3] = {false};
        for(int j=0; j<3; j++){
            found[j] = (s[i+j] == s[(i+1)%len] || s[i+j] == s[(i+2)%len]);
        }
        if(!found[0] && !found[1] && !found[2]) return false;
    }
    return true;
}