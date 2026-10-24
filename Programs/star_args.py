def fun1(*args):
    # when we take *args it means we can take no of arguments and all these arguments save intuple
    print(args)
    print()
    print(type(args))
fun1(10)
fun1(10,20,30,40,50)
fun1(10,20,30,40,50,60,70)
