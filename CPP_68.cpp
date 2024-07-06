#include <iostream>
#include <vector>

std::vector<int> pluck(std::vector<int> arr) {
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
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;

    for(int i = 0; i < n; i++){
        int val;
        std::cout << "Enter element " << i+1 << ": ";
        std::cin >> val;
        input.push_back(val);
    }

    std::vector<int> output = pluck(input);

    if(output.size() > 0) {
        std::cout << "The minimum even value is: " << output[0] << "\n";
        std::cout << "The index of the minimum even value is: " << output[1] << "\n";
    } else {
        std::cout << "No even values found.\n";
    }

    return 0;
}