#include <vector>
#include <algorithm>

double findClosestElements(vector<float> a) {
    double minDist = numeric_limits<double>::max();
    for (int i = 0; i < a.size() - 1; i++) {
        double dist = a[i + 1] - a[i];
        if (dist < minDist)
            minDist = dist;
    }
    return minDist;
}

bool issame(vector<float> a, vector<float> b) {
    return (a.size() == b.size() && equal(a.begin(), a.end(), b.begin()));
}