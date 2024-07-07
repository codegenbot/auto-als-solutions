Here is the completed code:

string file_name_check(string file_name){
    int digit_count = 0;
    bool has_dot = false;
    string before_dot;

    for(int i=0; i<file_name.size(); i++){
        if(file_name[i] >= '0' && file_name[i] <= '9'){
            digit_count++;
        }else if(file_name[i] == '.'){
            has_dot = true;
            before_dot = file_name.substr(0, i);
            string after_dot = file_name.substr(i+1);
        }
    }

    if(digit_count > 3 || !has_dot || before_dot.empty() || 
       (!isalpha(before_dot[0]) && !isupper(before_dot[0])) || 
       (after_dot != "txt" && after_dot != "exe" && after_dot != "dll")){
        return "No";
    }else{
        return "Yes";
    }
}