class Base:
    # ...

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            raise TypeError('create() can only be called on Rectangle or Square')
        dummy.update(**dictionary)
        return dummy
