bool any_int(float a, float b, float c){
    if (fmod(a+b-c,1) == 0 && fmod(a+b-0.5,2) > -0.5)
        return true;
    else
        return false;
}