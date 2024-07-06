#include <vector>
#include <string>

bool hasOdd(vector<int>& vec) {
    for (int num : vec) {
        if (num % 2 != 0)
            return true;
    }
    return false;
}

string exchange(vector<int> lst1, vector<int> lst2) {
    while (!hasOdd(lst1)) {
        bool found = false;
        for (int i = 0; i < lst2.size(); i++) {
            if (lst2[i] % 2 != 0) {
                swap(lst1.back(), lst2[i]);
                found = true;
                break;
            }
        }
        if (!found)
            return "NO";
    }
    return "YES";
}