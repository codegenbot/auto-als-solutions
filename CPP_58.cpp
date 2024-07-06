#include <vector>
#include <algorithm>
using namespace std;

vector<int> common(vector<int> l1, vector<int> l2) {
    set<int> s11(l1.begin(), l1.end()); 
    set<int> s22(l2.begin(), l2.end());

    set<int> intersection;
    set_intersection(s11.begin(), s11.end(), s22.begin(), s22.end(),
                      inserter(intersection, intersection.begin()));

    vector<int> result(intersection.begin(), intersection.end());
    return result;
}