Here is the solution:

int fuelCost(vector<int> &fuel) {
    int sum = 0;
    for (int i : fuel) {
        if (i >= 3) {
            sum += (i / 3 - 2);
        }
    }
    return sum;
}

int main() {
    vector<int> input;
    int num;
    
    cout << "Enter the number of inputs: ";
    cin >> num;
    
    for(int i = 0; i < num; ++i) {
        cout << "Enter a positive integer: ";
        cin >> input.push_back(num);
    }
    
    cout << "The fuel cost is: " << fuelCost(input) << endl;
    
    return 0;
}