int is_bored(string S){
    int boredom_count = 0;
    string word;
    size_t pos = 0;

    while((pos = S.find('.', pos)) != string::npos || 
          (pos = S.find('?', pos)) != string::npos || 
          (pos = S.find('!', pos)) != string::npos){
        size_t start = pos;
        if(start > 0) {
            for(size_t i = 0; i < 2; ++i, ++start)
                if(S[start] != ' ')
                    break;
        }
        word = S.substr(start, pos - start);
        if(word == "I") 
            boredom_count++;
        pos = start + (pos > start ? 1 : 0);
    }

    return boredom_count;
}