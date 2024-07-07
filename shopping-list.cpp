#include <vector>
#include <iostream>

double totalShoppingTripPrice(const std::vector<double>& prices, const std::vector<double>& discounts) {
    double total = 0.0;
    for (int i = 0; i < prices.size(); ++i) {
        double priceWithDiscount = prices[i] * (1 - discounts[i] / 100.0);
        total += priceWithDiscount;
    }
    return total;
}

int main() {
    int numItems, numDiscounts;
    std::cin >> numItems >> numDiscounts;
    
    std::vector<double> prices(numItems), discounts(numDiscounts);
    
    for (int i = 0; i < numItems; ++i) {
        std::cin >> prices[i];
    }
    
    for (int i = 0; i < numDiscounts; ++i) {
        std::cin >> discounts[i];
    }
    
    std::cout << totalShoppingTripPrice(prices, discounts) << std::endl;
    
    return 0;
}