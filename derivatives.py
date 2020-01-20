#calculate simple first order derivatives
sample_fcn = "x^2+x"
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
    terms, operations = split_into_terms(fnctn)
    answer = ""
    for i in range(len(terms)):
        #getting derivative of each term
        j = 0
        current_term = terms[i]
        current_char = current_term[j]
        coefficient = ""
        exponent = ""
        while (current_char != 'x'):
            #get starting coefficient
            coefficient += current_char
            j += 1
            current_char = current_term[j]
        if len(coefficient) == 0:
            #in case coefficient is not written in
            coefficient = "1"
        if j != len(current_term) - 1 and current_term[j+1] == '^':
            #assuming exponent is rest of the string in term
            for k in range(j+2,len(current_term)):
                exponent += current_term[k]
        if len(exponent) == 0:
            #in case exponent is not written in
            exponent = "1"
        #this is the derivative of the term
        answer = answer + (str(int(exponent) * int(coefficient))+ "x^" + str(int(exponent)-1))
        if i != len(terms) - 1:
            #if it is not the last term, add an operand before moving to the next one
            answer += operations[i]
    return answer

print(first_order_deriv(sample_fcn))
