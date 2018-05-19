#list with 5 varables 
int_list = []

counter=1
result=0
su=0
counter=0
go=0
ga =0 #ints greater than average
while (go < 5):
    num = int(input("Enter a number less than 100: "))
    if(num>100):
        print("error, has to be lesss than 100")
    else:
        int_list.append(num)
        go = go+1
#goes through list and computes the sum
if(len(int_list) > 0 and len(int_list) <100):
    
    while(counter < len(int_list)):
        print(int_list[counter])
        su= su + int_list[counter]
        counter =counter + 1
result= su
print("The sum of the array is %d" %(result))
#computing the average
average = result / len(int_list)
print(average)

#numbers greater than average
counter=0
while(counter < len(int_list)):
        if (int_list[counter] >average):
            ga = ga +1 #increments the average counter
        counter =counter + 1
print("The indexes greater than the average are %d" % (ga))
