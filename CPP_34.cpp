#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> unique(vector<int> l){
    l.erase(unique(l.begin(), l.end()), l.end());
    return l;
}

int main(){
    vector<int> v = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> res = unique(v);
    for(int i:res){
        cout << i << " ";
    }
    return 0;
}