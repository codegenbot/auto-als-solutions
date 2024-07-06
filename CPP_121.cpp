int main() {
    vector<int> lst;
    int result = 0;
    cout << "Enter the elements of the list (space-separated): ";
    for (string s; cin >> s) {
        lst.push_back(stoi(s));
    }
    result = solution(lst);
    cout << "The sum is: " << result << endl;
    return 0;
}