#include <iostream>
#include <string>

int main(){
    std::string str;
    std::cin >> str;
    int i = 0;
    string filp_case(std::string s){
        while(i < s.length()){
            if(s[i] >= 'a' && s[i] <= 'z'){
                s[i] -= 32; // Convert lowercase to uppercase
            }else if(s[i] >= 'A' && s[i] <= 'Z'){
                s[i] += 32; // Convert uppercase to lowercase
            }
            i++;
        }
        return s;
    }
    std::cout << filp_case(str) << std::endl;
    return 0;
}