```
#include <vector>

int filterSpecialNumbers(const std::vector<int>& numbers){
    int count = 0;
    for(int num : numbers){
        if(num > 10 && (num % 10) % 2 != 0 && (num / 10) % 10 % 2 != 0){
            count++;
        }
    }
    return count;
}