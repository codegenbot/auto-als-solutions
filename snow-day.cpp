#include <iostream>
using namespace std;

float snowDay(int hours, float initialSnow, float rate, float melt) {
    float snow = initialSnow;
    
    for (int i = 0; i < hours; i++) {
        snow += rate; // Add snowfall
        snow -= min(snow, snow * melt); // Melt snow
        
    }
    
    return snow;
}

int main() {
    int hours;
    float initialSnow, rate, melt;

    cin >> hours >> initialSnow >> rate >> melt;

    cout << fixed << setprecision(10) << snowDay(hours, initialSnow, rate, melt);

    return 0;
}