```cpp
int do_algebra(vector<string> operato, vector<int> operand) {
    int result = 0;
    stack<int> opStack;
    for(int i=0; i<operato.size();i++){
        if(operato[i] == "(") opStack.push(i);
        else if(operato[i] == ")"){
            while(opStack.top() != (int)operand[0]) {
                if(operato[opStack.top()] == "+")  result += operand[opStack.pop()];
                else if(operato[opStack.top()] == "-") result -= operand[opStack.pop()];
                else if(operato[opStack.top()] == "*") result *= operand[opStack.pop()];
                else{
                    if(result < 0) return -1;
                    result = pow(static_cast<double>(result), operand[opStack.pop()]);
                }
            }
            opStack.pop();
        }else{
            if(opStack.size() > 0 && operato[opStack.top()] == "("){
                while(operato[opStack.top()] != ")"){
                    opStack.pop();
                }
                opStack.pop(); //pop the '('
            }
            if(operato[i] == "+")  result += operand[i];
            else if(operato[i] == "-") result -= operand[i];
            else if(operato[i] == "*") result *= operand[i];
            else if(operato[i] == "//"){
                if(result < 0) return -1;
                if(operand[i] == 0) return -1; // prevent division by zero
                result = result / static_cast<int>(operand[i]);
            }
            else{
                if(result < 0) return -1;
                result = pow(static_cast<double>(result), operand[i]);
            }
        }
    }
    return result;
}