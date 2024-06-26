# Synchronous cooking
# 1 kitchen 1 chefs 1 dish
from time import sleep, ctime, time

#cooking synchronous 
def cooking(index):
    print(f'{ctime()} Kitchen-{index} : Begin cooking...')
    sleep(2)
    print(f'{ctime()} Kitchen-{index} : Cooking done!...')

if __name__=="__main__":
    #Begin of main thread
    print(f'{ctime()} Main : Start cooking.')
    start_time = time() #จับเวลาในบรรทัดที่ 14 
    #Cooking
    cooking(0)

    duration = time() - start_time
    print(f'{ctime()} Main : Finished cooking duration in {duration:0.2f} second')