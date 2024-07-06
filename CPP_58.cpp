#include <vector>
using namespace std;

vector<int> findCommon(vector<int>a,vector<int>b){
    vector<int> result;
    for(int i=0; i<min(a.size(),b.size());i++){
        if(a[i] == b[i])result.push_back(a[i]);
    }
    return result;
}

int main(){
    assert(issame(findCommon({4, 3, 2, 8}, {}),{}));
}