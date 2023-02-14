def implies(a, b):
    if a == "F" and b == "F":
        return "T"
    elif a == "F" and b == "T":
        return "T"
    elif a == "T" and b == "F":
        return "F"
    elif a == "T" and b == "T":
        return "T"
    return


print("P = (a -> b) -> (c -> d)")
print("Q = (a -> (b -> c)) -> d")
print("* = P != Q\n")
print("a\t\t b\t\t c\t\t d\t\t| P\t\t Q")
print("____________________________________________")

final = []

c = ["F", "T"]
FxValues = []
GxValues = []

for i in c:
    for j in c:
        for k in c:
            for l in c:
                print(i, "\t\t", j, "\t\t", k, "\t\t", l, "\t\t|", implies(implies(i, j),implies(k, l)),"\t", implies(implies(i, implies(j, k)), l), end = " ")
                FxValues.append(implies(implies(i, j), implies(k, l)))
                GxValues.append(implies(implies(i, implies(j, k)), l))
                if FxValues[len(FxValues) - 1] != GxValues[len(GxValues) - 1]:
                    print("*")
                else:
                    print("")