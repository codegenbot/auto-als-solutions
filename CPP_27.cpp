```c++
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

int main {
    std::string s;
    std::cout << "Enter a string: ";
    std::getline(std::cin, s);
    std::cout << "Flip case: " << flip_case(s) << std::endl;
}