#include <vector>
#include <algorithm>
#include <string>

bool issame(std::vector<std::string> v1, std::vector<std::string> v2) {
    if(v1.size() != v2.size())
        return false;
    for(int i = 0; i < v1.size(); i++)
        if(v1[i] != v2[i])
            return false;
    return true;
}

std::vector<std::string> by_length(std::vector<int> arr) {
    std::vector<int> temp;
    for (int num : arr) {
        switch(num){
            case 1:
            case 2:
            case 3:
                temp.push_back(num);
                break;
            default: 
                continue; 
        }
    }

    sort(temp.begin(), temp.end());
    reverse(temp.begin(), temp.end());

    std::vector<std::string> result;
    for (int num : temp) {
        switch(num){
            case 1: 
                result.push_back("One");
                break;
            case 2:
                result.push_back("Two");
                break;
            case 3:
                result.push_back("Three");
                break;
            default:
                continue; 
        }
    }

    return result;
}

int main() {
    assert (issame(by_length({9, 4, 8}) , {"Nine", "Four", "Eight"}));
    return 0;
}