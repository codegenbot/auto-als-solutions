#include <iostream>
#include <string>

std::string get_closest_vowel(std::string word);

int main() {
    std::string word;
    std::cout << "Enter a word: ";
    std::cin >> word;
    std::cout << "The closest vowel is: " << get_closest_vowel(word) << std::endl;
    assert (get_closest_vowel("Above") == "o");
    return 0;
}

std::string get_closest_vowel(std::string word) {
    std::string vowels = "aeiouAEIOU";
    int min_dist = -1, idx_min_dist = -1;
    for(int i = 0; i < word.length(); ++i) {
        if(vowels.find(word[i]) != std::string::npos) {
            if(min_dist == -1) {
                min_dist = i;
                idx_min_dist = i;
            }
            else {
                int dist = i - min_dist;
                if(dist > 0 && (dist < min_dist || idx_min_dist + (min_dist / (idx_min_dist != -1)) < i)) {
                    min_dist = i;
                    idx_min_dist = i;
                }
                else if(i == min_dist) {
                    idx_min_dist++;
                }
            }
        }
    }
    return word.substr(idx_min_dist, 1);
}