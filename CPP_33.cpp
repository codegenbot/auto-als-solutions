#include <vector>
#include <algorithm>

using namespace std;

vector<int> sort_third(vector<int> l) {
    vector<int> result;
    
    for (int i = 0; i < l.size(); i++) {
        if (i % 3 == 0) {
            for (int j = 0; j < l[i]; j++) {
                result.push_back(l[i]);
            }
        } else {
            result.push_back(l[i]);
        }
    }
    
    return result;
}