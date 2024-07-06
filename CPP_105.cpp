#include <vector>
#include <algorithm>
#include <initializer_list>
using namespace std;

bool issame(vector<string> v1, vector<string> v2) {
    if(v1.size() != v2.size())
        return false;
    for(int i = 0; i < v1.size(); i++)
        if(v1[i] != v2[i])
            return false;
    return true;
}

vector<string> by_length(vector<int> arr) {
    vector<pair<int, int>> temp;
    for (int i : arr) {
        if (i >= 1 && i <= 9) {
            temp.push_back({(i == 1)? 1 : ((i == 2)? 2 : ((i == 3)? 3 : ((i == 4)? 4 : ((i == 5)? 5 : ((i == 6)? 6 : ((i == 7)? 7 : ((i == 8)? 8 : 9)))))))))), i});
        }
    }

    sort(temp.begin(), temp.end());
    reverse(temp.begin(), temp.end());

    vector<string> result;
    for (auto& t : temp) {
        switch(t.first) {
            case 1:
                result.push_back("One");
                break;
            case 2:
                result.push_back("Two");
                break;
            case 3:
                result.push_back("Three");
                break;
            case 4:
                result.push_back("Four");
                break;
            case 5:
                result.push_back("Five");
                break;
            case 6:
                result.push_back("Six");
                break;
            case 7:
                result.push_back("Seven");
                break;
            case 8:
                result.push_back("Eight");
                break;
            case 9:
                result.push_back("Nine");
                break;
        }
    }

    return result;
}

int main() {
    vector<int> arr = {9, 4, 8};
    vector<string> result = by_length(arr);
    if (!issame({"One"}, {"Four", "Eight"}, {result})) {
        return 1; 
    }
    return 0;
}