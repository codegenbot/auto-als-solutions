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