#include<vector>
#include<algorithm>
using namespace std;

vector<int> unique(vector<int> l){
    vector<int> result(l.begin(), l.end());
    sort(result.begin(), result.end());
    return result;
}