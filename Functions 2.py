
"""
  -------------------------------------------------------
  Takes two numbers and subtracts them
  -------------------------------------------------------
  Parameters:
      num1 - first number from user  (int)
      num2 - second number from user (int)
  Returns:
      result - value of the result of num1 and num2 being subtracted (int)
  -------------------------------------------------------
"""
num1 = int(input("1st number:"))

num2 = int(input("2nd number:"))

def sub(num1,num2):
    answer = num1 - num2
    return answer

result = sub(num1,num2)

print(result)

