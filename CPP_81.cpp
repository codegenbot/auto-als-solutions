#include <vector>
#include <string>

using namespace std;

vector<string> numerical_letter_grade(vector<float> grades) {
    vector<string> result;
    
    for (float g : grades) {
        if (g >= 4.0)
            result.push_back("A+");
        else if (g > 3.9)
            result.push_back("A");
        else if (g > 3.6)
            result.push_back("B+");
        else if (g > 3.3)
            result.push_back("B");
        else if (g > 2.9)
            result.push_back("C+");
        else if (g > 2.6)
            result.push_back("C");
        else if (g > 2.3)
            result.push_back("D+");
        else if (g >= 1.0)
            result.push_back("D");
        else
            result.push_back("E");
    }
    
    return result;
}