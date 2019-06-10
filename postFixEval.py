operator = -10
operand = -20
leftparentheses = -30
rightparentheses = -40
empty = -50
 
def precedence(s):
    if s is '(':
        return 0
    elif s is '+' or s is '-':
        return 1
    elif s is '*' or s is '/' or s is '%':
        return 2
    else:
        return 99
                 
def typeof(s):
    if s is '(':
        return leftparentheses
    elif s is ')':
        return rightparentheses
    elif s is '+' or s is '-' or s is '*' or s is '%' or s is '/':
        return operator
    elif s is ' ':
        return empty    
    else :
        return operand                          
 
def convert(infix):
	postfix = []
	temp = []
	for i in infix :
		type = typeof(i)
		if type is leftparentheses :
			temp.append(i)
		elif type is rightparentheses :
			next = temp.pop()
			while next is not '(':
				postfix.append(next)
				next = temp.pop()
		elif type is operand:
			postfix.append(i)
		elif type is operator:
			p = precedence(i)
			while len(temp) is not 0 and p <= precedence(temp[-1]) :
				postfix.append(temp.pop())
			temp.append(i)
		elif type is empty:
			continue
					 
	while len(temp) > 0 :
		postfix.append(temp.pop())
	return postfix

def evaluate(pf):
	pf = convert(pf)
	stack = []
	for c in pf:
		pf = pf[1:]
		if typeof(c) == operator:
			a = stack.pop(0)
			b = stack.pop(0)
			stack.insert(0, eval(str(a) + c + str(b)))
		else:
			stack.insert(0,c)
	return stack[0]
	
print(evaluate("2 + 5 * 8"))





































