```
#include <vector>

bool issame(vector<float> a, vector<float> b){
    if(a.size() != b.size())
        return false;
    for(int i = 0; i<a.size(); i++)
        if(abs(a[i] - b[i]) > 1e-9)
            return false;
    return true;
}

vector<float> get_positive(vector<float> l) {
    vector<float> result;
    for (float x : l) {
        if (x > 0)
            result.push_back(x);
    }
    return result;

}

int main() {
    assert(issame(get_positive({}), {}));
    vector<float> a = {1.5, -2.4, 3.9};
    vector<float> b = {-1.6, -0.7, -3.8};
    
    if (issame(a,b)) {
        cout << "same" << endl;
    } else {
        cout << "not same" << endl;
    }
    
    a = get_positive(a);
    b = get_positive(b);

    if (issame(a,b)) {
        cout << "same" << endl;
    } else {
        cout << "not same" << endl;
    }

    return 0;
}