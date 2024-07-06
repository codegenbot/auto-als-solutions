int main { 
    string input;
    cout << "Enter a string: ";
    getline(cin, input); 
    if(input.empty()){
        cout << "Error! Please enter a valid input." << endl;
    } else {
        string output = solve(input);
        cout << "Output: " << output << endl;
    }
    return 0;
}