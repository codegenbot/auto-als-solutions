string find_max(vector<string> words){
    string max_word = *max_element(words.begin(),words.end(),[&](const string &a,const string &b){return (int)unique(a.begin(),a.end()) < (int)unique(b.begin(),b.end());});
    return max_word;
}