def convert_grams(gram):
    ounces = gram / 28.3495231
    return ounces

gram = float(input())
ounces = convert_grams(gram)

print(f"{ounces:.8f}")