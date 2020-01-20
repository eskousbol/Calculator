#calculate simple first order derivatives
sample_fcn = "x^2"

def first_order_deriv(fnctn):
    i = 0
    current_char = fnctn[i]
    while (current_char != 'x'):
        i += 1
        current_char = fnctn[i]
    if fnctn[i+1] == '^':
        current_exp = fnctn[i+2]
    return current_exp + 'x'

print(first_order_deriv(sample_fcn))