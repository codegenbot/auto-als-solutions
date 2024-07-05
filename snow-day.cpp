#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int hours;
    double initial_snow, snow_rate, melt_rate;
    cin >> hours >> initial_snow >> snow_rate >> melt_rate;

    double snow = initial_snow;
    for (int i = 0; i < hours; ++i) {
        snow += snow_rate;
        snow -= snow * melt_rate;
        if (snow < 0) snow = 0; // Ensure snow is not negative
    }

    cout << fixed << setprecision(16) << snow << endl;
    return 0;
}