```cpp
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
    inputList.push_back(3.5);
    inputList.push_back(-1.5);
    inputList.push_back(7.8);
    inputList.push_back(-9.0);

    long long sum = 0;
    for(float n : inputList){
        if(int(n) > 0 && int(n) % 2 != 0){ 
            sum += pow(int(n), 2); 
        }
    }
    int output = double_the_difference(inputList); 
    cout << "Sum: " << sum << endl;
    return 0;
}