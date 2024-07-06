#include <string>
#include <cctype>

std::string flip_case(std::string str){
    std::string result = "";
    for(char c: str){
        if(isalpha(c)){
            if(islower(c))
                result += toupper(c);
            else
                result += tolower(c);
        }else{
            result += c;
        }
    }
    return result;
}

int main(){
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);

    std::string output = flip_case(input);
    std::cout << "Flipped case: " << output << std::endl;

    return 0;
}