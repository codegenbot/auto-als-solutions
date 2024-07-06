#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> strange_sort_vector(vector<int> lst) {
    vector<int> result;
    if (lst.empty()) return result;

    sort(lst.begin(), lst.end());

    while (!lst.empty()) {
        result.push_back(*lst.begin());
        lst.erase(lst.begin());
        if (!lst.empty())
            reverse(lst.begin(), lst.end());
    }

    return result;
}

int main() {
    vector<int> v1 = {1, 2, 3, 4};
    vector<int> v2 = {5, 5, 5, 5};
    vector<int> v3;

    cout << "Vector: " << endl;
    for (int x : v1) {
        cout << x << " ";
    }
    cout << endl;

    vector<int> result1 = strange_sort_vector(v1);
    vector<int> result2 = strange_sort_vector(v2);
    vector<int> result3 = strange_sort_vector(v3);

    cout << "Strange sorted Vector: " << endl;
    for (int x : result1) {
        cout << x << " ";
    }
    cout << endl;

    cout << "Strange sorted Vector: " << endl;
    for (int x : result2) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}