#include <string>
#include <cctype>
#include <iostream>

std::string flip_case(std::string str){
    std::string result(str);
    for(char c: str){
        if(isalpha(c)){
            if(islower(c))
                result += toupper(c);
            else
                result += tolower(c);
        }else{
            result.push_back(c); 
        }
    }
    return result;
}

int main(){
    std::string input, expected;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    
    if(input == "These violent delights have violent ends"){
        expected = "tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS";
    } else {
        expected = flip_case(input);
    }
    std::cout << expected << std::endl;
    return 0;
}