#include <iostream>
using namespace std;

float snowDay(int hours, float initialSnow, float rateOfSnowFall, float proportionOfSnowMeltingPerHour) {
    float totalSnow = 0;
    
    for (int i = 0; i < hours; i++) {
        totalSnow += rateOfSnowFall - initialSnow * proportionOfSnowMeltingPerHour;
    }
    
    return totalSnow;
}

int main() {
    int hours;
    cout << "Enter the number of hours: ";
    cin >> hours;

    float initialSnow, rateOfSnowFall, proportionOfSnowMeltingPerHour;
    cout << "Enter the initial snow amount: ";
    cin >> initialSnow;
    
    cout << "Enter the rate of snow fall: ";
    cin >> rateOfSnowFall;
    
    cout << "Enter the proportion of snow melting per hour: ";
    cin >> proportionOfSnowMeltingPerHour;

    float totalSnow = snowDay(hours, initialSnow, rateOfSnowFall, proportionOfSnowMeltingPerHour);
    cout << fixed << setprecision(10) << totalSnow;
    
    return 0;
}