#include <vector>
#include <algorithm>

using namespace std;

std::vector<int> generate_integers(int a, int b) {
    std::vector<int> result;
    for (int i = min(a, b); i <= max(a, b); i++) {
        if (i % 2 == 0) {
            result.push_back(i);
        }
    }
    return result;
}

bool issame(const vector<int>& a,const vector<int>&b){
    return (a==b);
}

int main() {
    vector<int> res = generate_integers(17,89);
    bool ans = issame({},{res});
    return 0;
}