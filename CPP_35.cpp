#include <vector>
#include <iostream>

float max_element(vector<float> l){
    float max = l[0];
    for(int i=1; i<l.size(); i++){
        if(l[i] > max)
            max = l[i];
    }
    return max;
}

int main() {
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;

    vector<float> v(n);
    cout << "Enter the elements:" << endl;
    for(int i=0; i<n; i++){
        cin >> v[i];
    }

    float max = max_element(v);

    cout << "The maximum element is: " << max << endl;

    return 0;
}