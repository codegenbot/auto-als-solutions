#include <algorithm>

vector<float> sort_even(vector<float> l) {
    vector<float> result(l.size());
    
    for (int i = 0; i < l.size(); i++) {
        if (i % 2 == 0) {
            // Sort even indices
            vector<float> temp;
            int j = 0;
            for (int k = 0; k < l.size(); k++) {
                if (k % 2 == 0) {
                    temp.push_back(l[k]);
                }
            }
            sort(temp.begin(), temp.end());
            
            // Assign sorted values to even indices in result
            j = 0;
            for (int k = 0; k < l.size(); k++) {
                if (k % 2 == 0) {
                    result[k] = temp[j];
                    j++;
                } else {
                    result[k] = l[k];
                }
            }
        } else {
            // Leave odd indices as they are
            result[i] = l[i];
        }
    }
    
    return result;
}