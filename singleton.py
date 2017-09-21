"""
    Create a singleton Design Pattern class following the Borg DP
"""

class Singleton(object):
    """Singleton class"""
    __shared_state = {}

    def __init__(self, **kwargs):
        self.__dict__ = self.__shared_state
        self.__shared_state.update(kwargs)

    def __str__(self):
        return str(self.__shared_state)


param = Singleton(VT='Virginia Tech')

print(param)
print(param.VT)

y = Singleton(MSS='MolSSI software scientist')

print(param.MSS)
