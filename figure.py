import math

class line:
    '''길이(length)를 가지는 선분'''
    __length = 0

    def __init__(self, length):
        '''길이(length)를 초기화'''
        self.__length = length

    def get_length(self):
        '''길이(length)를 반환'''
        return self.__length
    
    def set_length(self,length):
        '''길이(length)를 설정'''
        self.__length = length

def area_square(length):
    '''length * length 의 정사각형 넓이를 반환'''
    return length * length

def area_circle(length):
    '''3.14 * length * length * pi 의 원의 넓이를 반환'''
    return length * length * math.pi

def area_regular_triangle(length):
    '''length * length * math.sqrt(3) / 4 의 정삼각형 넓이를 반환'''
    return length * length * math.sqrt(3) / 4