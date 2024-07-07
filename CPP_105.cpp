#include <vector>
#include <string>

bool issame(vector<string> a, vector<string> b) {
    if (a.size() != b.size()) return false;
    for (int i = 0; i < a.size(); ++i)
        if (a[i] != b[i]) return false;
    return true;
}

vector<string> by_length(vector<int> arr) {
    vector<vector<string>> result;
    for (int i : arr) {
        if (i >= 1 && i <= 9) {
            string s = "";
            switch (i) {
                case 1: s = "One"; break;
                case 2: s = "Two"; break;
                case 3: s = "Three"; break;
                case 4: s = "Four"; break;
                case 5: s = "Five"; break;
                case 6: s = "Six"; break;
                case 7: s = "Seven"; break;
                case 8: s = "Eight"; break;
                case 9: s = "Nine"; break;
            }
            vector<string> temp({s});
            result.push_back(temp);
        }
    }
    return result;
}

int main() {
    assert(issame(by_length({9, 4, 8}), {{"Nine"}, {"Four"}, {"Eight"}}));
    return 0;
}