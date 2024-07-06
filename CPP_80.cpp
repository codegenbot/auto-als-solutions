int main(){
    string s;
    cout << "Enter a string: ";
    getline(cin, s);
    if(is_happy(s))
        cout << "The given string is happy." << endl;
    else
        cout << "The given string is not happy." << endl;
    return 0;
}