input_str = "_2818_"
output_str = "-2818_"

for i in range(2800, 2911):
    input_str = input_str.replace(f"_{i:04d_}", f"-{i:04d_}")

print(input_str)