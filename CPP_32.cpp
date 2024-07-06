```cpp
#include <vector>
using namespace std;

double find_zero(vector<double> xs){
    double a = xs[0], b = 0;
    for (int i = 1; i < xs.size(); i++) {
        if(i % 2 == 0) b += xs[i];
        else a -= xs[i];
    }
    return -b / a;
}