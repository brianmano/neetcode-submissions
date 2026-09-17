class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            #print(i)
            if (i != "+" and i != "-" and i != "*" and i != "/" ):
                stack.append(int(i))
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                if i == "+":
                    temp = t2 + t1
                if i == "-":
                    # print(stack[1])
                    # print(stack[0])
                    temp = t2 - t1
                    # print(temp)
                if i == "*":
                    temp = t2 * t1
                if i == "/":
                    temp = int(t2 / t1)

                stack.append(temp)
                #print(stack)
                
        return stack.pop()