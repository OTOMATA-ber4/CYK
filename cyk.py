def cyk_algorithm(grammar, start_symbol, input_string):
    n = len(input_string)
    
    # Create a table with back pointers
    table = [[{"symbols": set(), "back": []} for _ in range(n)] for _ in range(n)]

    # Step 1: Fill length 1 substrings
    for i in range(n):
        for lhs, productions in grammar.items():
            for prod in productions:
                if prod == input_string[i]:
                    table[0][i]["symbols"].add(lhs)

    # Step 2: Fill longer substrings
    for l in range(2, n + 1):
        for s in range(n - l + 1):
            for p in range(1, l):
                left_cell = table[p-1][s]["symbols"]
                right_cell = table[l-p-1][s+p]["symbols"]
                for lhs, productions in grammar.items():
                    for prod in productions:
                        if len(prod) == 2 and prod[0] in left_cell and prod[1] in right_cell:
                            table[l-1][s]["symbols"].add(lhs)
                            table[l-1][s]["back"].append((p, prod[0], prod[1]))

    # Check acceptance
    accepted = start_symbol in table[n-1][0]["symbols"]
    
    # Get derivation if accepted
    derivation = []
    if accepted:
        derivation = build_derivation(table, grammar, start_symbol, n-1, 0, input_string)
    
    return accepted, table, derivation

def build_derivation(table, grammar, symbol, i, j, string):
    if i == 0:  # Terminal case
        return [f"{symbol} → {string[j]}"]
    
    # Find the production used
    for back in table[i][j]["back"]:
        p, left, right = back
        if symbol in grammar and any(prod == left+right for prod in grammar[symbol]):
            left_deriv = build_derivation(table, grammar, left, p-1, j, string)
            right_deriv = build_derivation(table, grammar, right, i-p, j+p, string)
            return [f"{symbol} → {left}{right}"] + left_deriv + right_deriv
    
    return []

def print_derivation(derivation):
    print("\nDerivation Path:")
    for step in derivation:
        print(step)

def print_table(table, input_string):
    n = len(input_string)
    print("\nCYK Parse Table:")
    for row in range(n):
        print([",".join(sorted(cell["symbols"])) if cell["symbols"] else "-" for cell in table[row]])

if __name__ == "__main__":
    grammar = {
        "S": ["AB", "BC"],
        "A": ["BA", "a"],
        "B": ["CC", "b"],
        "C": ["AB", "a"]
    }
    start_symbol = "S"
    input_string = "baaba"

    accepted, table, derivation = cyk_algorithm(grammar, start_symbol, input_string)
    print(f"Can the string '{input_string}' be generated? {'Yes' if accepted else 'No'}")
    print_table(table, input_string)
    
    if accepted:
        print_derivation(derivation)