def i_am_decorator(func_to_decorate):
    def decoration():
        print("Hi i am a decorator. My name is Anuvrat")
        func_to_decorate()
        print("Ok. I'll decorate you")

    return decoration


@i_am_decorator
def normal_func():
    print("I want to be decorated Anuvrat")


normal_func()