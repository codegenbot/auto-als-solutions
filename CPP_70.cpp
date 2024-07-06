int main() {
    int n, m;
    cout << "Enter the size of list: ";
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cout << "Enter number " << i+1 << ": ";
        cin >> a[i];
    }
    vector<int> result = strange_sort_list(a);
    if (!issame(a, result)) {
        cout << "The list is not sorted." << endl;
    } else {
        cout << "The list is sorted." << endl;
    }
    return 0;
}