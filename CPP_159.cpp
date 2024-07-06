#include <iostream>
#include <vector>
using namespace std;

vector<int> eat(double number, double need, double remaining) {
    vector<int> result;
    
    int total = (int)(number + need);
    int left = min((int)((total - 1000)), (int)(remaining));
    
    if ((int)(total - left) < 0) {
        total -= left;
        left = 0;
    }
    
    result.push_back(total);
    result.push_back(left);
    
    return result;
}

int main() {
    vector<int> output;
    
    output = eat(5.0, 6.0, 10.0);
    for (int i : output) {
        cout << i << " ";
    }
    cout << endl;
    
    output = eat(4.0, 8.0, 9.0);
    for (int i : output) {
        cout << i << " ";
    }
    cout << endl;
    
    output = eat(1.0, 10.0, 10.0);
    for (int i : output) {
        cout << i << " ";
    }
    cout << endl;
    
    output = eat(2.0, 11.0, 5.0);
    for (int i : output) {
        cout << i << " ";
    }
    cout << endl;
    
    return 0;
}