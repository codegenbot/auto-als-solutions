#include <iostream>
#include <string>
using namespace std;

int i = 0;
std::string flip_case(std::string str){
    while(i < str.length()){
        if(str[i] >= 'a' && str[i] <= 'z'){
            str[i] -= 32; // Convert lowercase to uppercase
        }else if(str[i] >= 'A' && str[i] <= 'Z'){
            str[i] += 32; // Convert uppercase to lowercase
        }
        i++;
    }
    return str;
}