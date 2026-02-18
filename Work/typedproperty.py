

def typedproperty(propa, expected_type):

    private_propa = '_' + propa

    @property
    def prop(self):
        return getattr(self, private_propa)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type) or (isinstance(value, (int, float)) and value < 0):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_propa, value)

    return prop




String = lambda t_prop: typedproperty(t_prop, str)
Integer = lambda t_prop: typedproperty(t_prop, int)
Float = lambda t_prop: typedproperty(t_prop, float)

