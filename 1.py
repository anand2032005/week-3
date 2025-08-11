import os

pid = os.fork()

if pid == 0:
    print(f"Hello from the child! PID = {os.getpid()}, Parent PID = {os.getppid()}")
else:
    print(f"Hello from the parent! PID = {os.getpid()}, Child = {pid}" )
