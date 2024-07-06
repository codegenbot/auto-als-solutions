#include <vector>
#include <string>

bool issame(std::vector<std::string> a, std::vector<std::string> b) {
    if(a.size() != b.size()) {
        return false;
    }
    for(int i = 0; i < a.size(); i++) {
        if(a[i] != b[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    std::cin >> n;
    
    std::vector<std::string> vec1, vec2;
    for(int i = 0; i < n; i++) {
        std::string str;
        std::cin >> str;
        vec1.push_back(str);
    }
    
    for(int i = 0; i < n; i++) {
        std::string str;
        std::cin >> str;
        vec2.push_back(str);
    }
    
    if(issame(vec1, vec2)) {
        std::cout << "Vectors are the same." << std::endl;
    } else {
        std::cout << "Vectors are not the same." << std::endl;
    }
    
    return 0;