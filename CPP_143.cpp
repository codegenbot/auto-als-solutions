#include <string>
#include <vector>

std::string words_in_sentence(std::string sentence) {
    std::string result = "";
    std::vector<int> primeNumbers;
    for (int i = 2; i <= 100; i++) {
        bool isPrime = true;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime)
            primeNumbers.push_back(i);
    }

    std::vector<std::string> words = split(sentence, ' ');
    for (std::string word : words) {
        if (find(primeNumbers.begin(), primeNumbers.end(), word.length()) != primeNumbers.end())
            result += word + " ";
    }
    return result.substr(0, result.size() - 1);
}

std::vector<std::string> split(const std::string& str, char ch) {
    std::vector<std::string> tokens;
    size_t pos = 0;
    while ((pos = str.find(ch)) != std::string::npos) {
        tokens.push_back(str.substr(0, pos));
        str.erase(0, pos + 1);
    }
    tokens.push_back(str);
    return tokens;

}

int main() {
    assert(words_in_sentence("here is") == "is");
    return 0;
}