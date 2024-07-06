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
    // Add your code here
    std::vector<int> input;
    // Read input from user
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        int val;
        cin >> val;
        input.push_back(val);
    }
    
    vector<int> output = pluck(input);
    // Print the output
    cout << "Output: ";
    for(auto x : output) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}