import multiprocessing
import time
from subprocess import DEVNULL, call


def start_ethereum():
    call(["geth","--dev","--ipcpath","~/Library/Ethereum/geth.ipc"],stderr=DEVNULL,stdout=DEVNULL)

def start_ipfs():
    call(["ipfs","daemon"],stderr=DEVNULL,stdout=DEVNULL)

def start_dashboard():
    call(["python3","/Users/manan/Documents/BlockIoT/Code/new_BlockIoT/dashboard.py"],stderr=DEVNULL,stdout=DEVNULL)
def start_main():
    call(["python3","/Users/manan/Documents/BlockIoT/Code/new_BlockIoT/main.py"])
if __name__ == '__main__':
    p = multiprocessing.Process(target=start_ethereum)
    p.start()
    time.sleep(5)
    print("Ethereum Started")
    p = multiprocessing.Process(target=start_ipfs)
    p.start()
    time.sleep(5)
    print("IPFS Started")
    p = multiprocessing.Process(target=start_main)
    p.start()
    time.sleep(1)
    p.terminate()
    print("finish")
    p = multiprocessing.Process(target=start_main)
    p.start()
    time.sleep(1)
    p.terminate()
    print("finish")
    p = multiprocessing.Process(target=start_main)
    p.start()
    time.sleep(1)