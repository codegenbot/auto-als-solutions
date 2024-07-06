#include <vector>
#include <cassert>

using namespace std;

vector<int> common(vector<int> a,vector<int>b){
    vector<int> result;
    for(int i=0; i<a.size();i++){
        if(find(b.begin(),b.end(),a[i])!=b.end())result.push_back(a[i]);
    }
    return result;
}

int main() {
    assert(common({4, 3, 2, 8}, {}) == {});
    return 0;
}