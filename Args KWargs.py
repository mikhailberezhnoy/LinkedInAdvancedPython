
def f1(p1, p2 , p3, *args, **kwargs):
    print (p1, p2, p3)
    for x, y in enumerate(args):
        print (f'{x}-->{y}')
    print (kwargs)




f1 (1,4, 7, 9,19,29, kwarg1=100, kwarg2=200)
