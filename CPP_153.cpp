```
#include <vector>
#include <string>
#include <cctype>

using namespace std;

int Strongest_Extension(string class_name, vector<string> extensions) {
    int max_strength = 0;
    string strongest_extension;
    
    for (string extension : extensions) {
        int strength = 0;
        for (char c : extension) {
            if (isupper(c)) strength++;
            else if (islower(c)) strength--;
        }
        
        if (strength > max_strength) {
            max_strength = strength;
            strongest_extension = extension;
        }
    }
    
    return class_name + "." + strongest_extension;
}