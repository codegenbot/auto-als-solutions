```cpp
#include <iostream>
#include <string>

int main(){
    std::string str;
    std::cin >> str;
    int i = 0;
    for(i = 0; i < str.length(); i++){
        if(str[i] >= 'a' && str[i] <= 'z'){
            str[i] = (char)toupper((int)str[i]); // Convert lowercase to uppercase
        }else if(str[i] >= 'A' && str[i] <= 'Z'){
            str[i] = (char)tolower((int)str[i]); // Convert uppercase to lowercase
        }
    }
    std::cout << str;
    return 0;
}