float diff = numeric_limits<float>::max();
for(int i = 0; i < numbers.size() - 1; i++) {
    for(int j = i + 1; j < numbers.size(); j++) {
        float temp = abs(numbers[i] - numbers[j]);
        if(temp < threshold && temp < diff) {
            diff = temp;
        }
    }
}
return (diff < threshold);