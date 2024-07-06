#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int max_of_abs(vector<int> l) {
    return *max_element(abs(l.begin(), abs(l.end()));
}