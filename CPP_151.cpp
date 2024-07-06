Here is the solution:

long long double_the_difference(vector<float> lst){
    long long sum = 0;
    for(float n : lst){
        if(int(n) > 0 && int(n) % 2 != 0){ // Check if number is positive and odd
            sum += pow(int(n), 2); // Add the square of the number to the sum
        }
    }
    return sum;
}