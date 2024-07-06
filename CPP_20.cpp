#include <vector>

bool issame(float* a, int la, float* b, int lb) {
    for(int i = 0; i < la || i < lb; i++) {
        if(i < la && i < lb && (a[i] != b[i])) return false;
    }
    return true;
}