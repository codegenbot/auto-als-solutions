#include <iostream>
using namespace std;

double snowDay(int hours, float initialSnow, float rateOfFall, float meltingRate) {
    double totalSnow = 0;
    for (int i = 0; i < hours; i++) {
        totalSnow += rateOfFall - meltingRate * initialSnow > 0 ? rateOfFall : 0;
        initialSnow = max(initialSnow + rateOfFall - meltingRate * initialSnow, 0);
    }
    return initialSnow;
}

int main() {
    int hours;
    float initialSnow, rateOfFall, meltingRate;

    cin >> hours >> initialSnow >> rateOfFall >> meltingRate;

    cout << fixed << setprecision(10) << snowDay(hours, initialSnow, rateOfFall, meltingRate);

    return 0;
}