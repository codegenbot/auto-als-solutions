```cpp
#include <vector>
#include <algorithm>

string words_in_sentence(string sentence) {
    vector<string> words;
    size_t start = 0;
    while (start < sentence.size()) {
        size_t end = start;
        while (end + 1 <= sentence.size() && !isalpha(sentence[end])) {
            end++;
        }
        if (end > start) {
            words.push_back(sentence.substr(start, end - start));
        }
        start = end + 1;
    }

    string result;
    for (const auto& word : words) {
        size_t length = word.size();
        bool is_prime = false;
        for (size_t i = 2; i * i <= length; i++) {
            if (length % i == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime) {
            result += word + " ";
        }
    }

    return result.substr(0, result.find(" "));
}