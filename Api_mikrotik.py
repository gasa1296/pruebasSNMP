import routeros_api

#self.api.get_binary_resource('/').call('<resource>',{ <dict of params> })
#list = self.api.get_resource('/command')
#list_queues = self.api.get_resource('/queue/simple')
#list_queues.get()
#list.add(attribute="vale", attribute_n="value")
#list.set(id, attributes)
#list.get(attribute=value)
#list.remove(id)
class Mikrotik:

    def __init__(self):
        self.__host = '192.168.1.1'
        self.__username = 'admin'
        self.__password = ''
        self.__connection = routeros_api.RouterOsApiPool(self.__host, self.__username, self.__password)
        self.__api = self.__connection.get_api()

    def reset_router(self):
        print('reseteando router')
        resource = self.__api.get_resource('/system/')
        resource.call('reboot')

    def set_simple_queue(self, target_assigned, name_assigned = None,
            max_limit_assigned = None):
        queue = self.__api.get_resource('/queue/simple')
        queue.add(name=name_assigned, max_limit=max_limit_assigned, target=target_assigned)

    # TODO set attributes according which attribute user wants to update.
    def update_simple_queue(self, target_assigned, id_assigned=None,
            max_limit_assigned = None):
        queue = self.__api.get_resource('/queue/simple')
        queue.set(id=id_assigned, max_limit=max_limit_assigned, target=target_assigned)

    def get_simple_queue(self):
        list_queues = self.__api.get_resource('/queue/simple')
        return list_queues.get()

    def get_system_attributes(self):
        get = self.__api.get_resource('/system/package/')
        return get.call('getall')

    def disconnect(self):
        self.__connection.disconnect()

