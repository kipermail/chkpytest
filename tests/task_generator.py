import time
 
def task1():
    count = 0
    while True:
        count += 1
        print(f"Task 1: {count}")
        yield  # Возвращаем управление диспетчеру задач
 
def task2():
    count = 0
    while True:
        count += 1
        print(f"Task 2: {count}")
        yield  # Возвращаем управление диспетчеру задач
 
def task3():
    count = 0
    while True:
        count += 1
        print(f"Task 3: {count}")
        yield  # Возвращаем управление диспетчеру задач
 
def task_scheduler(tasks, max_cycles):
    # Инициализация генераторов задач
    task_generators = [task() for task in tasks]
 
    for _ in range(max_cycles):
        for task_gen in task_generators:
            next(task_gen)  # Переключаемся между задачами
            time.sleep(0.1)  # Задержка для демонстрации параллельной работы
 
# Пример использования
tasks = [task1, task2, task3]
task_scheduler(tasks, max_cycles=5)