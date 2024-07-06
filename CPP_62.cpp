#include <vector>
#include <cmath> 
using namespace std;

vector<float> derivative(vector<float> xs) {
    vector<float> res;
    for (int i = 1; i < xs.size(); i++) {
        res.push_back((xs[i] - xs[i-1]) / abs(xs[i] - xs[i-1]));
    }
    return res;
}