#include <vector>
#include <string>

using namespace std;

vector<string> numerical_letter_grade(vector<float> grades) {
    vector<string> result;
    
    for (float g : grades) {
        if (g >= 4.0)
            result.push_back("A+");
        else if (g > 3.7)
            result.push_back("A");
        else if (g > 3.3)
            result.push_back(g < 3.7 ? "A-" : "B+");
        else if (g > 2.9)
            result.push_back(g < 3.3 ? "B" : "C+");
        else if (g > 2.6)
            result.push_back(g < 2.9 ? "B-" : "C");
        else if (g > 2.1)
            result.push_back(g < 2.6 ? "C-" : "D+");
        else if (g > 1.8)
            result.push_back(g < 2.1 ? "D" : "E");
    }
    
    return result;
}