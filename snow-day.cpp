int main() {
    int hours;
    float initial_snow, snowfall_rate, melt_rate;
    cin >> hours >> initial_snow >> snowfall_rate >> melt_rate;

    float current_snow = initial_snow;

    for (int i = 0; i < hours; ++i) {
        current_snow += snowfall_rate;
        current_snow -= current_snow * melt_rate;
    }

    printf("%.13f\n", current_snow);
    return 0;
}