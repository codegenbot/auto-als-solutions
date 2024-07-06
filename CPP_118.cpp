```c++
#include <iostream>
#include <string>

std::string get_closest_vowel(std::string str) {
    int min_dist = std::numeric_limits<int>::max();
    char closest_vowel = '\0';
    for (int i = 0; i < str.length(); i++) {
        if ((str[i] >= 'a' && str[i] <= 'z') || (str[i] >= 'A' && str[i] <= 'Z')) {
            if ((str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u'
                || str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U')) {
                if (min_dist > i) {
                    min_dist = i;
                    closest_vowel = str[i];
                }
            }
        }
    }
    return std::string(1, closest_vowel);
}

int main() {
    std::cout << "Enter a word: ";
    std::string word;
    std::cin >> word;
    std::cout << "The closest vowel is: " << get_closest_vowel(word) << std::endl;
    return 0;
}