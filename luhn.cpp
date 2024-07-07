#include <vector>
using namespace std;

int luhn(vector<int> numbers) {
    int sum = 0;
    for(int i = 0; i < numbers.size(); i++) {
        if(i % 2 == 1) {
            int temp = numbers[i] * 2;
            if(temp > 9) {
                temp -= 9;
            }
            sum += temp;
        } else {
            sum += numbers[i];
        }
    }
    return sum;
}

int main() {
    vector<int> numbers = {4,7,8,7,1,1,6,5,9,2,9,8,0,9,1,4};
    cout << "The result is: " << luhn(numbers) << endl;
    return 0;
}