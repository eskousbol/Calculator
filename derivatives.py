#calculate simple first order derivatives
sample_fcn = "x^2+x-3"
#NO spaces should be present in fnctn fed to program
def split_into_terms(fnctn):
    #returns list of all the terms and the operands that seperate them
    terms = []
    current_term = []
    operations = []
    for i in range(len(fnctn)):
        #iterate through function given, every time there is a + or -
        #creat a new term
        if fnctn[i] != '+' and fnctn[i] != '-':
            current_term.append(fnctn[i])
        else:
            terms.append(current_term)
            current_term = []
            operations.append(fnctn[i])
        if i == len(fnctn) - 1:
            terms.append(current_term)
    return terms, operations

def first_order_deriv(fnctn):
    i = 0
    terms, operations = split_into_terms(fnctn)
    current_char = fnctn[i]
    while (current_char != 'x'):
        i += 1
        current_char = fnctn[i]
    if fnctn[i+1] == '^':
        current_exp = fnctn[i+2]

    return current_exp + 'x'

print(first_order_deriv(sample_fcn))
