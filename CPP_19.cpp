#include<stdio.h>
#include<string>
#include<map>
using namespace std;

string sort_numbers(string numbers){
    map<string,int> num_map;
    num_map["zero"] = 0;
    num_map["one"] = 1;
    num_map["two"] = 2;
    num_map["three"] = 3;
    num_map["four"] = 4;
    num_map["five"] = 5;
    num_map["six"] = 6;
    num_map["seven"] = 7;
    num_map["eight"] = 8;
    num_map["nine"] = 9;

    vector<string> vec;
    string temp;
    for(int i=0; i < numbers.length(); i++){
        if(numbers[i] != ' ')
            temp += numbers[i];
        else{
            vec.push_back(temp);
            temp = "";
        }
    }
    vec.push_back(temp);

    sort(vec.begin(),vec.end());

    string result = "";
    for(int i=0; i<vec.size(); i++){
        result += vec[i] + " ";
    }

    return result;
}