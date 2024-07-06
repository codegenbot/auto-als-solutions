#include <vector>
#include <algorithm>
using namespace std;

bool compare(const pair<int,int> &a,const pair<int,int> &b){
    vector<int> v1({a.second,a.first});
    vector<int> v2({b.second,b.first});
    return issame(v1,v2);
}

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
            result.push_back(*max_element(lst.end()-1, lst.begin()));
        }
    }
    return result;
}