# FILE NAME - convert_C_to_F_01.py

# NAME: Katrina Carpenter
# DATE: 02/14/2025
# BRIEF DESCRIPTION: Celsius to Fahrenheit lab



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience




    
# Don't forget to cast user input as a float!
    
########## ENTER YER CODE BELOW THIS LINE ##########

celsius = float(input("Enter a temperature in Celsius: "))
farenheit = (celsius * (9/5)) + 32
print(f"\n{celsius} degrees Celsius is {farenheit} degrees Fahrenheit.")

########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a temperature in Celsius: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: 1

1 degrees Celsius is 33.8 degrees Fahrenheit.

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does `float` mean?





2. Why do you think it is important to use `float` as opposed to
   a different type of variable type?

Because floats can represent decimal values, and the formula for converting celsius to fahrenheit often takes a whole number and returns a decimal. Also, it's important that this program accept decimal values for the initial input too.



'''
