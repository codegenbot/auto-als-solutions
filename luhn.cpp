#include <vector>
using namespace std;

int luhnAlgo(vector<int> numbers) {
    int sum = 0;
    bool doubleNext = false;
    
    for (int i = numbers.size() - 1; i >= 0; --i) {
        int digit = numbers[i];
        
        if (doubleNext) {
            digit *= 2;
            
            if (digit > 9) {
                digit -= 9;
            }
        }
        
        sum += digit;
        
        doubleNext = !doubleNext;
    }
    
    return sum;
}

int main() {
    int n;
    vector<int> numbers;
    
    cin >> n;
    
    for(int i = 0; i < n; ++i) {
        int num;
        cin >> num;
        numbers.push_back(num);
    }
    
    cout << luhnAlgo(numbers) << endl;
    
    return 0;
}