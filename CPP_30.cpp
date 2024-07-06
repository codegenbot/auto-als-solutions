#include <vector>
#include <iostream>

using namespace std;

bool issame(float f1, float f2) {
    if(abs(f1 - f2) <= 0.00001)
        return true;
    else
        return false;
}

vector<float> get_positive(vector<float> l){
    vector<float> result;
    for(float i : l) {
        if(i > 0) {
            result.push_back(i);
        }
    }
    return result;
}