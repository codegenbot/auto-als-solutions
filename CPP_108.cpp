#include <vector>
#include <initializer_list>

int count_nums(std::vector<int> nums) {
    int count = 0;
    for (int num : nums) {
        bool has_positive_sum = false;
        if (num < 0) {
            num = -num;
        }
        while (num > 0) {
            int digit = num % 10;
            if (digit != 0) {
                has_positive_sum = true;
                break;
            }
            num /= 10;
        }
        if (has_positive_sum) {
            count++;
        }
    }
    return count;
}

int main() {
    int n;
    std::vector<int> nums;
    std::cout << "Enter the number of integers: ";
    std::cin >> n;

    for(int i = 0; i < n; i++) {
        int num;
        std::cout << "Enter integer number " << (i+1) << ": ";
        std::cin >> num;
        nums.push_back(num);
    }
    
    std::cout << "Number of integers with positive sum of digits: " << count_nums(nums) << std::endl;

    return 0;
}