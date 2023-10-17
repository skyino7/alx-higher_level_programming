#!/usr/bin/python3
"""_
Module Doc
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class Doc
    inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for size Doc
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size Doc
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        __str__ Doc
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """
        to_dict doc
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y,
        }

    def update(self, *args, **kwargs):
        """
        update Doc
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def create(cls, *args, **kwargs):
        """
        create doc
        """
        return cls(*args, **kwargs)
