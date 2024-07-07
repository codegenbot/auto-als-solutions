#include <iostream>
using namespace std;

float snowDay(int hours, float initialSnow, float rateOfFall, float proportionMeltingPerHour) {
    float totalSnow = initialSnow;
    for (int i = 0; i < hours; i++) {
        totalSnow += rateOfFall;
        totalSnow *= (1 - proportionMeltingPerHour);
    }
    return totalSnow;
}

int main() {
    int hours;
    cin >> hours;
    float initialSnow, rateOfFall, proportionMeltingPerHour;
    cin >> initialSnow >> rateOfFall >> proportionMeltingPerHour;
    cout << fixed << setprecision(10) << snowDay(hours, initialSnow, rateOfFall, proportionMeltingPerHour) << endl;
    return 0;
}