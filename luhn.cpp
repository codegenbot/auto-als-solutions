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
    vector<int> numbers = {4, 7, 8, 7, 1, 1, 6, 5, 3, 5, 0, 0, 9, 9, 8, 1};
    cout << "The result is: " << luhn(numbers) << endl;
    return 0;
}