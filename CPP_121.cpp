int main() {
    vector<int> lst;
    cout << "Enter numbers (space separated): ";
    for(int i = 0; i < 5; ++i) {
        int num;
        cin >> num;
        lst.push_back(num);
    }
    int result = solution(lst);
    cout << "The sum of all even elements is: " << result << endl;
    return 0;
}