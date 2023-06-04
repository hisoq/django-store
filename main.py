# # написать декоратор (пользователь задает функционал: 1) замерить время работы фуии. 2) вывести принты
import time
def time_check(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время отработки фу-ии {func.__name__}: {end_time - start}')
        return result
    return wrapper

@time_check  # () с аргументами
def test():
    time.sleep(1)

test()