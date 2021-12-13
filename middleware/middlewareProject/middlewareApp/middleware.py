class  MiddleWareLifeCycle:
    def __init__(self, get_response) :
        print('INIT METhoD')
        self.get_response=get_response

    def __call__(self,request):
        print('before the view is executed')
        response= self.get_response(request)
        print('after the view is executed')

        return response

class  MiddleTest:
    def __init__(self, get_response) :
        print('INIT METhoD')
        self.get_response=get_response

    def __call__(self,request):
        print('before the view is executed')
        response= self.get_response(request)# next middleware ma janx last middleware ho vane view ma janx
        print('after the view is executed')

        return response