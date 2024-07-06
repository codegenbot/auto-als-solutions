int main 
{
    string s;
    cout << "Enter a string: ";
    getline(cin, s);
    if(s.empty()) 
    {
        cerr << "Error: No input entered." << endl;
        return 1;
    }
    if(!is_happy(s)) 
    {
        cerr << "Warning: The given string is not happy. Try again!" << endl;
    } 
    else 
    {
        cout << "The given string is happy." << endl;
    }
    return 0;
}