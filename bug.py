def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid operand types")
        return None

# This will raise an UnboundLocalError because 'result' is not defined outside the try block 
# if an exception occurs.
print(result)