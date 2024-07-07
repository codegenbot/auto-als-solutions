#include <vector>
using namespace std;

int fuelCost(vector<int> vec) {
    int sum = 0;
    for (int i : vec) {
        if(i%3==0){
            sum += (i/3 - 2);
        }
        else{
            sum += (i/3 - 1);
        }
    }
    return sum;
}

int main() {
    vector<int> vec;
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        vec.push_back(x);
    }
    cout << fuelCost(vec) << endl;
    return 0;
}