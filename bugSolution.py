def function_with_uncommon_error(a, b):
    result = None  # Initialize result to a default value
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid operand types")
        return None

print(function_with_uncommon_error(10, 2))
print(function_with_uncommon_error(10, 0))
print(function_with_uncommon_error(10, "a"))