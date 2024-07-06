#include <string>
#include <cctype>

std::string flip_case(std::string str){
    std::string result = "";
    for(int i=0; i<str.length();i++){
        if(isalpha(str[i])){
            if(islower(str[i]))
                result += toupper(str[i]);
            else
                result += tolower(str[i]);
        }else{
            result.append(1, str[i]);
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