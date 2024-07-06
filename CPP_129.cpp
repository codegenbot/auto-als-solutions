#include <vector>
#include <array>

using namespace std;

bool issame(vector<pair<int,int>>& a1, vector<pair<int,int>>& a2) {
    if (a1.size() != a2.size()) return false;
    for (int i = 0; i < a1.size(); i++) {
        if (issame(a1[i].first, a1[i].second, a2[i].first, a2[i].second)) return false;
    }
    return true;
}

bool issame(int a1, int b1, int a2, int b2) {
    if ((a1 == a2 && b1 == b2)) return true;
    return false;
}