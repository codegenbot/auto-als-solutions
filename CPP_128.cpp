int prod_signs(std::vector<int> arr) {
    int sign_product = 1;
    long long sum_of_magnitudes = 0;

    for (int num : arr) {
        if (num == 0) {
            if (sign_product < 0) return 0; 
            else return -32768; 
        }
        sign_product *= ((num > 0) ? 1 : ((num < 0) ? -1 : 0));
        sum_of_magnitudes += std::abs(num);
    }

    return sign_product * static_cast<long long>(sum_of_magnitudes);
}