int search(const std::vector<int>& v) {
    for(int i = 1; i < v.size(); i++) {
        if(v[i] == v[0])
            return -1;
    }
    return -2;
}

int main() {
    vector<int> vec;
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    vec.resize(n);
    
    cout << "Enter the elements: ";
    for(int i = 0; i < n; i++)
        cin >> vec[i];
    
    assert(search(vec) == -2); 
    return 0;
}