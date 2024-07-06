#include <vector>
#include <algorithm>
using namespace std;

vector<int> common(vector<int> l1, vector<int> l2) {
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());

    set<int> resultIntersection;
    if (s1.size() > s2.size()) {
        cout << "Error: The first list is larger than the second." << endl;
    }
    else if (s2.size() > s1.size()) {
        cout << "Error: The second list is larger than the first." << endl;
    }
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                      inserter(resultIntersection, resultIntersection.begin()));

    vector<int> result(resultIntersection.begin(), resultIntersection.end());
    return result;
}