#include <vector>
#include <algorithm>

bool issame(vector<string> a, vector<string> b) {
    if (a.size() != b.size()) return false;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) return false;
    }
    return true;
}

vector<string> by_length(vector<int> arr) {
    vector<std::vector<string>> result;
    for (int num : arr) {
        if (num >= 1 && num <= 9) {
            vector<std::string> nums;
            for (int i = 0; i < num; i++) {
                switch (i % 10 + 1) {
                    case 1:
                        nums.push_back("One");
                        break;
                    case 2:
                        nums.push_back("Two");
                        break;
                    case 3:
                        nums.push_back("Three");
                        break;
                    case 4:
                        nums.push_back("Four");
                        break;
                    case 5:
                        nums.push_back("Five");
                        break;
                    case 6:
                        nums.push_back("Six");
                        break;
                    case 7:
                        nums.push_back("Seven");
                        break;
                    case 8:
                        nums.push_back("Eight");
                        break;
                    case 9:
                        nums.push_back("Nine");
                        break;
                }
            }
            if (issame(result, vector<std::string>({""}))) {
                result = nums;
            } else {
                for (int i = 0; i < result.size(); i++) {
                    if (!issame(result[i], nums)) {
                        result.push_back(nums);
                        break;
                    }
                }
                if (result.size() == 0) {
                    result.push_back(nums);
                }
            }
        }
    }
    return result;
}