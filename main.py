import sys
line = 1

var = ""
knowledge_base = []
clause_dict = {}

def negate_var(var):
    for char in var:
        if char == '~':
            var = var[1]
            return var
        else:
            var = "~" + var
            return var
        
def resolve(clause1, clause2):
    clause_to_remove = []
    counter = 0
    
    for x in clause1:
        for y in clause2:
            if len(x) - len(y) != 0:
                if x[-1] == y[-1]:
                    counter += 1
                    if counter > 1:
                        return None
                    clause_to_remove.append(x[-1])
    if counter == 0:
        return None
    for c in clause1:
        if c[-1] == clause_to_remove[0]:
            clause1.remove(c)
    for c in clause2:
        if c[-1] == clause_to_remove[0]:
            clause2.remove(c)
    new_clause = clause1 + clause2
    return set(new_clause)

if len(sys.argv) == 2:
    input_file = sys.argv[1]
file1 = open(input_file, "r")
num = 1
readList = file1.readlines()

for rl in range(len(readList)):
    readList[rl] = readList[rl].strip()
for x in readList:
    var = x[0:]
    var = list(var.split())
    if x == readList[-1]:
        last_var = x.split()
        for y in last_var:
            t = negate_var(y)
            arr = [t]
            knowledge_base.append(arr.copy())
            print(f"{line}. {t}")
            line += 1
            clause_dict[str(arr.copy())] = arr.copy()
    else: 
        knowledge_base.append(var)
        print(f"{line}. {str(var)}")
        line += 1
        clause_dict[str(var)] = var
    num+=1
clauses = knowledge_base
ptr1 = 0
ptr2 = 1
length = len(clauses)
while ptr2 < length:
    ptr1 = 0
    while ptr1 < ptr2:
        new_clause = resolve(clauses[ptr2].copy(), clauses[ptr1].copy())
        if new_clause is not None:
            new_clause = list(new_clause)
            if len(new_clause) == 0:
                print(f"{line}. Contradiction")
                length = 0
                break
            if str(new_clause) not in clause_dict:
                new_clause.sort()
                clauses.append(new_clause)
                print(f"{line}. {str(new_clause)}")
                line += 1
                clause_dict[str(new_clause)] = new_clause
            #print(f"New clause: {new_clause} {(ptr2)}, {(ptr1)}")
            length = len(clauses)
        ptr1 += 1
    ptr2 += 1
    #print("clauses: ", clauses)


