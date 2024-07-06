#include <vector>
#include <algorithm>
#include <string>
#include <random>

bool issame(std::vector<std::string> a, std::vector<std::string> b) {
    return a == b;
}

std::vector<std::string> total_match(std::vector<std::string> lst1, std::vector<std::string> lst2) {
    if (issame(lst1, lst2)) {
        return lst1;
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
            std::random_device rd;  // obtain a random number from hardware
            std::mt19937 eng(rd()); // seed the generator
 
            std::bernoulli_distribution dist(0.5); // probability of true

            if (dist(eng)) {
                return lst1;
            } else {
                return lst2;
            }
        }
    }
}