
import Api_mikrotik as api

exitFlag= 1

while (exitFlag!=0):
    print('1. Enter simple queue options \n 2. Enter System options')
    option = input()
    if(option==1):
        print('1. Get simple queue list \n 2. Set simple queue')
        option_queue = input()
        if(option_queue==1):
            api.get_simple_queue() 