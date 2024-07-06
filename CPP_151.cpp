long long double_the_difference(vector<float> lst);

int main() {
    vector<float> inputList;  
    for(int i = 0 ; i < 3 ; i++){
        float num;
        cin >> num;
        inputList.push_back(num);
    }
    
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