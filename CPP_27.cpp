```cpp
#include <iostream>
#include <string>

int main(){
    std::string str;
    int i = 0;
    std::string filp_case(std::string s){
        for(i = 0; i < s.length(); i++){
            if(s[i] >= 'a' && s[i] <= 'z'){
                s[i] = (s[i] - 'a' + 'A'); // Convert lowercase to uppercase
            }else if(s[i] >= 'A' && s[i] <= 'Z'){
                s[i] = (s[i] - 'A' + 'a'); // Convert uppercase to lowercase
            }
        }
        return s;
    }
    
    std::cout << "Enter a string: ";
    std::cin >> str;

    std::cout << "Flipped case of the input string is: " << filp_case(str) << std::endl;

    return 0;
}