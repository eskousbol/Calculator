#calculate simple first order derivatives
sample_fcn = "3x^5+3cos(3x)+5"
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
        if fnctn[i] != "+" and fnctn[i] != "-":
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
    #a simple polynomial etc.
    if "s" in term or "c" in term:
        term_type = 0
    elif "l" in term:
        term_type = 1
    else:
        term_type = 2
    return term_type

def trig_term(current_term):
    #differentiate a trigonometric term
    coefficient = ""
    j = 0
    trig = ""
    while current_term[j] != "c" and current_term[j] != "s":
        coefficient += current_term[j]
        j+=1
    for i in range(3):
        trig += current_term[j+i]
    j += 4
    #get derivarive of trig function
    if trig == "cos":
        new_trig = "sin("
    elif trig == "sin":
        new_trig = "cos("
    inside_fnctn = ""
    while current_term[j] != ")":
        inside_fnctn += current_term[j]
        j+=1
    inside_deriv = polynomial_term(inside_fnctn)
    answer = coefficient + "*" + inside_deriv + "*" + new_trig + inside_fnctn + ")"
    return answer

def polynomial_term(current_term):
    #differentiates one simple polynomial term
    #need to add support for fraction exponents
    j = 0
    current_char = current_term[j]
    coefficient = ""
    exponent = ""
    answer = ""
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
    return answer
    
def first_order_deriv(fnctn):
    terms, operations = split_into_terms(fnctn)
    print(terms)
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
        current_term = terms[i]
        term_type = determine_type(current_term)
        if term_type == 0:
            answer += trig_term(current_term)
        elif term_type == 2:
            answer += polynomial_term(current_term)
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

print(multi_order_deriv(1,sample_fcn))
