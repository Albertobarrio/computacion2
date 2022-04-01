import os
import time
def main():
    if os.fork() == 0:
        time.sleep(2)
        print("hola soy el hijo", os.getpid())
    else:
        print("hola soy el padre", os.getpid())
        os.wait()
if __name__ == "__main__":
    main()
