#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> common(vector<int> a, vector<int> b){
    vector<int> result;
    for(auto x : a){
        if(std::find(b.begin(), b.end(), x) != b.end()) result.push_back(x);
    }
    return result;
}

int main(){
    vector<int> a; 
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    cout << "Enter the elements: ";
    for(int i=0; i<n; i++){
        int temp;
        cin >> temp;
        a.push_back(temp);
    }
    
    vector<int> b; 
    int m;
    cout << "Enter the number of elements: ";
    cin >> m;
    cout << "Enter the elements: ";
    for(int j=0; j<m; j++){
        int temp;
        cin >> temp;
        b.push_back(temp);
    }
    
    vector<int> result = common(a, b);
    for (auto x : result) {
        cout << x << " ";
    }
    cout << endl;
}