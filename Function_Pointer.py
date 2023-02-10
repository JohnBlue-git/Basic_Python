# Auther: John Blue
# Time: 2023/2
# Object: display how to use function pointer

def fun_ptr1():
    print("Hello one");

def fun_ptr2():
    print("Hello two");

# storage function as pointer
lst = [fun_ptr1, fun_ptr2]

# calling function by function pointer
lst[0]();
lst[1]();
