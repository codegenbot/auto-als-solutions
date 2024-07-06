strings = input("Enter strings separated by space : ").split()
print(' '.join(filter(None, strings)))