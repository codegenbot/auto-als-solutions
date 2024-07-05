```cpp
#include <vector>
#include <string>

bool isSame(vector<string> a, vector<string> b){
    if(a.size() != b.size()) return false;
    for(auto str : a){
        if(std::find(b.begin(), b.end(), str) == b.end()) return false;
    }
    return true;
}

vector<string> filter_by_substring(vector<string> strings, string substring){
    vector<string> result;
    for(auto str : strings){
        if(str.find(substring) != std::string::npos){
            result.push_back(str);
        }
    }
    return result;
}

int main(){
    assert(isSame(filter_by_substring({"grunt", "trumpet", "prune", "gruesome"}, "run") ,{"grunt", "prune"}));
    return 0;
}