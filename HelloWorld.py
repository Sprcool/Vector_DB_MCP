# a = 10 
# b = 40
# print(a+b)

#list

# a = [1,2,3,4,5,"chandu","monika"]
# print(a)
# print(a[0])

#set 

# b = {1,1,2,2,2,2,3,4,5,6,7}

# print(b)

# tuple

# g = (1,2,3,4,5,6,7,8)
# print(g)
# g.append(9)

# dictionary

# h = {
#     "a" : 1,
#     "b" : 2,
#     "c" : 3
# }

# print(h)

# def sum (a , b) :
#     return a+b


# print(sum (3,4))

# def condition (f,g) :
#     if(f>g) :
#         return f - g
#     else :
#         return f + g

# print(condition(10,7)) 

# name = "Eren"
# print(f"My name is {name}")

# # Reverse string

# def rev(a) :
#     return a[::-1]

# print (rev("ErenYeagar"))

#count

def counter(inputText) :
    return len(inputText)

print (counter("Sailaja"))

# lambda functions

add = lambda a,b : a+b

print(add(1,4))

largest = lambda a,b : a if a>b else b

print(largest(10,20))