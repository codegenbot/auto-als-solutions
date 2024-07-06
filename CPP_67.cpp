#include <iostream>
using namespace std;

int fruit_distribution(string s, int n) {
    int total_apples = 0;
    int total_oranges = 0;
    
    size_t pos = 0;
    while ((pos = s.find(" apples")) != string::npos) {
        total_apples += stoi(s.substr(pos + 8));
        s.erase(0, pos + 8);
    }
    
    while ((pos = s.find(" oranges")) != string::npos) {
        total_oranges = stoi(s.substr(0, pos).erase(0, 7));
        s.erase(0, pos + 7);
    }
    
    return n - total_apples - total_oranges;
}

int main() {
    string str;
    int n;
    cout << "Enter the fruit information: ";
    cin >> str;
    cout << "Enter the number of people: ";
    cin >> n;
    cout << "The remaining fruit is: " << fruit_distribution(str, n) << endl;
    return 0;
}