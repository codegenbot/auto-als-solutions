```cpp
#include <string>
#include <cstring>
#include <cassert>

int str_len(std::string str){
    return str.length();
}

int main(){
    assert(strlen("asdasnakj") == 11);
}