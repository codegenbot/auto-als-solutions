#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int do_algebra(vector<string> operatorVec, vector<int> operandVec) {
    string expression = "";
    
    for (int i = 0; i < operatorVec.size(); i++) {
        expression += to_string(operandVec[i]);
        
        if (i < operatorVec.size() - 1) {
            expression += operatorVec[i];
        }
    }
    
    int result = eval(expression.c_str());
    
    return result;
}

int eval(char* str)
{
    char temp[10];
    int i, j, k;

    for(i=0;str[i];i++)
    {
        if(str[i] == ' ')
            continue;
        
        else
        {
            if(str[i] >= '0' && str[i] <= '9')
            {
                for(j=i;str[j]>='0'&&str[j]<='9';j++);
                for(k=0;(k<10)&&(str[j-k]>='0'&&str[j-k]<='9');k++)
                    temp[k] = str[j-k];
                temp[k] = '\0';
                i = j;
            }
        }
    }

    int num = atoi(temp);
    return num;
}