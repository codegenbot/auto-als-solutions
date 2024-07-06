#include <iostream>
#include <string>

int main(){
    std::string str;
    std::cin >> str;
    int i = 0;
    string filp_case(std::string str){
        while(i < str.length()){
            if(str[i] >= 'a' && str[i] <= 'z'){
                str[i] = (char)(str[i] - 32); // Convert lowercase to uppercase
            }else if(str[i] >= 'A' && str[i] <= 'Z'){
                str[i] = (char)(str[i] + 32); // Convert uppercase to lowercase
            }
            i++;
        }
        return str;
    }
    std::cout << filp_case(str) << std::endl;
    return 0;
}