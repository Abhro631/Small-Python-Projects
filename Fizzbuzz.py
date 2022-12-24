for i in range(1, 20):
  #if divisible by 3 as well as 5
    if i % 3 == 0 and i % 5 == 0:
        print("Abhro")
        #if only divisible by 3
    elif i % 3 == 0:
        print("Abi")
        #if only divisible by 5
    elif i % 5 == 0:
        print("Set")
    else:
        print(i)
    
  #Abhro=FizzBuzz
  #Abi=Fizz
  #Set=Buzz
