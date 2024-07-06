long long double_the_difference(vector<float> lst){
    long long sum = 0;
    for(float n : lst){
        if(int(n) > 0 && int(n) % 2 != 0){ 
            sum += pow(int(n), 2); 
        }
    }
    return sum;
}

int main() {
    vector<float> inputList;  
    // Read your input data here

    long long sum = 0;
    for(float n : inputList){
        if(int(n) > 0 && int(n) % 2 != 0){ 
            sum += pow(int(n), 2); 
        }
    }
    long long output = double_the_difference(inputList); 
    assert (output == sum );
    return 0;
}