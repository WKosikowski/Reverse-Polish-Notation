operations = ['+','-','*','/']

brackets = ['(', ')']

def isOperation(element):
	return element in operations

def isBracket(element):
	return element in brackets

def generateRPN(formula, start = 0):
	stack = []
	rpn = []
	x = start - 1

	numberOfBrackets = 0
	for a in range(start, len(formula)):
		x +=1
		if x >= len(formula):
			return (rpn + stack, numberOfBrackets)
		element = formula[x]
		if element == '(':
			(insideBracket, position) = generateRPN(formula, x + 1)

			x = position 
			rpn += insideBracket
		elif element == ')':
			return (rpn + stack, x)
		elif isOperation(element) == False:
			rpn.append(element)
		else:
			if element== "*" or "/"  and not stack:
				stack.append(element)
			elif element == "+" or "-":
				if not stack:
					stack.append(element)
				else:
					rpn.append(stack.pop())
					stack.append(element)
				
			else:
				rpn.append(element)
	
	return (rpn + stack, len(formula))



def calculate(a, b, operation):
	a = float(a)
	b = float(b)
	if operation == "+":
		wynik = a + b
	elif operation == "-":
		wynik = a - b
	elif operation == "*":
		wynik = a * b
	elif operation == "/":
		wynik = a / b
	return str(wynik)



def calculateFromRPN(rpn):
	stack = []
	for x in range(len(rpn)):
		element = rpn[x]
		if isOperation(element) == False:
			stack.append(element)
		else:
			b = stack.pop()
			a = stack.pop()
			stack.append(calculate(a, b, element))		
	return stack.pop()

toCalculate = ['(', '4', '+', '(', '4', '*', '4', '+', '2',')', ')', '*', '8']
#toCalculate = ['(','4', '+', '2',')','*','8']



#(4+3)*(4-1)


(rpn_format, a) = generateRPN(toCalculate)
print (rpn_format)
result = calculateFromRPN(rpn_format)
print(result)