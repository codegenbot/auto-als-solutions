```cpp
#include <vector>
using namespace std;

double find_zero(vector<double> xs){
    double a = 0, b = 0;
    for (int i = 0; i < xs.size(); i++) {
        if(i % 2 == 1) a += xs[i];
        else b += xs[i];
    }
    return -b / a;
}