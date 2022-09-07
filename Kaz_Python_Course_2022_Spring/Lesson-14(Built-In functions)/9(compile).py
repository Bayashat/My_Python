'''
compile()	Returns the specified source as an object, ready to be executed

compile(source, filename, mode)

source  --  Required. Can be a String, Bytes, Object

Filename    -- Required. The name of the file that source comes from. If the source does not comes from a file, you can write whatever you like

Mode    --  Required, 
    eval    - if the source is a string expression
    exec    - if the source is a blick of statements
'''
x = compile('print(45)','test',"eval")
exec(x)


x = compile("print(55)\nprint(88)", "test", "exec")
exec(x)