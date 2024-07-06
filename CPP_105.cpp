```cpp
#include <vector>
#include <algorithm>

bool issame(std::vector<std::string> v1, std::vector<std::string> v2) {
    if(v1.size() != v2.size())
        return false;
    for(int i = 0; i < v1.size(); i++)
        if(v1[i] != v2[i])
            return false;
    return true;
}

std::vector<std::string> by_length(std::vector<int> arr) {
    std::vector<std::pair<int, int>> temp;
    for (int i : arr) {
        if (i >= 1 && i <= 9) {
            if(i == 1) temp.push_back({1, i});
            else if(i == 2) temp.push_back({2, i});
            else if(i == 3) temp.push_back({3, i});
            else if(i == 4) temp.push_back({4, i});
            else if(i == 5) temp.push_back({5, i});
            else if(i == 6) temp.push_back({6, i});
            else if(i == 7) temp.push_back({7, i});
            else if(i == 8) temp.push_back({8, i});
            else temp.push_back({9, i});
        }
    }

    std::sort(temp.begin(), temp.end());
    std::reverse(temp.begin(), temp.end());

    std::vector<std::string> result;
    for (auto& t : temp) {
        if(t.first == 1)
            result.push_back("One");
        else if(t.first == 2)
            result.push_back("Two");
        else if(t.first == 3)
            result.push_back("Three");
        else if(t.first == 4)
            result.push_back("Four");
        else if(t.first == 5)
            result.push_back("Five");
        else if(t.first == 6)
            result.push_back("Six");
        else if(t.first == 7)
            result.push_back("Seven");
        else if(t.first == 8)
            result.push_back("Eight");
        else
            result.push_back("Nine");
    }

    return result;
}

int main() {
    std::vector<int> arr = {9, 4, 8};
    std::vector<std::string> result = by_length(arr);
    if (!issame({{"One"}}, {result})) {
        return 1; 
    }
    return 0;
}