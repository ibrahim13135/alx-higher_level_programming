#!/usr/bin/python3
#def uppercase(str):
def uppercase(str):
        for c in str:
                if ord(c) >= 65 and ord(c) <= 90:
                        return(True)
                else:
                        return(False)
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")
