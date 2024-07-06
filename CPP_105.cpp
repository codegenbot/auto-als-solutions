bool issame(vector<string> a, vector<string> b) {
    return a == b;
}

int main() {
    int b = 0;
    vector<int> arr;
    cout << "Enter the numbers (space separated): ";
    for (int i; cin >> i;) {
        arr.push_back(i);
        if (cin.peek() != ' ') {
            cin.ignore();
        } else {
            cin.ignore(1);
            if (i == b) {
                vector<string> result = by_length(arr);
                cout << "The numbers in descending order with their names are: ";
                for (int i = 0; i < result.size(); i++) {
                    cout << result[i] << " ";
                }
                cout << endl;
            } else {
                arr.clear();
                b++;
            }
        }
    }
    return 0;
}

vector<string> by_length(vector<int> arr) {
    vector<int> numbers;
    for (int num : arr) {
        if (num >= 1 && num <= 9) {
            numbers.push_back(num);
        }
    }

    sort(numbers.begin(), numbers.end());
    reverse(numbers.begin(), numbers.end());

    vector<string> result;
    for (int num : numbers) {
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