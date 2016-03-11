from zope.interface import Interface
from zope import schema

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
    
class IExtendRegistrationForm(Interface):
    """Marker interface for my custom registration form
    """


class ExtendRegistrationForm(Interface):
    
    kn_jobtitle = schema.TextLine(
        title=(u'Job Title'),
        description=u'',
        required=False,
        )
    
    kn_organization = schema.TextLine(
        title=(u'Job Organization'),
        description=u'',
        required=False,
        )
