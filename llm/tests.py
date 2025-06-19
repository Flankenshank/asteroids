from functions.get_files_info import get_files_info, get_file_content
from functions.write_files import write_file
from functions.run_python import run_python_file


def test():
    results = get_files_info({'directory': '.'})
    print(results)


def test2():
    result2 = get_files_info({'directory': 'pkg'})

def test3():
    result3 = run_python_file("calculator", "../main.py")
    print(result3)

def test4():
    result4 = run_python_file("calculator", "nonexistent.py")
    print(result4)

if __name__ == "__main__":
    test()
    test2()
    test3()
    test4()
    print("Ran all run_python_file tests!")