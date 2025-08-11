import os

pid = os.fork()

if pid == 0:
    print(f"Child: PID={os.getpid()}, Parent PID={os.getppid()}")
else:
    print(f"Parent: PID={os.getpid()}, waiting for child {pid}")
    finished_pid, status = os.wait()
    print(f"Parent: Child {finished_pid} finished with status {status}")
