def _merge(str, str2):
    return str + ' ' + str2


def hello(name='function'):
    return 'hello ' + name


class User:
    def hello(self, name='class function'):
        return 'hello ' + name


defaultUser = User()
defaultName = 'defUser'
_value = 0
