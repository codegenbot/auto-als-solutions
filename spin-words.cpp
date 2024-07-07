#include <vector>
#include <iostream>
#include <string>

std::string spinWords(const std::string& input) {
    std::vector<std::string> words;
    std::stringstream ss(input);
    std::string word;

    while (ss >> word) {
        if (word.length() >= 5)
            std::reverse(word.begin(), word.end());
        words.push_back(word);
    }

    std::stringstream output;
    for (auto it = words.begin(); it != words.end(); ++it) {
        output << *it << " ";
    }
    
    return output.str();
}

int main() {
    // Testing the code
    std::cout << spinWords("a") << std::endl;  // Output: a
    std::cout << spinWords("this is a test") << std::endl;  // Output: this is a test
    std::cout << spinWords("this is another test") << std::endl;  // Output: this is rehtona test
    std::cout << spinWords("hi") << std::endl;  // Output: hi
    
    return 0;
}