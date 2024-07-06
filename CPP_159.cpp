#include <iostream>
#include <vector>
using namespace std;

vector<int> eat(int number, int need, int remaining) {
    vector<int> result;
    
    int total = number + need;
    int left = min(total - 1000, remaining);
    
    if (left < 0) {
        total -= left;
        left = 0;
    }
    
    result.push_back(total);
    result.push_back(left);
    
    return result;
}

int main() {
    cout << "Eating..." << endl;
    vector<int> output1 = eat(5, 6, 10);
    for (int i : output1) {
        cout << i << " ";
    }
    cout << endl;
    
    cout << "Eating..." << endl;
    vector<int> output2 = eat(4, 8, 9);
    for (int i : output2) {
        cout << i << " ";
    }
    cout << endl;
    
    cout << "Eating..." << endl;
    vector<int> output3 = eat(1, 10, 10);
    for (int i : output3) {
        cout << i << " ";
    }
    cout << endl;
    
    cout << "Eating..." << endl;
    vector<int> output4 = eat(2, 11, 5);
    for (int i : output4) {
        cout << i << " ";
    }
    cout << endl;
    
    return 0;
}