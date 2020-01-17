import routeros_api
host = '192.168.1.1'
username = 'admin'
password = ''

def connect ():
    connection = routeros_api.RouterOsApiPool(host,username,password)
    return connection.get_api()

#api.get_binary_resource('/').call('<resource>',{ <dict of params> })
#list = api.get_resource('/command')
#list_queues = api.get_resource('/queue/simple')
#list_queues.get()
#list.add(attribute="vale", attribute_n="value")
#list.set(id, attributes)
#list.get(attribute=value)
#list.remove(id)
#connection.disconnect()

def reset_router():
    api = connect()
    print('reseteando router')
    resource = api.get_resource('/system/')
    resource.call('reboot')

def set_simple_queue(name_assigned,
        max_limit_assigned, target_assigned):
    api = connect()
    queue = api.get_resource('/queue/simple')
    queue.add(name=name_assigned, max_limit=max_limit_assigned, target=target_assigned)

# TODO set attributes according which attribute user wants to update.
def update_simple_queue(id_assigned,
        max_limit_assigned, target_assigned):
    api = connect()
    queue = api.get_resource('/queue/simple')
    queue.set(id=id_assigned, max_limit=max_limit_assigned, target=target_assigned)

def get_simple_queue():
    api = connect()
    list_queues = api.get_resource('/queue/simple')
    list_queues.get()


""" get = api.get_resource('/system/package/')
out = get.call('getall')
for o in out:
    print(o) """
