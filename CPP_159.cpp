#include <iostream>
#include <vector>
using namespace std;

vector<int> eat(int number, int need, int remaining) {
    int total = number + need;
    int left = min(total - 1000, remaining);
    if (left < 0) {
        return {total, 0};
    } else {
        return {total, max(0, remaining - need)};
    }
}