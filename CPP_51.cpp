#include <iostream>
#include <string>

std::string remove_vowels(std::string text){
    std::string result = "";
    for(char c : text){
        if(toupper(c) != 'A' && toupper(c) != 'E' && toupper(c) != 'I' && toupper(c) != 'O' && toupper(c) != 'U'){
            result += c;
        }
    }
    return result;
}

int main(){
    std::string text;
    std::cout << "Enter a string: ";
    std::getline(std::cin, text);
    std::cout << "String with vowels removed: " << remove_vowels(text) << std::endl;
    return 0;
}