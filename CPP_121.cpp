int main() {
    vector<int> lst;
    int sum = 0;
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        cout << "Enter element " << i + 1 << ": ";
        cin >> lst.push_back(i);
    }
    
    for (int i = 0; i < lst.size(); i++) {
        if ((i % 2 == 0 && lst[i] % 2 != 0)) {
            sum += lst[i];
        }
    }
    
    cout << "The sum of odd elements at even positions is: " << sum;
    return 0;
}