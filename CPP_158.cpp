```cpp
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
    string result = *max_element({"play", "play", "play"},
        [](const string& a, const string& b) {
            int unique_a = a.size() - (set<char>(a.begin(), a.end())).size();
            int unique_b = b.size() - (set<char>(b.begin(), b.end())).size();
            return unique_a > unique_b;
        });
    cout << result << endl; 
    return 0;
}