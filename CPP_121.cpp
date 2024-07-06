```cpp
#include <vector>
#include <algorithm>

std::vector<int> lst = {1,2,3,4,5};

int solution(std::vector<int> lst) {
    int sum = 0;
    for (int i = 1; i < lst.size(); i++) {
        if (lst[i] % 2 != 0) {
            sum += lst[i];
        }
    }
    return sum;

}

int main() { 
    return solution(lst); 
}