from pysnmp.hlapi import *

# original sysName  MikroTik
COMMUNITY = CommunityData('public')
TARGET = UdpTransportTarget(('demo.snmplabs.com', 162)
#COMMUNITY = CommunityData('desarrollo', mpModel=1)
#TARGET = UdpTransportTarget(('192.168.1.1', 161))

def getRouter(community, target):
    objectType = ObjectType(ObjectIdentity( 'SNMPv2-MIB', 'sysName',0))
    errorIndication, errorStatus, errorIndex, varBinds = next(getCmd(SnmpEngine(), community, target, ContextData(), objectType))


    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))

def setRouter(community, target):
    objectType = ObjectType(ObjectIdentity(
        'SNMPv2-MIB', 'sysName'), 'desarrollo')
    command = setCmd(SnmpEngine(), COMMUNITY, TARGET, ContextData(), objectType)
    print(next(command))
    getRouter(community, target)
    
def getAllMIB (community, target):
    objectType = ObjectType(ObjectIdentity( 'SNMPv2-MIB', 'sysName' ))
    for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(SnmpEngine(), community, target, ContextData(), objectType):
        if errorIndication or errorStatus:
            print(errorIndication or errorStatus)
            print(errorIndex)
            break
        else:
            for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))

setRouter(COMMUNITY, TARGET)
