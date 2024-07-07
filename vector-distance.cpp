#include <vector>
#include <iostream>

using namespace std;

double calculateEuclideanDistance(vector<double> vector1, vector<double> vector2) {
    double distance = 0;
    for (int i = 0; i < vector1.size(); i++) {
        distance += pow((vector1[i] - vector2[i]), 2);
    }
    return sqrt(distance);
}

int main() {
    int n;
    cin >> n;

    vector<double> vector1(n);
    for (double &val : vector1) {
        cin >> val;
    }

    vector<double> vector2(n);
    for (double &val : vector2) {
        cin >> val;
    }

    double distance = calculateEuclideanDistance(vector1, vector2);

    cout << fixed << setprecision(10) << distance << endl;

    return 0;
}