std::string spinWords(std::string sentence) {
    std::vector<std::string> words;
    std::istringstream iss(sentence);
    std::string word;

    while (iss >> word) {
        if (word.length() >= 5)
            word = std::string(word.rbegin(), word.rend());
        words.push_back(word);
    }

    sentence = ""; 
    for (int i = 0; i < words.size(); ++i) {
        sentence += words.back();
        if (i != words.size() - 1)
            sentence += " "; 
        else
            words.pop_back(); 
    }
    return sentence;
}