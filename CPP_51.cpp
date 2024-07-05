#include <string>
#include <cctype>

std::string remove_vowels(std::string text){
    std::string result = "";
    for(char c : text){
        if(std::toupper(c) != 'A' && std::toupper(c) != 'E' && std::toupper(c) != 'I' && std::toupper(c) != 'O' && std::toupper(c) != 'U'){
            result += c;
        }
    }
    return result;
}

int main() {
    string text;
    cout << "Enter a string: ";
    cin >> text;
    string output = remove_vowels(text);
    cout << "String after removing vowels: " << output << endl;
    return 0;
}