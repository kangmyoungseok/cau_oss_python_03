'''
width 와 height 값을 가지는 클래스 line과
직사각형, 타원, 직각삼각형의 넓이를 구하는 함수들을 정의한 모듈
'''

import math

class line:
    """line class
    선들의 길이를 저장하는 클래스

    Attributes:
        __width: 선의 넓이
        __height: 선의 높이
    
    Methods:
        get_length: 선의 넓이와 높이를 반환
        set_length: 선의 넓이와 높이를 설정
    """
    __width,__height = 0,0

    def __init__(self, __width, __height):
        self.__width = __width
        self.__height = __height

    def get_length(self):
        return self.__width,self.__height
    
    def set_length(self,__width,__height):
        self.__width = __width
        self.__height = __height

def check_value(width,height):
    """check_value
    width와 height가 0보다 작거나 같으면 ValueError를 발생시킨다.

    Args:
        width: 넓이
        height: 높이

    Raises:
        ValueError: width와 height가 0보다 작거나 같을 때 발생
    """
    if width <= 0 or height <= 0:
        raise ValueError

def area_rectangle(width, height):
    """area_rectangle
    width와 height를 매개변수로 받아, width * height의 직사각형의 넓이를 반환한다.

    Args:
        width: 넓이
        height: 높이

    Returns:
        width * height: 직사각형의 넓이        
    """
    check_value(width,height)
    return width * height

def area_ellipse(width,height):
    """area_ellipse
    width와 height를 매개변수로 받아, width * height * pi의 타원의 넓이를 반환한다.

    Args:
        width: 넓이
        height: 높이

    Returns:
        width * height * pi: 타원의 넓이
    """
    check_value(width,height)
    return width * height * math.pi

def area_right_triangle(width,height):
    """area_right_triangle
    width와 height를 매개변수로 받아, width * height / 2의 직각삼각형의 넓이를 반환한다.

    Args:
        width: 넓이
        height: 높이
    
    Returns:
        width * height / 2: 직각삼각형의 넓이
    """
    check_value(width,height)
    return width * height / 2