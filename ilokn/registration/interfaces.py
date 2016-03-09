from zope.interface import Interface

class IProductSpecific(Interface):
    pass

class IUserApprovedEvent(Interface):
    pass

class IUserRejectedEvent(Interface):
    pass

class IUserRegisteredEvent(Interface):
    pass

class IRegistrationApproval(Interface):

    def get(key):
        pass

    def add(key, data):
        pass

    def approve(key):
        pass

    def reject(key):
        pass
