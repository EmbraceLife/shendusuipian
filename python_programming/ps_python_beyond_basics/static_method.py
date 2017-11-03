class Class_Instance_Attributes:
    next_id_number = 100

    def __init__(self, identity, job):
        self.id = identity
        self.job = job
        self.id_number = Class_Instance_Attributes.next_id_number # 调用class attributes
        # 修改class attributes
        Class_Instance_Attributes.next_id_number+=1

ca1 = Class_Instance_Attributes('py2.7', 'basics')
ca1.id
ca1.id_number
ca1.job
ca1.next_id_number
Class_Instance_Attributes.next_id_number

class Class_Instance_Attributes:
    next_id_number = 100

    def _get_next_id_number(self): # label it for no public use
        result = Class_Instance_Attributes.next_id_number
        Class_Instance_Attributes.next_id_number+=1
        return result

    def __init__(self, identity, job):
        self.id = identity
        self.job = job
        self.id_number = self._get_next_id_number()

ca1 = Class_Instance_Attributes('py2.7', 'basics')
ca1.id
ca1.id_number
ca1.job
ca1.next_id_number
ca1._get_next_id_number()
Class_Instance_Attributes._get_next_id_number(ca1)
dir(Class_Instance_Attributes)

# add object method only for implementation details not for public use
class Class_Instance_Attributes:
    next_id_number = 100 # class attri

    @staticmethod
    def _get_next_id_number(): # no self is needed
        print("using super class staticmethod")
        result = Class_Instance_Attributes.next_id_number
        Class_Instance_Attributes.next_id_number+=1
        # print(self.id) # can't access self or instance here
        return result

    def __init__(self, identity, job):
        self.id = identity
        self.job = job
        self.id_number = Class_Instance_Attributes._get_next_id_number()

ca1 = Class_Instance_Attributes("py", "all")
id(ca1)
ca1.id
ca1.job
ca1.id_number
ca1.next_id_number
Class_Instance_Attributes.next_id_number
ca1._get_next_id_number()
ca1._get_next_id_number()
Class_Instance_Attributes._get_next_id_number()
###################
# staticmethod inheritance
class Class_Instance_Attributes:
    next_id_number = 100 # class attri

    @staticmethod
    def _get_next_id_number(): # no self is needed
        print("using super class staticmethod")
        result = Class_Instance_Attributes.next_id_number
        Class_Instance_Attributes.next_id_number+=1
        # print(self.id) # can't access self or instance here
        return result

    def __init__(self, identity, job):
        self.id = identity
        self.job = job
        self.id_number = Class_Instance_Attributes._get_next_id_number()

class SubClass(Class_Instance_Attributes):# inherit everything from superclass
    @staticmethod
    def _get_next_id_number(): # overwrite statimethod
        print("using subclass staticmethod")
        result = SubClass.next_id_number
        SubClass.next_id_number+=1
        return result+1
# subclass staticmethod is not used
ca2 = SubClass('py3', "more")

class Class_Instance_Attributes:
    next_id_number = 100 # class attri

    @staticmethod
    def _get_next_id_number(): # no self is needed
        print("using super class staticmethod")
        result = Class_Instance_Attributes.next_id_number
        Class_Instance_Attributes.next_id_number+=1
        # print(self.id) # can't access self or instance here
        return result

    def __init__(self, identity, job):
        self.id = identity
        self.job = job
        self.id_number = self._get_next_id_number()
        # self._get_next_id_number is key to use subclass staticmethod

class SubClass(Class_Instance_Attributes):

    @staticmethod
    def _get_next_id_number():
        print("using subclass staticmethod")
        result = SubClass.next_id_number
        SubClass.next_id_number+=1
        return result+1

ca2 = SubClass('py3', "more")


########################
# class method
class Class_Instance_Attributes:
    next_id_number = 100 # class attri

    @classmethod
    def _get_next_id_number(cls): # now use cls as args
        result = cls.next_id_number
        cls.next_id_number+=1
        return result

    @classmethod
    def create_empty(cls, identity):
        return cls(identity, job=None)

    def __init__(self, identity, job):
        self.id = identity
        self.job = job
        self.id_number = Class_Instance_Attributes._get_next_id_number()
ca1 = Class_Instance_Attributes('py5', 'DL')
ca1.id
ca1.job
ca1.id_number
ca1.next_id_number
Class_Instance_Attributes.next_id_number
Class_Instance_Attributes.create_empty("py5")
ca1._get_next_id_number()
Class_Instance_Attributes._get_next_id_number()
ca1._get_next_id_number
