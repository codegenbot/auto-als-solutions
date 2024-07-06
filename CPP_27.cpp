#include <iostream>
#include <string>
using namespace std;

std::string filp_case(std::string str){
    for(int i = 0; i < str.length(); i++){
        if(str[i] >= 'a' && str[i] <= 'z'){
            str[i] = toupper(str[i]); // Convert lowercase to uppercase
        }else if(str[i] >= 'A' && str[i] <= 'Z'){
            str[i] = tolower(str[i]); // Convert uppercase to lowercase
        }
    }
    return str;
}