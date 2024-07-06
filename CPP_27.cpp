```cpp
#include <iostream>
#include <string>

int main(){
    std::string str;
    int i = 0;
    
    std::cout << "Enter a string: ";
    std::cin >> str;
    
    for(i = 0; i < str.length(); i++){
        if(str[i] >= 'a' && str[i] <= 'z'){
            str[i] = toupper(str[i]);
        }else if(str[i] >= 'A' && str[i] <= 'Z'){
            str[i] = tolower(str[i]);
        }
    }
    
    std::cout << "The flipped case of the string is: " << str << std::endl;
    
    return 0;
}