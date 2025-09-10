def my_function(a, b):
    print("chamei")

    return a + b


def my_new_function(a, b):
    print("chamei")

    for number in range(5):
        print(f"numero = {number}")
        yield number  # <----
        print("saiu do yield")
        yield "xyz"  # <----

    return a + b


result = my_new_function(5, 10)
value1 = next(result)
value2 = next(result)
value3 = next(result)

print(value1, value2, value3)
