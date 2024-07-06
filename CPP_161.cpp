#include <iostream>
#include <string>

std::string solve(std::string s){
    std::string result = "";
    for(int i=0; i<s.length(); i++){
        if(isalpha(s[i])){
            result += (isupper(s[i])) ? tolower(s[i]) : toupper(s[i]);
        }else{
            result += s[i];
        }
    }
    return result;
}

int main(){
    std::string str;
    std::cout << "Enter a string: ";
    std::getline(std::cin, str);
    if(str.empty()){
        std::cout << "Error: Please enter a non-empty string." << std::endl;
    }else{
        std::cout << solve(str) << std::endl;
    }
    return 0;
}