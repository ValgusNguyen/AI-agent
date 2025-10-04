# from functions.write_file import write_file

# def run_tests():
#     print("=== Test overwrite lorem.txt ===")
#     print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

#     print("\n=== Test nested new file ===")
#     print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

#     print("\n=== Test forbidden absolute path ===")
#     print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

# if __name__ == "__main__":
#     run_tests()

from functions.get_files_info import get_files_info


def test():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)


if __name__ == "__main__":
    test()