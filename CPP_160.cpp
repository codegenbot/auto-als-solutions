#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
#include<algorithm>
#include<stdlib.h>

int do_algebra(vector<string> operato, vector<int> operand){
    int result = operand[0];
    for(int i=1; i<operand.size();i++){
        if(operato[i-1] == "+")  result += operand[i];
        else if(operato[i-1] == "-") result -= operand[i];
        else if(operato[i-1] == "*") result *= operand[i];
        else if(operato[i-1] == "//") {
            if(result < 0) return -1;
            result = result / static_cast<int>(operand[i]);
        }
        else{
            if(result < 0) return -1;
            result = pow(static_cast<double>(result), operand[i]);
        }
    }
    return result;
}