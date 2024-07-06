```cpp
#include <iostream>
#include <string>
using namespace std;

std::string get_closest_vowel(std::string str) {
    int min_dist = numeric_limits<int>::max();
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
    return string(1, closest_vowel);
}

int main() {
    string word;
    cout << "Enter a word: ";
    getline(cin, word);
    cout << "The closest vowel is: " << get_closest_vowel(word) << endl;
    return 0;
}