int main() {
    vector<int> lst;
    int result = solution(lst);
    cout << "Enter numbers separated by spaces: ";
    for (int i = 0; i < 5; i++) {
        int num;
        cin >> num;
        lst.push_back(num);
    }
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