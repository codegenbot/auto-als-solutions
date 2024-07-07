bool iscuber(int a){
    double c = cbrt(a);
    return std::floor(c + 0.5) * std::floor(c + 0.5) * std::floor(c + 0.5) == a;
}