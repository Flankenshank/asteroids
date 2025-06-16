from functions.get_files_info import get_files_info, get_file_content
from functions.write_files import write_file


def test():
    results = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(results)


def test2():
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result2)

def test3():
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result3)

if __name__ == "__main__":
    test()
    test2()
    test3()