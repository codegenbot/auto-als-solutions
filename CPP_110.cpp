```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    void exchange(vector<int> lst1, vector<int> lst2) {
        int oddCount = 0;
        for (int num : lst1) {
            if (num % 2 != 0) {
                oddCount++;
            }
        }
        bool result = oddCount == 0;
        cout << (result ? "YES" : "NO") << endl;
    }

    int main() {
        exchange({100, 200}, {200, 200});
        return 0;
    }
};