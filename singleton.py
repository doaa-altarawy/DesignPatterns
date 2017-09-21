"""
    Create a singleton Design Pattern class following the Borg DP
"""

class Singleton(object):
    """Singleton class"""
    _shared_data = {} # shared dictionary

    def __init__(self, **kwargs):
        self.__dict__ = self._shared_data
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


param = Singleton(VT='Virginia Tech')

print(param)
print(param.VT)

y = Singleton(MSS='MolSSI software scientist')

print(param.MSS)
