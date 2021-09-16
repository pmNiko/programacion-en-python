def uppercase(f):
    """ Dada una función f que devuelve un string lo pasa todo a mayúsculas """
    def wrapper():
        return f().upper()
    return wrapper


def make_bold(f):
    """ Dada una función f que devuelve un string le añade los tags de bold """
    def wrapper():
        return '\033[1m' + f()
    return wrapper


if __name__ == "__main__":
    @make_bold
    @uppercase
    def sayHello():
        return "Hello world"

    print(sayHello())
