#include <vector>
#include <iostream>

using namespace std;

bool issame(float x, float y) {
    if(x == y)
        return true;
    else
        return false;
}

vector<float> get_positive(vector<float> l){
    vector<float> result;
    for(float i : l) {
        if(i > 0) {
            result.push_back(i);
        }
    }
    return result;
}

int main() {
    vector<float> numbers = {1, -2, 3, -4, 5};
    vector<float> positive_numbers = get_positive(numbers);

    for(float num : positive_numbers) {
        if(issame(num, 0)) {
            cout << "Number is zero." << endl;
        } else if (num > 10) {
            cout << "Large number: " << num << endl;
        } else {
            cout << "Number: " << num << endl;
        }
    }

    return 0;
}