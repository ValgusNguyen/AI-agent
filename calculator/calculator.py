def add(x, y):
    return x + y 

def subtract(x, y):
    return x - y

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    sum_result = add(num1, num2)
    difference_result = subtract(num1, num2)
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference_result}")