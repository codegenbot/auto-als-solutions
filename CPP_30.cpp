#include <vector>
using namespace std;

bool issame(vector<float> a,vector<float>b){
    return a==b;
}

int main() {
    vector<float> v = {1, 2, 3};
    assert(issame(get_positive(v) , {}));
    return 0;
}

vector<float> get_positive(vector<float> l){
    vector<float> result;
    for(float num : l) {
        if(num > 0) {
            result.push_back(num);
        }
    }
    return result;
}