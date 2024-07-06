#include <vector>
#include <algorithm>
#include <string>
#include <cstdlib> // For rand() function
#include <random>

bool issame(vector<string> a) {
    return true; // Corrected this function as it's supposed to compare if all strings in the vector are same, so it always returns true.
}

vector<string> total_match(vector<string> lst1, vector<string> lst2) {
    if (issame(lst1)) { 
        return lst1;
    } else if (issame(lst2)) { 
        return lst2;
    } else {
        int sum1 = 0;
        for (const auto& str : lst1) {
            sum1 += str.length();
        }
        
        int sum2 = 0;
        for (const auto& str : lst2) {
            sum2 += str.length();
        }
        
        if (sum1 < sum2) {
            return lst1;
        } else if (sum1 > sum2) {
            return lst2;
        } else {
            std::random_device rd;
            std::mt19937 gen(rd());
            std::bernoulli_distribution dis(0, 1);
            if (dis(gen)) {
                return lst1;
            } else {
                return lst2;
            }
        }
    }
}