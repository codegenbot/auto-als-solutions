```
#include <iostream>
#include <string>

std::string solve(std::string s){
    std::string result = "";
    for(int i=0; i<s.length(); i++){
        if(std::isalpha(s[i])){
            result += (s[i] >= 'a' && s[i] <= 'z') ? std::toupper(s[i]) : std::tolower(s[i]);
        }else{
            result += s[i];
        }
    }
    return result;
}

int main(){
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    
    if(input.empty()){
        std::cout << "Error! You must enter a valid string." << std::endl;
    } else {
        std::string output = solve(input);
        std::cout << "Output: " << output << std::endl;
    }
    return 0;
}