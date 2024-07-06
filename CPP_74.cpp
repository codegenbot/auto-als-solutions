#include <vector>
#include <string>
using namespace std;

vector<string> total_match(vector<string> lst1, vector<string> lst2) {
    vector<string> result;
    int count1 = 0, count2 = 0;

    for (const auto& s : lst1) {
        count1 += s.length();
    }
    for (const auto& s : lst2) {
        count2 += s.length();
    }

    if (count1 < count2) {
        return lst1;
    } else if (count1 > count2) {
        return lst2;
    } else {
        return lst1;
    }
}