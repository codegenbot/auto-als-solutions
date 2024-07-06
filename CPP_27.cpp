```cpp
#include <iostream>
#include <string>

int main(){
    std::string str;
    int i = 0;

    std::cin >> str;

    for(i = 0; i < str.length(); i++){
        if(str[i] >= 'a' && str[i] <= 'z'){
            str[i] = str[i] - 32; // Convert lowercase to uppercase
        }else if(str[i] >= 'A' && str[i] <= 'Z'){
            str[i] = str[i] + 32; // Convert uppercase to lowercase
        }
    }

    std::cout << str;

    return 0;
}