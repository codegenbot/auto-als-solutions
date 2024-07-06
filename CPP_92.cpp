Here is the completed code:

bool any_int(float a, float b, float c){
    if (a == (int)b + (int)c || b == (int)a + (int)c || c == (int)a + (int)b) {
        return true;
    }
    return false;
}