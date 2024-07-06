```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> eat(double number, double need, double remaining) {
    vector<int> result;
    
    double total = number + need;
    int left = (int)min(total - 1000, (double)remaining);
    
    if (left < 0) {
        total -= left;
        left = 0;
    }
    
    result.push_back((int)total);
    result.push_back(left);
    
    return result;
}

int main() {
    vector<int> output;
    
    output = eat(5, 6, 10);
    for (int i : output) {
        cout << i << " ";
    }
    cout << endl;
    
    output = eat(4, 8, 9);
    for (int i : output) {
        cout << i << " ";
    }
    cout << endl;
    
    output = eat(1, 10, 10);
    for (int i : output) {
        cout << i << " ";
    }
    cout << endl;
    
    output = eat(2, 11, 5);
    for (int i : output) {
        cout << i << " ";
    }
    cout << endl;
    
    return 0;
}