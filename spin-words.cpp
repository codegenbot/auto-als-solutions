#include <iostream>
#include <string>

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

int main() {
    std::cout << spinWords("a") << "\n";
    std::cout << spinWords("this is a test") << "\n";
    std::cout << spinWords("this is another test") << "\n";
    std::cout << spinWords("hi") << "\n";
    return 0;
}