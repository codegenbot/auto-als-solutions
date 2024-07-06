#include <vector>
#include <string>

std::vector<std::string> numerical_letter_grade(std::vector<int> scores) {
    std::vector<std::string> grades;
    
    for (int score : scores) {
        if (score >= 90)
            grades.push_back("A");
        else if (score >= 80)
            grades.push_back("B");
        else if (score >= 70)
            grades.push_back("C");
        else if (score >= 60)
            grades.push_back("D");
        else
            grades.push_back("F");
    }
    
    return grades;
}