```
size_t dot_pos = 0; 
for (int i=0; i<file_name.length(); i++) { 
    if (file_name[i] == '.') { 
        dot_pos=i; 
        break; 
    } 
} 
string after_dot = file_name.substr(dot_pos+1);