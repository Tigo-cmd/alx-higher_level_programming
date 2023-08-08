#!/usr/bin/python3
#!/usr/bin/python3
for i in range(0, 99):
    print("0{}, ".format(i) if i <= 9 else "{}, ".format(i), end="")
print("99")
