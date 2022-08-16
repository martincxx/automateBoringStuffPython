def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Division by Zero')


print(div42by(20))
print(div42by(0))
print(div42by(12))
