#include <iostream>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

vector<int> common(vector<int> a, vector<int> b){
    vector<int> result;
    for(int i=0; i<a.size();i++){
        if(find(b.begin(),b.end(),a[i])!=b.end())result.push_back(a[i]);
    }
    return result;
}

bool issame(vector<int> a, vector<int> b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i < a.size(); i++)
        if (find(b.begin(), b.end(), a[i]) == b.end())
            return false;
    return true;
}

int main(){
    vector<int> a, b;
    int n1,n2;

    cout << "Enter size of first array: ";
    cin >> n1;
    for(int i=0; i<n1;i++){
        cout << "Enter element: ";
        cin >> a[i];
    }

    cout << "Enter size of second array: ";
    cin >> n2;
    for(int i=0; i<n2;i++){
        cout << "Enter element: ";
        cin >> b[i];
    }
    
    if(issame(a, b))
        cout << "Both arrays are same." << endl;
    else{
        vector<int> res = common(a,b);
        if(res.size() > 0)
            cout << "Common elements in the two arrays are: ";
        for(int i=0; i<res.size();i++){
            cout << res[i] << " ";
        }
        cout << endl;
        else
            cout << "No common elements." << endl;
    }

    return 0;
}