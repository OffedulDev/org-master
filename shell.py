import org

while True:
    text = input('org > ')
    result, error = org.run("<stdin>", text)

    if error: print(error.as_string())
    elif result: print(repr(result))