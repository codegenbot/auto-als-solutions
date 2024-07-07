#include <vector>
#include <iostream>
using namespace std;

double calculateEuclideanDistance(const vector<float>& vec1, const vector<float>& vec2) {
    double distance = 0;
    for (int i = 0; i < vec1.size(); i++) {
        distance += pow(vec1[i] - vec2[i], 2);
    }
    return sqrt(distance);
}

int main() {
    int n;
    cin >> n;

    vector<float> v1(n);
    for (float& x : v1) {
        cin >> x;
    }

    vector<float> v2(n);
    for (float& x : v2) {
        cin >> x;
    }

    double distance = calculateEuclideanDistance(v1, v2);

    cout.setprecision(10); // to avoid precision loss
    cout << fixed << distance << endl;

    return 0;
}