#############  26.globals()

'''
The globals() function returns the global symbol table as a dictionary.

A symbol table contains necessary information about the current program

# Syntax:
globals()

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Display the global symbol table:

x = globals()
print(x)    # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x02A8C2D0>, 
            # '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'demo_ref_globals.py', '__cached__': None,
            #  'x'_ {...}}


# Ex-2: Get the filename of the current program:

x = globals()
print(x["__file__"])    # E:\KBTU\PP\Phyton\Week-5(Built-In func)\26-globals().py

