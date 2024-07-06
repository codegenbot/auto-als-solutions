```
#include <iostream>
using namespace std;

class Solution {
public:
    int exchange(vector<int> lst1, vector<int> lst2) {
        int oddCount = 0;
        for (int num : lst1) {
            if (num % 2 != 0) {
                oddCount++;
            }
        }
        return oddCount == 0 ? 1 : 0;
    }

    int main() {
        cout << exchange({100, 200}, {200, 200}) << endl;
        return 0;
    }
};