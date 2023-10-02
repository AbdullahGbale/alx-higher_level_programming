#!/usr/bin/python3
       """Defines object attribute lookup function."""


def lookup(obj):
      """Return a list of object's available attributes.
      Args:
          obj: object whose attributes we are looking for
        """
    attr_meth = dir(obj)
    avail = [item for item in attr_meth]
    return avail
