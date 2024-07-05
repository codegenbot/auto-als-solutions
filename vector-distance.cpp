#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<float> vec1(n), vec2(n);
    for (int i = 0; i < n; ++i) cin >> vec1[i];
    for (int i = 0; i < n; ++i) cin >> vec2[i];
    
    float sum = 0.0;
    for (int i = 0; i < n; ++i) {
        float diff = vec1[i] - vec2[i];
        sum += diff * diff;
    }
    
    cout << sqrt(sum) << endl;
    return 0;
}