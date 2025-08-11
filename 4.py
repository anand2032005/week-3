import os
import sys

pid = os.fork()

if pid == 0:
    # Child process
    print(f"Child: PID={os.getpid()}, running 'date'...", flush=True)
    try:
        os.execlp("date", "date")  # replace with 'date' command
    except FileNotFoundError:
        print("Child: 'date' command not found!", flush=True)
        os._exit(1)  # exit with error
else:
    # Parent process
    print(f"Parent: PID={os.getpid()}, waiting for child {pid}...", flush=True)
    finished_pid, status = os.waitpid(pid, 0)
    exit_code = status >> 8
    print(f"Parent: Child {finished_pid} exited with code {exit_code}")
