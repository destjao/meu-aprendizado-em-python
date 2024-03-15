def soma(*args, **kwargs):
    print(sum(args*kwargs))
    print(kwargs)

soma(1,kwargs=3)