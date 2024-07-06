string int_to_mini_roman(int number) {
    string roman[14] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII"};
    vector<string> thousands, hundreds, tens, ones;
    thousands.push_back("M");
    for (int i = 1; i <= 3; ++i) {
        hundreds.push_back("C" + string(i, 'D'));
        for (int j = 1; j <= 3; ++j) {
            tens.push_back("X" + string(j, 'X'));
            for (int k = 1; k <= 10; ++k)
                ones.push_back(roman[k] + (k == 9 ? "" : "X"));
        }
    }

    string result;
    int temp = number;

    while (temp >= 1000) {
        result += thousands[0];
        temp -= 1000;
    }

    for (int i = 12; i >= 1; --i) {
        if (temp >= int(stoi(hundreds[i])) + int(stoi(tens[i-1])) + int(stoi(ones[i-1])))
            result += hundreds[i] + ones[i - 1];
        else if (temp >= int(stoi(tens[i-1])) + int(stoi(ones[i-1])))
            result += tens[i-1] + ones[i-1];
        else
            result += ones[i-1];

        temp -= int(stoi(hundreds[i])) + int(stoi(tens[i-1])) + int(stoi(ones[i-1]));
    }

    return tolower(result);
}