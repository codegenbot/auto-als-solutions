```cpp
Calculate the sum of squares of all elements in the input list.

int sum_squares(vector<float> lst){
    int result = 0;
    for (float x : lst) {
        int ceil_x = ceil(x);
        result += pow(ceil_x, 2);
    }
    return result;
}

int main() {
    vector<float> lst = {1.5, 2.25, 3.0};
    cout << "Sum of squares: " << sum_squares(lst) << endl;
    return 0;
}