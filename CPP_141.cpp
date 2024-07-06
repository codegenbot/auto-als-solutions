string file_name_check(string file_name){
    int dot_count = 0;
    bool has_dot = false;
    int digit_count = 0;
    for(int i=0; i<file_name.length(); i++){
        if(file_name[i] == '.'){
            dot_count++;
            has_dot = true;
        } else if(isdigit(file_name[i])){
            digit_count++;
        }
    }
    
    if(dot_count > 1 || !has_dot) return "No";
    if(digit_count > 3) return "No";
    
    string before_dot = file_name.substr(0, file_name.find('.'));
    if(before_dot.empty() || !isalpha(before_dot[0])) return "No";
    
    string after_dot = file_name.substr(file_name.find('.') + 1);
    if(after_dot != "txt" && after_dot != "exe" && after_dot != "dll") return "No";
    
    return "Yes";
}