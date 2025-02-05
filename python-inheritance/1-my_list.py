#!/usr/bin/python3
"""
modulo documentado
"""


class MyList(list):
    """
    class MyList that inherits frm list
    """
    def print_sorted(self):
        print(sorted(self))
