import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_PathcompserviceUuidLabelValuenameImpl:

    @classmethod
    def put(cls, uuid, valueName, nameandvalue):
        print str(nameandvalue)
        print 'handling put'
        if uuid in Context._pathCompService:
            Context._pathCompService[uuid].label[valueName] = nameandvalue
        else:
            raise KeyError('valueName')

    @classmethod
    def post(cls, uuid, valueName, nameandvalue):
        print str(nameandvalue)
        print 'handling post'
        if uuid in Context._pathCompService:
            Context._pathCompService[uuid].label[valueName] = nameandvalue
        else:
            raise KeyError('valueName')

    @classmethod
    def delete(cls, uuid, valueName):
        print 'handling delete'
        if uuid in Context._pathCompService:
            if valueName in Context._pathCompService[uuid].label:
                del Context._pathCompService[uuid].label[valueName]
            else:
                raise KeyError('valueName')
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid, valueName):
        print 'handling get'
        if uuid in Context._pathCompService:
            if valueName in Context._pathCompService[uuid].label:
                return Context._pathCompService[uuid].label[valueName]
            else:
                raise KeyError('valueName')
        else:
            raise KeyError('uuid')
