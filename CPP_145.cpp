#include <vector>
#include <algorithm>
#include <functional>

bool issame(std::vector<int> a, std::vector<int> b) {
    if(a.size() != b.size()) {
        return false;
    }
    
    for(int i = 0; i < a.size(); i++) {
        long long sum1 = 0, sum2 = 0;
        while(a[i] > 0){
            sum1 += a[i] % 10;
            a[i] /= 10;
        }
        while(b[i] > 0){
            sum2 += b[i] % 10;
            b[i] /= 10;
        }
        if(sum1 != sum2) {
            return false;
        }
    }
    
    return true;
}

int main() {
    std::vector<int> order_by_points = {0,6,6,-76,-21,23,4};
    assert(issame(order_by_points, {-76, -21, 0, 4, 23, 6, 6}));
    return 0;
}