string filp_case(string str){
    string result = "";
    for(int i=0; i<str.length(); i++){
        char c = str[i];
        if(c >= 'a' && c <= 'z')
            result += (c - ('a' - 'A'));  // Convert lowercase to uppercase
        else if(c >= 'A' && c <= 'Z')
            result += (c - ('A' - 'a'));  // Convert uppercase to lowercase
        else 
            result += c; // Do not change non-alphabet characters
    }
    return result;
}