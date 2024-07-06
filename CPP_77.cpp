Here is the completed code:

bool iscuber(int a){
    double c = pow(a, 1.0/3.0);
    return (c == round(c));
}