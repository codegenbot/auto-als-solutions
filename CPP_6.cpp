#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

vector<int> parse_nested_parens(string paren_string){
    vector<int> result;
    int max_depth = 0;
    for(int i=0; i<paren_string.length(); i++){
        if(paren_string[i] == '('){
            int depth = 1;
            int j=i+1;
            while(j < paren_string.length() && (paren_string[j] == '(' || paren_string[j] == ')')){
                if(paren_string[j] == '(') depth++;
                else if(paren_string[j] == ')') depth--;
                j++;
            }
            i = j-1;
            result.push_back(depth);
            max_depth = max(max_depth, depth);
        }
    }
    return result;
}