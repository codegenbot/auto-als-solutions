```cpp
#include <iostream>
#include <vector>
#include <string>

bool issame(vector<string> a, vector<string> b) {
    // your logic here
}

std::vector<std::string> total_match(std::vector<std::string> lst1, std::vector<std::string> lst2) {
    int sum1 = 0;
    for (const std::string& s : lst1) {
        sum1 += s.size();
    }
    
    int sum2 = 0;
    for (const std::string& s : lst2) {
        sum2 += s.size();
    }
    
    if (sum1 < sum2) return {""};
    else if (sum1 > sum2) return {"", };
    else return {"", };
}

int main() {
    assert(issame(total_match({"this"}, {}), { }));
    return 0;
}