int do_algebra(vector<string> operato, vector<int> operand) {
    int result = operand[0];
    for(int i=1; i<operand.size();i++){
        if(operato[i-1] == "+")  result += operand[i];
        else if(operato[i-1] == "-") result -= operand[i];
        else if(operato[i-1] == "*") result *= operand[i];
        else if(operato[i-1] == "//") {
            if(result < 0) return -1;
            if(operand[i] == 0) return -2; // division by zero error
            if(operand[i] < 0 && (result % static_cast<int>(abs(operand[i]))) != 0) return -3; // invalid integer division
            result = result / static_cast<int>(operand[i]);
        }
        else{
            if(result < 0) return -1;
            if(operand[i] == 0) return -2; // power with zero error
            result = pow(static_cast<double>(result), operand[i]);
        }
    }
    return result;
}