#include <vector>
#include <cmath>

long long double_the_difference(std::vector<float> lst) {
    long long sum = 0;
    for(float n : lst){
        if(int(n) > 0 && int(n) % 2 != 0){ 
            sum += pow(int(n), 2); 
        }
    }
    return sum;
}

int main() {
    std::vector<float> lst; // Declare the vector
    float odd_sum = double_the_difference(lst);
    return 0;
}