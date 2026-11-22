class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for ops in operations:
            if ops not in ["+","C","D"]:
                try:
                    num = int(ops)
                    stack.append(num)
                    print(f"stack inside try {stack}")
                except:
                    raise
            elif ops == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                final = num1 + num2
                stack.append(final)
                print(f"stack when + {stack}")
            elif ops == "C":
                stack.pop()
                print(f"stack when C {stack}")
            elif ops == "D":
                prev = stack[-1]
                stack.append(prev * 2)
                print(f"stack when D {stack} ")
            else:
                continue
        total = sum(stack)
        return total