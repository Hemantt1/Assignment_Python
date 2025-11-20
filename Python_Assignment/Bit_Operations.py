val = 0xCAFE

result1 = (bin(val & 0xF).count("1") >= 3)
result2 = ((val >> 8) | (val << 8)) & 0xFFFF
result3 = ((val << 4) | (val >> 12)) & 0xFFFF

print(result1)
print(hex(result2))
print(hex(result3))
