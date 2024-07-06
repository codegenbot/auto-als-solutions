#include <string>
#include <cctype>

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
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    std::cout << flip_case(input) << std::endl;
    return 0;
}