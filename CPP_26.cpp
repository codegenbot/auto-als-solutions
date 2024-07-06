#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> remove_duplicates(vector<int> numbers) {
    vector<int> result;
    for (int number : numbers) {
        if (find(result.begin(), result.end(), number) == result.end()) {
            result.push_back(number);
        }
    }
    return result;
}

int main() {
    vector<int> numbers = {1, 2, 3, 2, 4};
    vector<int> result = remove_duplicates(numbers);
    for (int number : result) {
        cout << number << " ";
    }
    cout << endl;
    return 0;
}