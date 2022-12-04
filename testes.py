import variaveis as vars

# testing if the variables can be used as int for a simple sum
vars.tsomaconj1 = vars.asoma1 + vars.asoma2 + vars.asoma3 + vars.asoma4
vars.tsomaconj2 = vars.bsoma1 + vars.bsoma2 + vars.bsoma3 + vars.bsoma4

# testing if they can becompared
print(vars.tsomaconj2)
print(vars.tsomaconj1)
if vars.tsomaconj1 < vars.tsomaconj2:
    print(vars.tsomaconj2)
else:
    print("n")