#include<string>
#include<map>
#include<unordered_map>
using namespace std;

map<char,int> histogram(string test){
    map<char,int> result;
    unordered_map<char,int> count;
    string temp;
    
    for(int i=0; i<test.length(); i++){
        if(test[i] == ' ' || i==test.length()-1){
            if(temp.length() > 0){
                if(count.find(temp[0]) == count.end()){
                    count[temp[0]] = 1;
                }else{
                    count[temp[0]]++;
                }
                temp.clear();
            }
        }else{
            temp += test[i];
        }
    }
    
    int maxCount = 0;
    for(auto it : count){
        if(it.second > maxCount){
            maxCount = it.second;
        }
    }
    
    map<char,int> finalResult;
    for(auto it : count){
        if(it.second == maxCount){
            finalResult[it.first] = it.second;
        }
    }
    
    return finalResult;
}