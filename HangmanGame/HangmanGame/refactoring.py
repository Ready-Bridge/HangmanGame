score = int(input("Enter score : "))

st = "Your score is %d Grade is " % score

if score >= 90:

    print(st + 'A')



elif score >= 80:

    print(st + 'B')



elif score >= 70:

    print(st + 'C')



else:

    print(st + 'F')