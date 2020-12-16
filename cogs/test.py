# pattern shows that initial number is 64 and should be divided by 2 until 64 becomes 1
num=64 #initial number to print
for x in range(7): #we need to loop it 7 times to make 64 come to 1
    print(num,end=' ') #printing the number
    num//=2 #dividing num by 64
