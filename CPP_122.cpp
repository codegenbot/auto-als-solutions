#include <iostream>
#include <vector>
#include <cmath>

int add_elements(std::vector<int> arr, int k){
    int sum = 0;
    for(int i=0; i<k; i++){
        if(log10(arr[i]+1) <= 2){
            sum += arr[i];
        }
    }
    return sum;
}

int main() {
    std::vector<int> input = {1, 3, 5};
    int k = 3;
    assert (add_elements(input, k) == 9);
    return 0;
}