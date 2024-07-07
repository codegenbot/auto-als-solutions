def solve(fuel_costs):
    return sum((fuel // 3) - 2 for fuel in map(int, input().split()))