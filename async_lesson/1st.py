import os
import time
import asyncio
from datetime import datetime

COEFF = 1


async def interview(cort):
    name = cort[0]
    first_prepare = cort[1]
    first_defence = cort[2]
    second_prepare = cort[3]
    second_defence = cort[4]
    print(f"{name} started the 1 task.")
    time.sleep(COEFF * first_prepare)
    print(f"{name} moved on to the defense of the 1 task.")
    await asyncio.sleep(COEFF * first_defence)
    print(f'{name} completed the 1 task.')
    print(f'{name} is resting.')
    await asyncio.sleep(COEFF * 5)
    print(f"{name} started the 2 task.")
    time.sleep(COEFF * second_prepare)
    print(f"{name} moved on to the defense of the 2 task.")
    await asyncio.sleep(COEFF * second_defence)
    print(f'{name} completed the 2 task.')


async def interviews(datas):
    tasks = []
    for elem in datas:
        asyncio.create_task(interview(elem))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    t0 = time.time()  # запоминаем время начала работы
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(interviews(data)) # запускаем асинхронное приготовление
    print(time.time() - t0)
