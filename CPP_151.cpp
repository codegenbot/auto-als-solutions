#include <cmath>
#include <vector>

int main() {
    std::vector<float> lst;
    float num;
    long long sum = 0;

    std::cout << "Enter numbers (enter 'stop' to finish):" << std::endl;
    while(std::cin >> num) {
        if(num > 0 && floor(num) == num) {
            sum += pow(num, 2);
        }
        if(std::string("stop") == num) break;
    }

    long long double_the_difference = sum;
    return 0;
}