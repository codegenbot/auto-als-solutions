#include <algorithm>
using namespace std;

vector<float> sort_even(vector<float> l) {
    vector<float> result;
    for(int i = 0; i < l.size(); i++) {
        if(i % 2 == 0) {
            int j = i;
            while(j < l.size() && j+1 < l.size() && j % 2 == 0) {
                vector<float> evenVals(l.begin() + j, l.begin() + j+1);
                sort(evenVals.begin(), evenVals.end());
                result.push_back(evenVals[0]);
                j += 2;
            }
        } else {
            result.push_back(l[i]);
        }
    }
    return result;