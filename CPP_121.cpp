int main() {
    vector<int> lst;
    int input;
    
    while (true) {
        cout << "Enter a number (-1 to finish): ";
        cin >> input;
        
        if (input == -1) break;
        
        lst.push_back(input);
    }
    
    int result = solution(lst);
    
    cout << "Sum: " << result << endl;
    
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