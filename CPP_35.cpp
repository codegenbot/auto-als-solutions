#include <algorithm>
#include <cmath> // for abs()
#include <vector>

double maximumTemperature(vector<int> l) {
    return *max_element(l.begin(), l.end());
}