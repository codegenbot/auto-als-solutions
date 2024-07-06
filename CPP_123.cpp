#include <vector>
#include <algorithm>

using namespace std;

vector<int> get_odd_collatz(int n) {
    vector<int> sequence;
    while (n != 1) {
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
        sequence.push_back(n);
    }
    sequence.push_back(1); // Add the final 1 to the sequence
    vector<int> odd_numbers;
    for (int num : sequence) {
        if (num % 2 != 0) {
            odd_numbers.push_back(num);
        }
    }
    sort(odd_numbers.begin(), odd_numbers.end());
    return odd_numbers;
}