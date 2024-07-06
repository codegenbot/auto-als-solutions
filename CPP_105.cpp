#include <vector>
#include <string>
using namespace std;

vector<string> by_length(vector<int> arr) {
    vector<int> result;
    for (int i : arr) {
        if (i >= 1 && i <= 9) {
            result.push_back(i);
        }
    }
    sort(result.begin(), result.end());
    reverse(result.begin(), result.end());
    vector<string> names = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    for (int i : result) {
        cout << i << endl;
        if (i >= 1 && i <= 9) {
            cout << names[i - 1] << endl;
        }
    }
    return vector<string>();
}