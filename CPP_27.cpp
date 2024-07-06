int main(){
    int i = 0;
    std::string flip_case(std::string str){
        for(i = 0; i < str.length(); i++){
            if(str[i] >= 'a' && str[i] <= 'z'){
                str[i] = toupper((char)str[i]); // Convert lowercase to uppercase
            }else if(str[i] >= 'A' && str[i] <= 'Z'){
                str[i] = tolower((char)str[i]); // Convert uppercase to lowercase
            }
        }
        return str;
    }
    string input;
    cout << "Enter a string: ";
    getline(cin, input);
    cout << "Flipped case: " << flip_case(input) << endl;
    return 0;
}