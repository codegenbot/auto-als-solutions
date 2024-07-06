int main 
{
    std::vector<int> pile1 = make_a_pile(8);
    std::vector<int> pile2 = make_a_pile(8);
    
    for (int i : pile1)
        std::cout << i << " ";
    std::cout << "\n";
    
    for (int i : pile2)
        std::cout << i << " ";
    std::cout << "\n";
}