# Author : UnoHwang

# 2.6.1 모듈
# 모듈이란 : 함수 정의, 클래스 등 파이썬 문장들을 담고 있는 파일
#        : .py 확장자를 갖는 파일 모두
# 패키지  : 여러 모듈(.py 파일)을 특정 디렉터리에 모아 놓은 것
​
######## help 모듈 #############
# help('modules') # 현재 PC에 설치된 모듈 목록
# help('pandas') /# pandas 모듈 상세 설명
​
######## import ~ ###########
# import 모듈명 or import 패키지명.모듈명
# import keyword
# print(keyword.kwlist)
​
# import random
# a = random.randint(1, 10)
# b = random.randrange(1, 10, 3)
# print(a,b)
# # randint(1,10) : 1~10중에서 임의의 값
# # randrange : 1,4,7 중에서 임의의 값(10을 포함하지 않는다.)
# print(help('random.randrange'))
​
######## from ~ import ~ ##########
# from 패키지명 import 모듈명
# from 모듈명 import 클래스명, 함수명
​
from random import randint
# a = randint(1, 10)
# # b = randrange(1, 10, 3)
# print(a)
# print(b)
​
# from random import *
# a = randint(1, 10)
# b = randrange(1, 10, 3)
# print(a)
# print(b)
​
# ####### (from ~) import ~ as ##########
# import random as rd
# a = rd.randint(1, 10)
# b = rd.randrange(1, 10, 3)
# print(a,b)
​
# from random import randint as rdi
# a = rdi(1, 10)
# print(a)
​
####### __file__ ########
# import random
# print(random.__file__)
​
​
# 2.6.2 패키지
# import urllib.request
# print(type(urllib.request))
# print(type(urllib))
# 패키지도 모듈의 일부, 경로 속성을 갖기 때문에 패키지라 부른다.
# print(urllib.__path__)
# print(urllib.request.__path__)
​
​
# import 패키지명.모듈이나 패키지 O
# import 패키지명.클래스나 함수 X
# from 패키지명.모듈 import 클래스나 함수 O
​
######## __all__ ##########
# from 패키지명 import * 을 하게되면 패키지에 속한 모듈은 사용할 수 없다.
# import TestFolder.test1
# testp = TestFolder.test1.test1package()
# testp.detail()
#
# from TestFolder import test1
# testp = test1.test1package()
# testp.detail()
#
# from TestFolder import *
# testp = test1.test1package()
# testp.detail()
# # __init__.py 에다가 __all__ 입력 -> 사용가능
#
​
####### __init__.py #############
# # __init__.py : 패키지 초기화 파일
# 패키지 내의 모든 모듈에서 공통적으로 사용할 속성이 있다면 패키지 초기화 파일에 정의
#
###### terminal pip #############
# # 터미널에서 pip list : 현재 설치된 패키지
# # 터미널에서 pip show 패키지 : 패키지 정보
# # 터미널에서 pip install --upgrade 패키지명
# 패키지 오른쪽버튼 - Show in Explorer 위치탐색기 실행, 경로 이동 가능
​
# import inspect
# import pandas
# print(inspect.getfile(pandas))
