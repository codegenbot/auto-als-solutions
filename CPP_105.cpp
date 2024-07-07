vector<string> by_length(vector<int> arr) {
    vector<int> tempArr;
    for (int num : arr) {
        if (num >= 1 && num <= 9) {
            tempArr.push_back(num);
        }
    }

    sort(tempArr.begin(), tempArr.end());
    reverse(tempArr.begin(), tempArr.end());

    vector<string> result;
    for (int num : tempArr) {
        string str = "";
        switch (num) {
            case 1:
                str = "One";
                break;
            case 2:
                str = "Two";
                break;
            case 3:
                str = "Three";
                break;
            case 4:
                str = "Four";
                break;
            case 5:
                str = "Five";
                break;
            case 6:
                str = "Six";
                break;
            case 7:
                str = "Seven";
                break;
            case 8:
                str = "Eight";
                break;
            case 9:
                str = "Nine";
                break;
        }
        result.push_back(str);
    }

    return result;
}