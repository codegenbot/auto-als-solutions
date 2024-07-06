#include <iostream>
#include <string>

int main(){
    std::string str;
    std::cout << "Enter your string: ";
    std::cin >> str;

    for (int i = 0; i < str.length(); ++i) {
        if(str[i] >= 'a' && str[i] <= 'z'){
            str[i] = str[i] - 32; // Convert lowercase to uppercase
        }else if(str[i] >= 'A' && str[i] <= 'Z'){
            str[i] = str[i] + 32; // Convert uppercase to lowercase
        }
    }

    std::cout << "Flipped case: " << str << std::endl;
    
    return 0;
}