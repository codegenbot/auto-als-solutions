```cpp
#include <vector>
using namespace std;

int luhn(vector<int> numbers) {
    int sum = 0;
    for(int i = 0; i < numbers.size(); i++) {
        if(i % 2 == 1) {
            numbers[i] *= 2;
            if(numbers[i] > 9) {
                numbers[i] -= 9;
            }
        }
        sum += numbers[i];
    }
    return sum;
}

int main() {
    vector<int> numbers = {4,3,7,1,3,5,8,6,7,9,2};
    int result = luhn(numbers);
    cout << "The Luhn check sum is: " << result << endl;
    return 0;
}