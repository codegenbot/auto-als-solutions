#include <vector>
#include <limits>

std::vector<int> findMinEvenIndex(std::vector<int> arr) {
    std::vector<int> result = {};
    int minEvenValueIndex = -1;
    int minEvenValue = std::numeric_limits<int>::max();

    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0 && arr[i] < minEvenValue){
            minEvenValue = arr[i];
            minEvenValueIndex = i;
        }
    }

    if(minEvenValue != std::numeric_limits<int>::max()){
        result.push_back(minEvenValue);
        result.push_back(minEvenValueIndex);
    }

    return result;
}