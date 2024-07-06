#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> total_match(vector<string> lst1, vector<string> lst2) {
    vector<string> result;
    
    if (lst1.empty()) {
        return min(lst2, [](const string& s1, const string& s2) { 
            return count(s1.begin(), s1.end(), '\0') < count(s2.begin(), s2.end(), '\0');
        }, lst2);
    } else if (lst2.empty()) {
        return max(lst1, [](const string& s1, const string& s2) { 
            return count(s1.begin(), s1.end(), '\0') < count(s2.begin(), s2.end(), '\0');
        }, lst1);
    }
    
    int sum1 = 0, sum2 = 0;
    for (const auto& str : lst1) {
        sum1 += str.size();
    }
    for (const auto& str : lst2) {
        sum2 += str.size();
    }
    
    if (sum1 < sum2) {
        return lst1;
    } else if (sum1 > sum2) {
        return lst2;
    } else {
        return lst1.empty() ? lst1 : lst2;
    }
}