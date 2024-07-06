#include <cmath>
#include <vector>

int sum_squares(vector<float> lst) {
    int result = 0;
    for (float x : lst) {
        int ceil_x = ceil(x);
        result += pow(ceil_x, 2);
    }
    return result;
}

int main() {
    float num;
    cout << "Enter a number: ";
    cin >> num;

    vector<float> lst;
    for(float i=num; i>=1.0; --i) {
        lst.push_back(i);
    }

    int sum = sum_squares(lst);

    cout << "Sum of squares: " << sum << endl;

    return 0;
}