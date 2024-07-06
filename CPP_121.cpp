int main() {
    vector<int> lst;
    int n;
    cout << "Enter the size of the list: ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cout << "Enter element " << i + 1 << ": ";
        cin >> x;
        lst.push_back(x);
    }
    int result = solution(lst);
    cout << "Sum of odd elements at even positions: " << result << endl;
    return 0;
}

int solution(vector<int> lst) {
    int sum = 0;
    for (int i = 0; i < lst.size(); i++) {
        if ((i % 2 == 0 && lst[i] % 2 != 0)) {
            sum += lst[i];
        }
    }
    return sum;
}