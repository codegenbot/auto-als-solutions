#include <string>
#include <map>
#include <cctype>

bool check_dict_case(const std::map<std::string, std::string>& dict) {
    for (const auto& pair : dict) {
        if (!pair.first.empty() && 
            (!std::isupper(pair.first[0]) || !std::islower(pair.first[0])) 
        ) 
            return false;
    }
    return true;
}

int main() {
    std::map<std::string, std::string> myDict = {{"Hello", "world"}, {"This", "is"}};
    assert(check_dict_case(myDict));
    return 0;
}