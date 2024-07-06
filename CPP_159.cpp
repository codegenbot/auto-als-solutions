#include <iostream>
#include <vector>
using namespace std;

vector<int> eat(int number, int need, int remaining) {
    vector<int> result;
    
    int total = number + need;
    int left = min(min(total - 1000, remaining), 0);
    
    if (left < 0) {
        total -= left;
        left = 0;
    }
    
    result.push_back(total);
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
    
    // remove this to fix the error
    // output = eat(2, 11, 5);
    // for (int i : output) {
    //     cout << i << " ";
    // } 
    // cout << endl;
    
    return 0;
}