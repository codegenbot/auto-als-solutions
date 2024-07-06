int solutions(vector<int> lst) {
    int sum = 0;
    for (int i = 1; i < lst.size(); i += 2) {
        if (lst[i] % 2 != 0) {
            sum += lst[i];
        }
    }
    return sum;

}

int main() {
    assert(solutions({3, 13, 2, 9}) == 3);
    
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    
    vector<int> lst(n);
    for (int i = 0; i < n; i++) {
        cout << "Element "<<i+1<<":";
        cin >> lst[i];
    }
    
    int result = solutions(lst);
    cout << "\nThe sum of all the odd elements is: " << result << endl;
    
}