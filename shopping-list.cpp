#include <vector>
#include <iostream>

double totalShoppingTripCost(const std::vector<float>& prices, const std::vector<float>& discounts) {
    double totalPrice = 0.0;
    for (int i = 0; i < prices.size(); ++i) {
        float price = prices[i];
        float discount = price * discounts[i] / 100.0;
        totalPrice += price - discount;
    }
    return totalPrice;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<float> prices(n);
    for (auto& price : prices) {
        std::cin >> price;
    }
    std::vector<float> discounts(n);
    for (auto& discount : discounts) {
        std::cin >> discount;
    }
    double totalCost = totalShoppingTripCost(prices, discounts);
    std::cout << std::fixed << std::setprecision(1) << totalCost << std::endl;
    return 0;
}