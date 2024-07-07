int main() {
    std::vector<float> lst;
    float num;
    long long sum = 0;
    
    while(std::cin >> num) {
        if(num > 0 && floor(num) == num) {
            sum += pow(num, 2);
        }
    }
    
    return sum;
}