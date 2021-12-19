"""
File: arithExp.py
Author: Man-Chi Leung
A program for evaluating arithmetic expressions.
"""

from liststack import ListStack

operator = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 3, ")": 3}
stack = ListStack()


def infix_to_postfixreturn(infix_exp):
    """ Converts infix expression to postfixreturn expression.
    Return postfixreturn expression.
    Operands/operators are separated by spaces in expressions."""
    postfix = ""
    inparent = False

    for i in infix_exp.split(" "):
        if isOperator(i):
            if inparent:
                if stack.peek() == "(":
                    stack.push(i)
                elif i == ")":
                    while not stack.peek() == "(":
                        postfix += stack.pop() + " "
                    stack.pop()
                    inparent = False
            else:
                if i == "(":
                    stack.push(i)
                    inparent = True
                elif stack.isEmpty():
                    stack.push(i)
                else:
                    count = 0
                    while not stack.isEmpty():
                        count += 1
                        if checkPresidence(i):
                            stack.push(i)
                            break
                        else:
                            postfix += str(stack.pop()) + " "
                            count -= 1
                        if count == len(stack):
                            stack.push(i)
                            break
        else:
            postfix += i + " "
    postfix += str(stack.pop())
    return postfix


def isOperator(c):
    if operator.__contains__(c):
        return True
    else:
        return False


def checkPresidence(c):
    op = operator.get(c)
    for i in stack.peek():
        if op > operator[i]:
            return True
        else:
            return False

def matchedPren(infix):
    numberOfParentheses = 0
    numberOfOpsInParen = []

    inparen = False
    for ch in infix.split(" "):
        if ch == '(':
            inparen = True
            numberOfParentheses += 1
        if inparen and isOperator(ch):
            stack.push(ch)
            if stack.peek() == ')':
                inparen = False
                temp = 0
                while not stack.isEmpty():
                    if stack.peek() != '(' and stack.peek() != ')':
                        temp += 1
                    stack.pop()
                numberOfOpsInParen.append(temp)

    compare = numberOfOpsInParen[0]

    if numberOfParentheses != len(numberOfOpsInParen):
        return False
    for num in numberOfOpsInParen:
        if num != compare:
            return False

    return True

def recursive(num=0):
    number = num
    if stack.isEmpty():
        return number
    if stack.peek() != '(' and stack.peek() != ')':
        number += 1
    stack.pop()
    recursive(number)



def main():
    infix = "4 + 5 * 6 - 3"
    postfix = infix_to_postfixreturn(infix)
    print("Infix expression:", infix)
    print("postfixreturn expression:", postfix)
    print()

    infix = "( 4 + 5 ) * ( 6 - 3 )"
    postfix = infix_to_postfixreturn(infix)
    print("Infix expression:", infix)
    print("postfixreturn expression:", postfix)


    infix = "( 2 * 3 ) + ( 6 + 4 ) * 5"
    infix = "( ( 2 * ( 3 + 6 ) + 4 ) * 5"

    print(matchedPren(infix))


if __name__ == "__main__":
    main()
