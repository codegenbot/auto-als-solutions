#include <vector>
#include <algorithm>
#include <string>
#include <random>

bool issame(vector<string>, vector<string>);
vector<string> total_match(vector<string>, vector<string>);

bool issame(vector<string> a, vector<string> b) {
    return a == b;
}

vector<string> total_match(vector<string> lst1, vector<string> b) {
    if (issame(lst1, b)) {
        return lst1;
    } else {
        int sum1 = 0;
        for (const auto& str : lst1) {
            sum1 += str.length();
        }
        
        int sum2 = 0;
        for (const auto& str : b) {
            sum2 += str.length();
        }
        
        if (sum1 < sum2) {
            return lst1;
        } else if (sum1 > sum2) {
            return b;
        } else {
            std::random_device rd;
            std::mt19937 gen(rd());
            std::uniform_int_distribution<> dis(0, 1);
            
            if (dis(gen)) {
                return lst1;
            } else {
                return b;
            }
        }
    }
}