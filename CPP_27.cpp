#include <iostream>
#include <string>

int main(){
    std::string str;
    std::cout << "Enter a string: ";
    std::cin >> str;
    
    for(int i = 0; i < str.length(); i++){
        if(str[i] >= 'a' && str[i] <= 'z'){
            str[i] = (char)(str[i] - 32); // Convert lowercase to uppercase
        }else if(str[i] >= 'A' && str[i] <= 'Z'){
            str[i] = (char)(str[i] + 32); // Convert uppercase to lowercase
        }
    }
    
    std::cout << "Flipped case string: " << str << std::endl;
    
    return 0;
}