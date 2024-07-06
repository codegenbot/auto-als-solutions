string file_name_check(string file_name){
    int digit_count = 0;
    bool found_dot = false;
    bool valid_prefix = false;

    for(int i=0; i<file_name.length(); i++){
        char c = file_name[i];
        if(c >= '0' && c <= '9'){
            digit_count++;
            if(digit_count > 3) return "No";
        }
        else if(c == '.'){
            found_dot = true;
        }
        else if(c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z'){
            valid_prefix = true;
        }
    }

    if(!found_dot) return "No";
    string suffix = file_name.substr(file_name.find('.')+1);
    if(suffix == "txt" || suffix == "exe" || suffix == "dll")
        return "Yes";
    else
        return "No";
}