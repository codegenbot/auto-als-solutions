#include <vector>
#include <algorithm>
#include <string>

bool issame(std::vector<std::string> a, std::vector<std::string> b) {
    if(a.size() != b.size())
        return false;
    for(int i = 0; i < a.size(); i++)
        if(a[i] != b[i])
            return false;
    return true;
}

std::vector<std::string> by_length(std::vector<int> arr) {
    std::vector<std::pair<int, int>> temp;
    for (int i : arr) {
        if (i >= 1 && i <= 9) {
            temp.push_back({(i == 1)? 1 : ((i == 2)? 2 : ((i == 3)? 3 : ((i == 4)? 4 : ((i == 5)? 5 : ((i == 6)? 6 : ((i == 7)? 7 : ((i == 8)? 8 : 9)))))))))), i});
        }
    }

    std::sort(temp.begin(), temp.end());
    std::reverse(temp.begin(), temp.end());

    std::vector<std::string> result;
    for (auto& t : temp) {
        switch(t.first) {
            case 1:
                result.push_back("One");
                break;
            case 2:
                result.push_back("Two");
                break;
            case 3:
                result.push_back("Three");
                break;
            case 4:
                result.push_back("Four");
                break;
            case 5:
                result.push_back("Five");
                break;
            case 6:
                result.push_back("Six");
                break;
            case 7:
                result.push_back("Seven");
                break;
            case 8:
                result.push_back("Eight");
                break;
            case 9:
                result.push_back("Nine");
                break;
        }
    }

    return result;
}

int main() {
    std::vector<int> arr = {9, 4, 8};
    std::vector<std::string> result = by_length(arr);
    if (!issame(result, {"Nine", "Four", "Eight"})) {
        return 1; 
    }
    return 0;
}