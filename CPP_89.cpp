string encrypt(string s){
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    string result = "";
    
    for(int i=0; i<s.length(); i++){
        char c = tolower(s[i]);
        int pos = alphabet.find(c);
        
        if(pos != -1){
            pos = (pos + 2*2) % 26;
            result += alphabet[pos];
        }
        else{
            result += s[i];
        }
    }
    
    return result;
}