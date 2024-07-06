#include <string>
using namespace std;

bool check_dict_case(map<string,string> dict){
    for(auto &pair : dict) {
        if(pair.first.length() > 0 && (!isupper(pair.first[0]) || !islower(pair.first))) 
            return false;
    }
    return true;