input_str = "_-2823_")
for i in range(2823, 2911):
    input_str = input_str.replace(f"_{i:04d_}", f"-{i:04d_}")

print(input_str)