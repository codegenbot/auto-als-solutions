#include <iostream>
#include <string>
#include <vector>

int smallest_change(std::vector<int> arr) {
    int n = arr.size();
    std::string str = "";
    for (int i : arr) {
        str += std::to_string(i);
    }
    int left = 0, right = n - 1;
    int changes = 0;
    while (left < right) {
        if (str[left] != str[right]) {
            changes++;
            if (str[left] == str[right - 1]) {
                right--;
            } else if (str[right] == str[left + 1]) {
                left++;
            } else {
                break;
            }
        } else {
            left++;
            right--;
        }
    }
    return changes;

}

int main() {
    std::assert(smallest_change({0, 1}) == 1);
    return 0;
}