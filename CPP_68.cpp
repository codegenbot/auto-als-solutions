```cpp
#include <vector>
#include <algorithm>

using namespace std;

struct pair {
    int first;
    int second;
};

bool compare(const pair& a, const pair& b) {
    if (a.first != b.first) return a.first < b.first;
    return a.second < b.second;
}

vector<int> pluck(vector<int> arr) {
    vector<pair> nodes;
    for (int i = 0; i < arr.size(); ++i) {
        if (arr[i] % 2 == 0) {
            nodes.push_back({arr[i], i});
        }
    }

    if (nodes.empty()) {
        return {};
    }

    sort(nodes.begin(), nodes.end(), compare);

    for (size_t i = 1; i < nodes.size(); ++i) {
        if (compare({nodes[i-1].first, nodes[i-1].second}, {nodes[i].first, nodes[i].second}) == false) {
            return {};
        }
    }

    int result = nodes[0].first;
    for(int i = 0; i < arr.size(); ++i){
        if(arr[i] == result){
            vector<int> output;
            output.push_back(result);
            return output;
        }
    }
}

int main() {
    vector<int> arr;
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    for (int i = 0; i < n; ++i) {
        int x;
        cout << "Enter element " << i+1 << ": ";
        cin >> x;
        arr.push_back(x);
    }
    vector<int> output = pluck(arr);
    if(output.size() > 0)
    {
        cout << "The output is: ";
        for(int i = 0; i < output.size(); ++i){
            cout << output[i] << " ";
        }
        cout << endl;
    }
    else
    {
        cout << "No output" << endl;
    }
    
    return 0;
}