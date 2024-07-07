#include <iostream>
#include <vector>
using namespace std;

double vector_distance() {
    int n;
    cin >> n;

    vector<float> v1(n);
    for (int i = 0; i < n; ++i) {
        cin >> v1[i];
    }

    vector<float> v2(n);
    for (int i = 0; i < n; ++i) {
        cin >> v2[i];
    }

    double distance = 0.0;
    for (int i = 0; i < n; ++i) {
        distance += pow(v1[i] - v2[i], 2);
    }
    return sqrt(distance);
}

int main() {
    int n1, n2;
    cin >> n1 >> n2;

    if(n1 != n2) {
        cout << "Invalid input. Both vectors must have the same number of dimensions." << endl;
        return -1;
    }

    double dist = vector_distance();

    printf("%.10f\n", dist);

    return 0;
}