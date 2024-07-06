#include <vector>
#include <cmath> 
using namespace std;

vector<float> derivative(vector<float> xs) {
    vector<float> res;
    for (int i = 1; i <= xs.size(); i++) {
        if(i < xs.size()) { // check if index is within bounds
            res.push_back(xs[i-1] - xs[i]);
        }
    }
    return res;
}