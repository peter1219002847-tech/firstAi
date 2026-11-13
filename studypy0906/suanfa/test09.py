import asyncio
import time


async def my_func(name, delay):
    print(f"任务 {name} 开始...")
    await asyncio.sleep(delay)
    print(f"任务 {name} 完成.")
    return f"结果 of {name}"


async def main_concurrent():
    print("--- 并发执行（总耗时 max(1s, 2s) = 2s）---")
    # 1. 创建 Task：协程被包装成任务，立即启动在后台运行
    task1 = asyncio.create_task(my_func("C", 1))
    task2 = asyncio.create_task(my_func("D", 2))
    # 2. 等待 Task 完成：await asyncio.gather() 等待所有任务结束
    #  注意：这里的 await 只是等待结果，任务本身早已开始并发运行。
    results = await asyncio.gather(task1, task2)

    print(f"所有结果: {results}")


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main_concurrent())
    print(f"并发总耗时: {time.time() - start_time:.2f}秒")
