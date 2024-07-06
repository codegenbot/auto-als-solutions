#include <iostream>
#include <vector>
#include <algorithm>

bool issame(const std::vector<std::string>& v1, const std::vector<std::string>& v2) {
    if (v1.size() != v2.size()) return false;
    for (int i = 0; i < v1.size(); ++i) {
        if (v1[i] != v2[i]) return false;
    }
    return true;
}

std::vector<std::string> by_length(std::vector<int> arr) {
    std::vector<int> temp;
    for (int i : arr) {
        if (i >= 1 && i <= 9) {
            temp.push_back(i);
        }
    }

    std::sort(temp.begin(), temp.end());
    std::reverse(temp.begin(), temp.end());

    std::vector<std::string> result;
    for (int i : temp) {
        switch (i) {
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
    std::vector<int> arr = {1, 2, 3, 4, 5};
    std::vector<std::string> res = by_length(arr);

    for (const auto& str : res) {
        std::cout << str << " ";
    }
    std::cout << std::endl;

    return 0;
}