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
    vector<int> output;

    int numCases; 
    cin >> numCases; 

    for(int i=0;i<numCases;++i) {
        int number, need, remaining; 
        cin >> number >> need >> remaining; 
        output = eat(number, need, remaining);
        for (int i : output) {
            cout << i << " ";
        }
        cout << endl;
    }

    return 0;
}