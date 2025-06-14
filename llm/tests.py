from functions.get_files_info import get_files_info, get_file_content


def test():
    result = get_file_content("calculator", "main.py")
    print("Result for current directory:")
    print(result)
    print("")

def test2():
    result2 = get_file_content("calculator", "pkg/calculator.py")
    print("Result for current directory:")
    print(result2)
    print("")

def test3():
    result3 = get_file_content("calculator", "/bin/cat")
    print("Result for current directory:")
    print(result3)
    print("")

if __name__ == "__main__":
    test()
    test2()
    test3()