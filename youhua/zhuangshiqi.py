import time

# 函数运行 2秒

# def timeit(func):
#     def result(*args, **kwargs):
#         start_time = time.time()
#         print(start_time)
#         func(*args, **kwargs)
#
#         time.sleep(2)
#
#         end_time = time.time()
#         print(end_time)
#
#         print('函数运行时间为：%.2fs' % (end_time - start_time))
#         return func
#     return result()
# @timeit
# def t_1():
#     print("11111")
# @timeit
# def t_2():
#     print('22222')
#
# @timeit
# def t_3():
#     print('333333')
# # t_2()
# t_3()
# t_1()
class ClassDeco:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Running {self.func.__name__}')
        self.func()
        print(f'End {self.func.__name__}')

@ClassDeco  # 等价于 foo = ClassDeco(foo)
def foo():
    print('do something')

foo()
