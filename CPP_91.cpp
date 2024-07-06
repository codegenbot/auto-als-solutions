int is_bored(string S){
    int boredom_count = 0;
    size_t start = 0;
    
    while((start = S.find("I", start)) != string::npos) {
        if (S[start] == 'I' && (S.find('.', start+1) == string::npos 
                && S.find('?', start+1) == string::npos 
                && S.find('!', start+1) == string::npos)) {
            boredom_count++;
        }
        start++;
    }
    
    return boredom_count;
}