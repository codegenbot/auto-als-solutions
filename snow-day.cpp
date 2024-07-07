#include <iostream>
using namespace std;

float calculateSnow(float hours, float initialSnow, float snowFall, float meltingRate) {
    return (initialSnow + snowFall * hours - meltingRate * hours);
}

int main() {
    int hours;
    cin >> hours;
    float initialSnow, snowFall, meltingRate;
    cin >> initialSnow >> snowFall >> meltingRate;

    cout << fixed << setprecision(10) << calculateSnow(hours, initialSnow, snowFall, meltingRate) << endl;

    return 0;
}