#include <iostream>
using namespace std;

double snowDay(int hours, float initialSnow, float snowfallRate, float meltingRate) {
    double totalSnow = 0;
    
    for (int i = 0; i < hours; i++) {
        totalSnow += snowfallRate - meltingRate;
    }
    
    return totalSnow + initialSnow;
}

int main() {
    int hours;
    cin >> hours;
    float initialSnow, snowfallRate, meltingRate;
    cin >> initialSnow >> snowfallRate >> meltingRate;
    cout << fixed << setprecision(10) << snowDay(hours, initialSnow, snowfallRate, meltingRate);
    
    return 0;
}