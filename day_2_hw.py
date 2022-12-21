#Question 1.

# This is a cool use of a list comprehension.
cubed = [a**3 for a in range(0,1001) if (a**3)< 1001]
# print(cubed)



#Question 2

prime = [a/a for a in range(1,101) if (a/1) in range(1,101)]
# print(prime)


#this is how I would tackle this- with a helper function that determines if a number 
# is prime and run that function for the desired range
# def func \/ \/ \/  
def isPrime(n):
    # We have to specify because only 2 and above work as primes
    if n > 1:
        #simple version here but both of these are completely valid
        # for x in range(2, n):

        # Optimized version that takes 1/2 as many steps
        for x in range(2, (n//2)+1):

            #checking each number in the range as the divisor of the original number
            #to find out if NOT prime
            if n % x == 0:
                #if this code-block runs we know it's not prime so return False now
                #which stops the function
                return False
        #If we've made it to the end of the loop and it's not broken the number is prime!        
        return True
    #this is back to the condition where the number is 1 or less which means not prime
    return False  
    
    #you could also write this way but there is no need
    # else:
    #     return False

#throw it in range to complete problem
#range of 0-100
for x in range(101):
    # returns either True or False for each num in range (which is x) so if True print
    if isPrime(x):
        print(x)


#Need help, saw examples online, but do not understand

#Question 3


# kids = input("Are you under 18?")
# adults = input("Are you 18-65?")
#Cant figure out how to do 65 and up :(


#for this one we're going to create an input for age and just evaluate that age:

age = int(input('how old are you?  Please input NUMBERS!'))

if age < 18:
    print('Kiddo!')
elif age < 65:
    print('Adult')
else:
    print('Sorry, you\'re old!')




# if range(1-18):
#     if "yes":
#         print("kids")
# else:
#     range(19-66)
#     if "no":
#         print("adults")

#Cannot get function to run correctly :( only prints adults.


















