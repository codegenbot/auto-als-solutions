#include <string>
#include <cstring>

int str_len(std::string str){
    return str.length();
}

int main(){
    assert(strlen("asdasnakj") == 9);
}