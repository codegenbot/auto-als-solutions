```c++
int length = s.length();
if(length < 3) return false;
for(int i = 0; i <= length - 3; i++){
    string sub = s.substr(i, 3);
    bool is_distinct = true;
    for(char c : sub){
        if(find(sub.begin(), sub.end(), c) == sub.end()){
            is_distinct = false;
            break;
        }
    }
    if(!is_distinct) return false;
}
return true;