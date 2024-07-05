#include <vector>
using namespace std;

double find_zero(vector<double> coeffs) {
    double root = 1;
    for(int i=0; i<coeffs.size();i++) {
        if(i%2==0){
            root = -coeffs[i]/(root);
        } else {
            root = (double)(coeffs[i-1])/(coeffs[i]+root);
        }
    }
    return round(root, 10);
}

int main() {
    vector<double> coeffs;
    coeffs.push_back(2); 
    coeffs.push_back(-7.5);
    coeffs.push_back(3.5);
    coeffs.push_back(-1);

    double solution = find_zero(coeffs);
    
    return 0;
}