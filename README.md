# Reverse-Polish-Notation
A reverse polish notation (RPN) implementation to analyse and calculate mathematical formula 

Please have a look at https://en.wikipedia.org/wiki/Reverse_Polish_notation to find out more!


How to use:

formula = ['(', '4', '+', '(', '4', '*', '4', '+', '2',')', ')', '*', '8']

(rpn_format, a) = generateRPN(formula)

print (rpn_format)

result = calculateFromRPN(rpn_format)

print(result)


Output:
['4', '4', '4', '*', '2', '+', '+', '8', '*']

176.0 
