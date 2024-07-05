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

int main(){
    std::string text;
    std::cout << "Enter the string: ";
    std::cin >> text;
    std::cout << "The string after removing vowels is: " << remove_vowels(text) << std::endl;
    return 0;
}