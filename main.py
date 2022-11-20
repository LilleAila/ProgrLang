from interpreter.interpreter import run
from sys import argv

def shell():
    while True:
        text = input("$ ")
        # if text.strip() == "exit": break
        if text.strip() == "":
            continue
        elif text in ("clear", "cls"):
            result, error = run("<stdin>", "clear()")
        else:
            result, error = run("<stdin>", text)

            if error:
                print(error.as_string())
            elif result:
                if len(result.elements) == 1:
                    print(repr(result.elements[0]))
                else:
                    print(repr(result))

def runfile(filename):
    if filename == "shell":
        shell()
    _, error = run("<stdin>", f"run(\"{filename}\")")
    if error: return print(error.as_string())

runfile(argv[1] if len(argv) > 1 else input("File name: "))