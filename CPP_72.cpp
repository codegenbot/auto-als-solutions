#include <algorithm>
#include <string>
#include <vector>

bool will_it_fly(vector<int> q, int w);

int main() {
    assert(will_it_fly({5}, 5) == true);
    bool willItFly = will_it_fly({1,2,3,4,5}, 10);
    cout << "Will it fly? " << (willItFly ? "Yes" : "No") << endl;
}

bool will_it_fly(vector<int> q, int w) {
    string s = "";
    for (int i : q) {
        s += to_string(i);
    }
    if (s != reverse(s).str()) return false;
    int sum = 0;
    for (int i : q) {
        sum += i;
    }
    return sum <= w;
}