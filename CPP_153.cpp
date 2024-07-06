#include <iostream>
#include <vector>
#include <string>

int Strongest_Extension(std::string class_name, std::vector<std::string> extensions) {
    int max_strength = 0;
    std::string strongest_extension;
    
    for (std::string extension : extensions) {
        int strength = 0;
        for (char c : extension) {
            if (std::isupper(c)) strength++;
            else if (std::islower(c)) strength--;
        }
        
        if (strength > max_strength) {
            max_strength = strength;
            strongest_extension = extension;
        }
    }
    
    return class_name + "." + strongest_extension;
}