from Api_mikrotik import Mikrotik



if __name__ == "__main__":
    MIKROTIK = Mikrotik()
    print('Que desea Haver?')
    print('1: mostrar configuraciones del sistema')
    print('2: mostrar cola simple')
    response = int(input())
    if response == 1:
        for x in MIKROTIK.get_system_attributes():
            print(x)
    
    else:
        for x in MIKROTIK.get_simple_queue():
            print(x)
