#!/usr/bin/python3
"""Module: Locked class"""
class LockedClass:
    """
    Class: LockedClass
    """
    def __setattr__(self, name, value):
         """
        Set instance attribute 'name' to 'value' if 'name' is 'first_name'.
        Raise an AttributeError for any other attribute.

        Args:
            name (str): The name of the attribute being set.
            value: The value to set the attribute to.

        Raises:
            AttributeError: If 'name' is not 'first_name'.
        """
        if name == "first_name":
            self.__dict__[name] = value

        else:
            raise AttributeError(f"can not set attribute '{name}'")
