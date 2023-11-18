#number_1 = float(input("give me first number:"))
#number_2 = float(input("give me the second one:"))
#sum = number_1 + number_2
#print(sum)


#Second one
# def numbers():
#     number_1 = float(input("first on :"))
#     number_2 = float(input(" second on :"))
#     sum = number_1 + number_2
#     print(sum)
    
# numbers()

#-------------------------------------------------
# def numbers(A , B):
    
#     sum = A + B
#     print(sum)
    
# number_1 = float(input("Give the first number bitch :"))
# number_2 = float(input("second one :"))

# numbers(number_1,number_2)




def add(num_1: float, num_2: float) -> float:
    
    total = num_1 + num_2
    return total
    
number_1 = float(input("Give the first number bitch :"))
number_2 = float(input("second one :"))

kir = add(number_1,number_2)
print(kir)
