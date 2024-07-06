#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> unique(vector<int> l) {
    vector<int> result(l.begin(), unique(l.begin(), l.end()).end());
    sort(result.begin(), result.end());
    result.erase(unique(result.begin(), result.end()), result.end());
    return result;
}

int main() {
    vector<int> numbers = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> uniqueNumbers = unique(numbers);
    for (int number : uniqueNumbers) {
        cout << number << " ";
    }
    return 0;
}