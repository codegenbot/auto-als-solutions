#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int hours;
    double initial_snow, snow_rate, melt_rate; // Use double for better precision
    cin >> hours >> initial_snow >> snow_rate >> melt_rate;

    double snow = initial_snow;
    for (int i = 0; i < hours; ++i) {
        snow += snow_rate;
        snow -= snow * melt_rate;
    }

    cout << fixed << setprecision(16) << snow << endl; // Ensure precision in output
    return 0;
}