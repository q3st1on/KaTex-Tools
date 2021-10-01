columns = 2
table = """
eqNotation, eqNotation2
x^{a}\\timesx^{b}, x^{a+b}
x^{a}\\divx^{b}, x^{a-b}
x^{a}\\timesx^{b}, x^{a+b}
x^{-a}, \\frac{1}{x^{a}}
x^{\\frac{a}{b}}, \\sqrt{b}{x^{a}}
"""

def wrapper(string, i, x, table):
    if x == 0:
        if string[:2] == "eq":
            return("\\text{"+string[2:]+"}")
        else:
            return("\\text{"+string+"}")
    if table[0].split(', ')[i][:2] == "eq":
        return(string)
    else:
        return("\\text{"+string+"}")


colformat = ""
for i in range(0,columns):
    colformat += "c:"
colformat = colformat[:len(colformat)-1]
table = table.split('\n')[1:]
table = table[:len(table)-1]

print("\\begin{array}{"+colformat+"}")

for i in range(0,columns):
    print(wrapper(table[0].split(', ')[i], i , 0, table), end='')
    if i <= columns-2:
        print(" & ", end='')

print(" \\\\ \\hline ")

for x in range(1, len(table)-1):
    for i in range(0,columns):
        print(wrapper(table[x].split(', ')[i], i, x, table), end='')
        if i <= columns-2:
            print(" & ", end='')
        elif x <= len(table)-3:
            print(" & \\\\")

print("\\end{array}")