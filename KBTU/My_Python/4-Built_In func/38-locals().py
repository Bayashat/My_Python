##################  38.locals()

'''
The locals() function returns the local symbol table as a dictionary.

A symbol table contains necessary information about the current program.

# Syntax:

locals()

'''

'''
*********************************************************************************************************************
'''


# Ex-1: Dispaly the local symbol table:

x = locals()
print(x)    # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001E50C5AB460>,
            #  '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'E:\\KBTU\\PP\\1.py', '__cached__': None, 
            # 'x': {...}}

# Ex-2: Get the filename of the current program:

x = locals()
print(x["__file__"])    # # E:\KBTU\PP\Phyton\Week-5(Built-In func)\38-locals().py
