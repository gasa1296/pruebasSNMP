import routeros_api

host = '192.168.1.1'

connection = routeros_api.RouterOsApiPool(
    host,
    username='admin',
    password=''
)
api = connection.get_api()

#api.get_binary_resource('/').call('<resource>',{ <dict of params> })
#list = api.get_resource('/command')
#list_queues = api.get_resource('/queue/simple')
#list_queues.get()
#list.add(attribute="vale", attribute_n="value")
#list.set(id, attributes)
#list.get(attribute=value)
#list.remove(id)
#connection.disconnect()

get = api.get_resource('/system/package/')
out = get.call('getall')
for o in out:
    print(o)
