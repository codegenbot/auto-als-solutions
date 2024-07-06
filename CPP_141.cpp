#include <cctype>
#include<string>
using namespace std;

string file_name_check(string file_name){
    int count_dot = 0;
    bool starts_with_letter = false;
    int digit_count = 0;
    
    for(int i=0; i<file_name.length(); i++){
        if(file_name[i] == '.'){
            count_dot++;
        }
        else if(isdigit(file_name[i])){
            digit_count++;
        }
        else if(i==0){
            starts_with_letter=true;
        }
        
        if(count_dot > 1 || (starts_with_letter && !isalpha(file_name[0])) 
          || digit_count > 3) return "No";
    }
    
    if(count_dot != 1) return "No";
    
    string after_dot = file_name.substr(file_name.find('.')+1);
    string allowed_extensions[]={"txt","exe","dll"};
    bool found=false;
    for(int i=0; i<3; i++){
        if(after_dot == allowed_extensions[i]){
            found=true;
            break;
        }
    }
    
    if(!found) return "No";
    
    return "Yes";
}