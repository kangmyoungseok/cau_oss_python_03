'''
width 와 height 값을 가지는 클래스 line과
직사각형, 타원, 직각삼각형의 넓이를 구하는 함수들을 정의한 모듈
'''

import math

class line:
    '''넓이(__width)와 높이(__height)변수 존재'''
    __width,__height = 0,0

    def __init__(self, __width, __height):
        '''넓이(__width)와 높이(__height) 초기화'''
        self.__width = __width
        self.__height = __height

    def get_length(self):
        '''넓이(__width)와 높이(__height) 반환'''
        return self.__width,self.__height
    
    def set_length(self,__width,__height):
        '''길이(length)를 설정'''
        self.__width = __width
        self.__height = __height

def check_value(width,height):
    ''' width와 height 값이 0 이하일 경우 ValueError를 발생'''
    if width <= 0 or height <= 0:
        raise ValueError

def area_rectangle(width, height):
    ''' width와 height를 매개변수로 받아, width * height의 직사각형의 넓이를 반환한다.'''
    check_value(width,height)
    return width * height

def area_ellipse(width,height):
    ''' width와 height를 매개변수로 받아, width * height * pi의 타원의 넓이를 반환한다.'''
    check_value(width,height)
    return width * height * math.pi

def area_right_triangle(width,height):
    ''' width와 height를 매개변수로 받아, width * height / 2의 직각삼각형의 넓이를 반환한다.'''
    check_value(width,height)
    return width * height / 2