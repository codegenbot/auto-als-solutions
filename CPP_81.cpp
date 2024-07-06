#include <vector>
#include <string>

bool issame(std::vector<std::string> a, std::vector<std::string> b) {
    if(a.size()!=b.size())return false;
    for(int i=0;i<a.size();i++)if(a[i]!=b[i])return false;
    return true;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<std::string> v1(n);
    std::vector<std::string> v2(n);

    for (int i = 0; i < n; ++i) {
        std::cin >> v1[i] >> v2[i];
    }

    bool result = issame(v1, v2);

    return result;
}