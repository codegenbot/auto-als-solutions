Here is the completed code:

string file_name_check(string file_name){
    int digit_count = 0;
    bool found_dot = false;
    for(int i=0; i<file_name.length(); i++){
        char c = file_name[i];
        if(c >= '0' && c <= '9'){
            digit_count++;
        } else if(c == '.'){
            found_dot = true;
        } else if(found_dot){
            string extension = file_name.substr(i);
            if(extension != "txt" && extension != "exe" && extension != "dll")
                return "No";
        }
    }
    if(digit_count > 3 || !found_dot)
        return "No";
    return "Yes";
}