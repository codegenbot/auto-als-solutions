int main() {
    int hours;
    float initial_snow, snow_rate, melt_rate;
    cin >> hours >> initial_snow >> snow_rate >> melt_rate;

    float snow = initial_snow;
    for (int i = 0; i < hours; ++i) {
        snow += snow_rate;
        snow -= snow * melt_rate;
    }

    cout << snow << endl;
    return 0;
}