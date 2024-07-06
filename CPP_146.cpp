#include <vector>
#include <iostream>

int specialFilter(std::vector<int> nums){
    int count = 0;
    for(int num : nums){
        if(num > 10 && (num % 10) % 2 != 0 && (num / 10) % 10 % 2 != 0){
            count++;
        }
    }
    return count;
}

int main() {
    std::vector<int> input; 
    int number; 

    cout << "Enter the numbers of your choice. Type 'stop' to finish." << endl;

    while (true) {   
        cin >> number;

        if (number == 0) continue;

        if (std::string("stop") == std::to_string(number)) {
            break;
        }
        
        input.push_back(number);
    } 

    int result = specialFilter(input);
    cout << "The result is: " << result << endl; 
    return 0;
}