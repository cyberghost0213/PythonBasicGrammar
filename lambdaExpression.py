# 람다 표현식을 변수에 할당해서 사용하기
# >>> plus_ten = lambda x: x + 10
# >>> plus_ten(1)
# 11

# 람다 표현식 자체를 호출하기
# >>> (lambda x: x + 10)(1)
# 11

# 람다 표현식 안에서는 변수 생성 불가능
# 람다 표현식 바깥에 있는 변수는 사용 가능
# >>> (lambda x: y = 10; x + y)(1)
# SyntaxError: invalid syntax
#
# >>> y = 10
# >>> (lambda x: x + y)(1)
# 11

# 람다 표현식을 인수로 사용하기
# 함수의 인수부분을 간단하게 하기 위해서 람다표현식을 사용하는 경우가 많다.
# >>> def plus ten(x):
# >>>   return x +10
# >>> list(map(plus_ten, [1, 2, 3]))
# [11, 12, 13]
#
# 위의 과정을 아래와 같이 축약할 수 있다.
# >>> list(map(lambda x: x + 10, [1, 2, 3]))
# [11, 12, 13]

# 람다 표현식에 조건부 표현식을 사용하기
# >>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> list(map(lambda x: str(x) if x % 3 == 0 else x, a))
# [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]
#
# 람다 표현식에서는 elif을 사용할 수 없다.
# if를 연속으로 사용해야한다.
# >>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
# ['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]

# map 객체를 여러 개 넣기
# map은 리스트 등의 반복 가능한 객체를 여러 개 넣을 수 있다.
# >>> a = [1, 2, 3, 4, 5]
# >>> b = [2, 4, 6, 8, 10]
# >>> list(map(lambda x, y: x * y, a, b))
# [2, 8, 18, 32, 50]

# filter 사용하기
# >>> def f(x):
# >>>  return x > 5 and x < 10
# >>> a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
# >>> list(filter(f, a))
# [8, 7, 9]
# 
# 위의 과정을 아래와 같이 축약 할 수 있다.
# >>> a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
# >>>list(filter(lambda x: x > 5 and x < 10, a)) 
# [8, 7, 9]

# reduce 사용하기
# >>> def f(x, y):
# >>>   return x + y
# >>> a = [1, 2, 3, 4, 5]
# >>> from functools import reduce
# >>> reduce(f, a)
# 15 
#
# 위의 과정을 아래와 같이 축약 할 수 있다.
# >>> a = [1, 2, 3, 4, 5]
# >>> from functools import reduce
# >>> reduce(lambda x, y: x + y, a)
# 15