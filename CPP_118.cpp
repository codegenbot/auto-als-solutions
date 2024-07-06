```cpp
#include <iostream>
#include <string>

std::string get_closest_vowel(std::string str) {
    int min_dist = std::numeric_limits<int>::max();
    char closest_vowel = '\0';
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u' ||
            str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U') {
            int dist = i;
            if (dist < min_dist) {
                min_dist = dist;
                closest_vowel = str[i];
            }
        }
    }
    return std::string(1, closest_vowel);
}

int main() {
    std::string word;
    std::cout << "Enter a word: ";
    std::cin >> word;
    std::cout << "The closest vowel is: " << get_closest_vowel(word) << std::endl;
    return 0;
}