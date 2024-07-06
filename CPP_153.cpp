string Strongest_Extension(string class_name, vector<string> extensions){
    string strongest_ext = "";
    int strongest_strength = 0;
    
    for(auto ext : extensions){
        int cap = 0, sm = 0;
        for(char c:ext){
            if(isupper(c)) cap++;
            else if(islower(c)) sm++;
        }
        int strength = cap - sm;
        
        if(strength > strongest_strength || (strength == strongest_strength && ext < strongest_ext)){
            strongest_strength = strength;
            strongest_ext = ext;
        }
    }
    
    return class_name + "." + strongest_ext;
}