#include <vector>
using namespace std;

double calculateDistance(int n, vector<float> v1, vector<float> v2) {
    double distance = 0;
    for (int i = 0; i < n; i++) {
        float diff = v1[i] - v2[i];
        distance += diff * diff;
    }
    return sqrt(distance);
}

int main() {
    int n;
    cin >> n;
    
    vector<float> v1(n), v2(n);

    for (int i = 0; i < n; i++) {
        float val;
        cin >> val;
        v1[i] = v2[i] = val;
    }

    double dist = calculateDistance(n, v1, v2);
    
    cout << fixed << setprecision(10) << dist << endl;

    return 0;
}