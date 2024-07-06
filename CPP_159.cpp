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