d = {'Alice' : 85, 'Ashley' : 90, 'Kennedy' : 78}
st= input("Enter  student's name:")
if st in d:
    print(f"{st}'s marks: {d[st]}")
else:
    print("Student not found. ")
