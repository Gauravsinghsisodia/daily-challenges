a=[]
b=[]
c=[]
for x in range(3):
    print("Enter/Paste your prompt. Ctrl-D to save it.If it is one line press enter and then press Ctrl+D.")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    question1='\n'.join(contents)
    print("\n")
    name=input("Input function name:\n")
    n=int(input("Enter no. of test cases:\n"))
    print("If inputs are strings put them in quotes")
    inp=[input("Enter inputs:\n") for _ in range(n)]
    out=[input("Enter outputs:\n") for _ in range(n)]
    notes=input("Enter Notes:\n")
    var=f'*{notes}*\n\n'
    if x==0:
        a.append("**Here Is Today's :python: Task for Beginners:**")
        a.append('------------------------------------------------')
        a.append(question1+'\n')
        a.append("**Examples**")
        a.append("```python")
        for x,y in zip(inp,out):
            a.append(f"{name}({x}) ➞ {y}\n")
        a.append("```\n\n")
        a.append("**Notes:**")
        a.append(var)
    elif x==1:
        b.append("**Here Is Today's :python: Task for Intermediates:**")
        b.append('------------------------------------------------')
        b.append(question1+'\n')
        b.append("**Examples**")
        b.append("```python")
        for x,y in zip(inp,out):
            b.append(f"{name}({x}) ➞ {y}\n")
        b.append("```\n\n")
        b.append("**Notes:**")
        b.append(var)
    elif x==2:
        c.append("**Here Is Today's :python: Task for Experts:**")
        c.append('------------------------------------------------')
        c.append(question1+'\n')
        c.append("**Examples**")
        c.append("```python")
        for x,y in zip(inp,out):
            c.append(f"{name}({x}) ➞ {y}\n")
        c.append("```\n\n")
        c.append("**Notes:**")
        c.append(var)
print("@Coder")
print('------------------------------------------------')
for x in a:
    print(x)
for x in b:
    print(x)
for x in c:
    print(x)
print("---------------------------")
print("**Goodluck to you all :v:**")
print("---------------------------")
