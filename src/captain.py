#! python3

class Captain():
    def __init__(self, name:str):
        self._name = name

    @property
    def name(self):
        return self._name


if __name__ == '__main__':
    c = Captain(name='Abraham')
    print("Hi " + c.name)
