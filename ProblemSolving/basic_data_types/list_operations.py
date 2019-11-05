if __name__ == '__main__':
    num_operations = int(input())
    
    operations = []
    for _ in range(num_operations):
        # get the expression
        expr = input().split()
        cmd = expr[0]
        args = expr[1:]
        if cmd == 'print':
            print(operations)
        else:
            cmd = cmd + "(" + ", ".join(args) + ")"
            eval("operations."+cmd)



# user_input = "insert 0 5".split()

# cmd = user_input[0]
# args = user_input[1:]
# cmd = cmd + "(" + ", ".join(args) + ")"
# print(cmd)
