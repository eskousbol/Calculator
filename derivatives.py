#calculate simple first order derivatives
sample_fcn = "3x^5+6x+5"
#NO spaces should be present in fnctn fed to program
def split_into_terms(fnctn):
    #returns list of all the terms and the operands that seperate them
    terms = []
    current_term = []
    operations = []
    for i in range(len(fnctn)):
        #iterate through function given, every time there is a + or -
        #creat a new term
        if fnctn[i] == chr(32):
            return(-1,-1)
        if fnctn[i] != '+' and fnctn[i] != '-':
            current_term.append(fnctn[i])
        else:
            terms.append(current_term)
            current_term = []
            operations.append(fnctn[i])
        if i == len(fnctn) - 1:
            terms.append(current_term)
    return terms, operations

def determine_type(term):
    #determine the type of the term, whether it is a trigonometric function, exponential,
    #a simple polynomial, logarithmic etc.
    pass

def polynomial_deriv(term):
    #intend to move differentiation of a polynomial term here
    pass

def first_order_deriv(fnctn):
    terms, operations = split_into_terms(fnctn)
    if terms == -1 and operations == -1:
        #xhexks to see if there are any spaces in terms
        print("This is not a valid function! Please include no spaces when typing.")
        return None
    if 'x' not in terms[len(terms)-1]:
        #drops constant calue immediately
        terms = terms[0:len(terms)-1]
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
        if int(exponent) > 1:
            answer = answer + (str(int(exponent) * int(coefficient))+ "x^" + str(int(exponent)-1))
        else:
            answer = answer + (str(int(exponent) * int(coefficient)))
        if i != len(terms) - 1:
            #if it is not the last term, add an operand before moving to the next one
            answer += operations[i]
    return answer

def multi_order_deriv(ord_deriv, fnctn):
    i = 0
    while i < ord_deriv:
        fnctn = first_order_deriv(fnctn)
        i+=1
    return fnctn

print(multi_order_deriv(2,sample_fcn))
