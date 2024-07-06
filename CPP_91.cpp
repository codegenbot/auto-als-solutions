int is_bored(string S){
    int count = 0;
    string sentence;

    for(int i=0; i<S.length(); i++){
        if(S[i] == '.' || S[i] == '?' || S[i] == '!'){
            string word = S.substr(0, i);
            if(word.find("I") != string::npos)
                count++;
            sentence.clear();
            S.erase(0, i+1);
        }
        else {
            sentence += S[i];
        }
    }

    // last sentence
    string word = S;
    if(word.find("I") != string::npos)
        count++;

    return count;
}