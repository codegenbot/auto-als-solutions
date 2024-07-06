int main { 
    std::vector<float> lst; 
    float num; 

    while(std::cin >> num) { 
        lst.push_back(num); 
    } 

    int sum = sum_squares(lst); 

    std::cout << "Sum of squares: " << sum << std::endl; 

    return 0;