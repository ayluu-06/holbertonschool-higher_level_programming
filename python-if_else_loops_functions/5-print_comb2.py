#!/usr/bin/python3
print(*("{:02}".format(i) for i in range(100)), sep=", ")
