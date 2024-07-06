```python
problem = """def digitSum(s):
    return str(sum(ord(c) - 55 for c in s.upper() if 'A' <= c <= 'Z'))
"""