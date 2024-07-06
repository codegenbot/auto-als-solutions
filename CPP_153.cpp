Here is the completed code:

string Strongest_Extension(string class_name,vector<string> extensions){
    string strongest = "";
    int max_strength = -1;
    
    for(auto ext : extensions){
        int upper = 0, lower = 0;
        for(char c: ext) {
            if(isupper(c)) upper++;
            else if(islower(c)) lower++;
        }
        double strength = (double)(upper-lower)/ext.length();
        
        if(strength > max_strength || (strength == max_strength && strongest.size() < extensions.size())){
            max_strength = strength;
            strongest = ext;
        }
    }
    
    return class_name + "." + strongest;
}