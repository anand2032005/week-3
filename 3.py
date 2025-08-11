import os

pid = os.fork()

if pid == 0:
    # Child: replace itself with `ls`
    os.execlp("ls", "ls", "-l")
else:
    # Parent: wait for child
    os.wait()
    print("Parent finished waiting")
