#include<stdio.h>
#include<string>
#include<map>
using namespace std;

string sort_numbers(string numbers) {
    map<string,int> num_map;
    string temp;

    for(int i = 0; i < numbers.length(); i++) {
        if(numbers[i] == ' ') {
            continue;
        } else {
            temp = "";
            while(i < numbers.length() && numbers[i] != ' ') {
                temp += numbers[i];
                i++;
            }
            num_map[temp]++;
            i--;
        }
    }

    string result = "";
    for(auto it = num_map.begin(); it != num_map.end(); it++) {
        if(result.length() > 0) {
            result += " ";
        }
        for(int i = 0; i < it->second; i++) {
            result += it->first;
        }
    }

    return result;
}