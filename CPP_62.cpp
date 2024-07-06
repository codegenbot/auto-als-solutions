#include <vector>
#include <cmath> 
using namespace std;

vector<float> derivative(vector<float> xs) {
    vector<float> res;
    for (int i = 1; i < xs.size(); i++) {
        res.push_back((xs[i] - xs[0]) * (xs[i] > xs[0]));
    }
    return res;
}