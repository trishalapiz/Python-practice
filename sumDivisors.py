#sum of divisors

prompt = int(input("Enter an interger: ")) #14

print("The divisors of the integer you entered are: ")
divisor_sum = 0 #updated line
for i in range(1, prompt+1): #14
    if(prompt%i==0): 
        print(i)
        divisor_sum+=i #calculate sum of all divisors

print("The sum of divisors " + str(divisor_sum)) #print the sum of divisors
