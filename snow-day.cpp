#include <iostream>
using namespace std;

double snowDay(int hours, float initialSnow, float snowfallPerHour, float meltingRate) {
    double totalSnow = initialSnow;
    
    for (int i = 0; i < hours; i++) {
        totalSnow += snowfallPerHour - totalSnow * meltingRate;
    }
    
    return totalSnow;
}

int main() {
    int h;
    cin >> h;
    float s, sf, mr;
    cin >> s >> sf >> mr;
    cout << fixed << setprecision(10) << snowDay(h, s, sf, mr) << endl;
    return 0;
}