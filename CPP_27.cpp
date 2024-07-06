#include <iostream>
#include <string>
using namespace std;

int i = 0;
std::string flip_case(std::string str){
    while(i < str.length()){
        if(str[i] >= 'a' && str[i] <= 'z'){
            str[i] -= 32; 
        }else if(str[i] >= 'A' && str[i] <= 'Z'){
            str[i] += 32; 
        }
        i++;
    }
    return str;
}