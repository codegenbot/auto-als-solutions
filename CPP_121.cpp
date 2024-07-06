int main() {
    vector<int> lst;
    int n; 
    cout << "Enter the number of elements: ";
    cin >> n;
    for(int i = 0; i < n; i++) {
        int num;
        cout << "Enter element "<<i+1<<":";
        cin >> num;
        lst.push_back(num);
    }
    int result = solution(lst);
    return 0;
}