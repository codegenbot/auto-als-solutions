#include <iostream>
#include <vector>

std::vector<int> pluck(const std::vector<int>& arr) {
    std::vector<int> result = {};
    int minEvenValueIndex = -1;
    int minEvenValue = INT_MAX;

    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0 && arr[i] < minEvenValue){
            minEvenValue = arr[i];
            minEvenValueIndex = i;
        }
    }

    if(minEvenValue != INT_MAX){
        result.push_back(minEvenValue);
        result.push_back(minEvenValueIndex);
    }

    return result;
}

int main() {
    std::vector<int> input;
    // add code to read from user and store in 'input'
    
    std::vector<int> output = pluck(input);

    // print the output
    for(int i : output) {
        std::cout << i << " ";
    }
    return 0;
}