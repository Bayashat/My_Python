def convert_tem(F):
    C = (5 / 9) * (F - 32)
    return C

F = float(input())
C = convert_tem(F)
print(f"{C:.1f}")

