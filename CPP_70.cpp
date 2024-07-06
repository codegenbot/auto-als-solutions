#include <vector>
#include <algorithm>
using namespace std;

bool issame(vector<int> a,vector<int>b){
    if(a.size() != b.size()) return false;
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    for(int i = 0; i < a.size(); i++){
        if(a[i] != b[i]) return false;
    }
    return true;

vector<int> strange_sort_list(vector<int> lst) {
    vector<int> result;
    while (!lst.empty()) {
        int min_val = *min_element(lst.begin(), lst.end());
        result.push_back(min_val);
        lst.erase(remove(lst.begin(), lst.end(), min_val), lst.end());
        if (!lst.empty()) {
            vector<int> temp;
            for(int i : lst){
                if(i == *max_element(lst.begin(), lst.end())){
                    temp.push_back(i);
                    break;
                }
            }
            for(int x:temp){
                lst.erase(remove(lst.begin(), lst.end(), x), lst.end());
            }
            result.push_back(*max_element(lst.begin(), lst.end()));
        }
    }
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> lst;
    for(int i=0; i<n; i++){
        int val;
        cin >> val;
        lst.push_back(val);
    }
    vector<int> sorted_lst = strange_sort_list(lst);
    if(issame(sorted_lst, lst)) cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}