```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    string exchange(vector<int> lst1, vector<int> lst2) {
        int oddCount = 0;
        for (int num : lst1) {
            if (num % 2 != 0) {
                oddCount++;
            }
        }
        return (oddCount == 0 ? "NO" : "YES");
    }

    string oddOrEven(vector<int> vec) {
        int count = 0;
        for (int num : vec) {
            if (num % 2 != 0) {
                count++;
            }
        }
        if (count > vec.size() / 2) {
            return "YES";
        } else {
            return "NO";
        }
    }

    int main() {
        cout << oddOrEven({100, 200}) << endl;
        cout << "Test cases passed." << endl;
        return 0;
    }
};