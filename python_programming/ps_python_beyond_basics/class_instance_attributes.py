class Class_Instance_Attributes:
    next_id_number = 100 # class attri

    def __init__(self, identity, job):
        self.id = identity
        self.job = job
        self.id_number = Class_Instance_Attributes.next_id_number # how to address class attri
        # self refer to object instance
        Class_Instance_Attributes.next_id_number+=1
Class_Instance_Attributes.__class__
ca1.__class__
ca1 = Class_Instance_Attributes("py", "all")
id(ca1)
ca1.id
ca1.job
ca1.id_number
ca1.next_id_number
Class_Instance_Attributes.next_id_number
dir(Class_Instance_Attributes)
dir(ca1)
ca2 = Class_Instance_Attributes('py3','all+MLDL')
id(ca2)
ca2.id
ca2.job
ca2.id_number
ca2.next_id_number
Class_Instance_Attributes.next_id_number
ca2.__init__
ca2.__init__("py4", "unknown new tech")
ca2.next_id_number
ca2.id
ca2.job
ca2.id_number
id(ca2)
