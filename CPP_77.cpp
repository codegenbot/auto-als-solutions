#include <cmath>
bool iscuber(int a){
    int c = round(pow(a, 1.0/3.0));
    return c*c*c == a;
}