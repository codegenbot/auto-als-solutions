```cpp
#include <string>

int is_bored(std::string S) {
    if(S.find("bored") == std::string::npos)
        return 0;
    else
        return 1;
}