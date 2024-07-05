```cpp
double find_zero(vector<double> xs){
    double root = 1;
    for(int i=1; i<xs.size();i+=2) {
        root = -xs[i]/(i*root);
    }
    return round(root, 10);
}

int main() {
    vector<double> xs = {...}; 
    double solution = find_zero(xs);    
    assert (abs(xs) < 1e-3);   
    return 0;
}