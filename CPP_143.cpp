string words_in_sentence(string sentence){
    vector<int> prime_numbers;
    for(int i=2; i<=100; i++){
        bool is_prime = true;
        for(int j=2; j*j <= i; j++){
            if(i % j == 0) {
                is_prime = false;
                break;
            }
        }
        if(is_prime) prime_numbers.push_back(i);
    }

    string result = "";
    vector<string> words = split(sentence, ' ');
    for(string word : words){
        if(find(prime_numbers.begin(), prime_numbers.end(), word.length()) != prime_numbers.end())
            result += word + " ";
    }
    return result.substr(0, result.size()-1);
}

vector<string> split(string str, char symbol) {
    vector<string> tokens;
    size_t pos = 0;
    while((pos = str.find(symbol)) != string::npos) {
        tokens.push_back(str.substr(0, pos));
        str.erase(0, pos + 1);
    }
    tokens.push_back(str);
    return tokens;
}