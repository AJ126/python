def fun(**kwargs):
    # when we take **kwargs it is a keyword argument , we can no of arguments and all these arguments are store in dictionary
    # we can take no of  key value pair using this 
    print(kwargs)
    print(type(kwargs))
fun(name='shiv',rollno=1,address='kailash')
fun(mobileno=8888888888,id=2)
