# # 숫자
# print(5)
# print(-10)
# print(3.14)
# print(5+3)
# print(2*8)
# print(3*(3+1))

# # 문자열
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9) # ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 과 같은 결과

# # boolean 자료형
# # 참 / 거짓
# print(5 > 10) # False
# print(5 < 10) # True
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))

# # 변수 : 애완동물을 소개
# animal = "고양이" #"강아지"
# name = "해피" #"연탄이"
# age = 3 #4
# hobby = "낮잠" #"산책"
# isAdult = age >= 3

# print("우리집 " + animal + "의 이름은 " + name + "에요~")
# hobby = "공놀이"
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요.")
# print(name, "는 ", str(age), "살이며, ", hobby, "을 아주 좋아해요.")    # , 일 경우는 스페이스가 한 칸씩 들어간다.
# print(name + "는 어른일까요? " + str(isAdult))

# 주석

# '#'은 한 문장을 주석처리합니다.

'''
이렇게 하면 
여러 문장이
주석 처리가 됩니다.
'''

# # 퀴즈
# stationName = "사당"        
# print(stationName + " 행 열차가 들어오고 있습니다.")
# stationName = "신도림"
# print(stationName + " 행 열차가 들어오고 있습니다.")
# stationName = "인천공항"
# print(stationName + " 행 열차가 들어오고 있습니다.")

# # 연산
# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)

# print(2**3)     # 2^3 (2의 3승)
# print(5%3)      # 나머지 구하기
# print(10%3)     # 나머지 구하기
# print(5//3)     # 몫 구하기 (정수로 구하기)
# print(10/3)     # 몫 구하기 (소숫점 아래까지 자세히 구하기)

# print(5 > 3)    # True
# print(4 >= 7)   # False
# print(10 < 3)   # False
# print(5 <= 5)   # True

# print(3 == 3)   # True
# print(4 == 2)   # False
# print(3 + 4 == 7)   # True

# print(1 != 3)   # True
# print(not(1 != 3))  # False

# print((3 > 0) and (3 < 5))  # True
# print((3 > 0) & (3 < 5))    # True
# print((3 > 0) or (3 > 5))   # True
# print((3 > 0) | (3 > 5))    # True

# print(5 > 4 > 3)    # True
# print(5 > 4 > 7)    # False

# # 간단한 수식
# print(2 + 3 * 4)    # 12
# print((2 + 3) * 4)  # 20
# number = 2 + 3 * 4  # 14
# print(number)
# number = number + 2 # 16
# print(number)
# number += 2         # 18
# print(number)
# number *= 2         # 36
# print(number)
# number /= 2         # 18
# print(number)
# number -= 2         # 16
# print(number)

# number %= 2         # 0, 자기를 2로 나누고 나머지 값을 저장한다.
# print(number)
# number %= 5         # 1, 상동
# print(number)

# # 숫자 처리 함수
# print(abs(-5))      # 5
# print(pow(4, 2))    # 4^2 = 16 4**2 와도 같은 의미
# print(max(5, 12))   # 12
# print(min(5, 12))   # 5
# print(round(3.14))  # 3, 올림 또는 버림 하는 함수이고 .14는 버린다.
# print(round(4.99))  # 5  올림 또는 버림 하는 함수이고 .99는 올린다.

# from math import *
# print(floor(4.99))  # 4, 이는 무조건 소수점 이하는 버림.
# print(ceil(3.14))   # 4, 이는 무조건 소수점 이하는 올림.
# print(sqrt(16))     # 제곱근. 4

# # 랜덤 함수
# from random import *

# print(random())             # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10)        # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10))   # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10)+1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10)+1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10)+1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10)+1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10)+1) # 1 ~ 10 이하의 임의의 값 생성

# print(int(random() * 45)+1)  # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45)+1)  # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45)+1)  # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45)+1)  # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45)+1)  # 1 ~ 45 이하의 임의의 값 생성

# print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성

# print(randint(1, 45))   # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45))   # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45))   # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45))   # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45))   # 1 ~ 45 이하의 임의의 값 생성

# # 퀴즈
# print(randint(4, 45))   # 1 ~ 45 이하의 임의의 값 생성
# print("오프라인 스터디 모임 날짜는 매월 " + str(randint(4, 28)) + " 일로 선정되었습니다.")

# # 문자열
# sentence = "Genius"
# print(sentence)
# sentence2 = "Predlojenie"
# print(sentence2)
# # " " 안에서의 "" 은 줄바꿈 문자이다.
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

#Sentence vol.2
# sentence3 = "`"
# print(sentence3)

# # 슬라이싱
# jumin = "123456-2345678"

# jumin kakoito
# from curses import color_content


# jumin = "123456-2345678"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])  # 0부터 2직전까지 (0, 1)
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6]) # 앞에 0을 쓰지 않아도 처음부터 6 직전까지라는 의미
# print("뒤 7자리 : " + jumin[7:]) # 뒤에 14를 쓰지 않아도 7부터 끝까지라는 의미
# print("뒤 7자리(뒤에서부터) :" + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지


# print("Genius +" + jumin[7] )
# print( "ot: " + jumin[0:2])  # 0 t shaman 2 (0,1)
# print("2hug " + jumin[2:4])
# print("012: " + jumin[4:6])
# print("Geniuss"+jumin[:6]) # che-to tam 6
# print("GGG" + jumin[7:]) # 14
# print("c|T 7 :" +jumin[-7:]) #kot

# # 문자열 처리 함수
# python = "Python is amazing"
# print(python.lower())
# print(python.upper())
# print(python.isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# String Processing Function
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python.isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1) # index + 1은 앞에서 찾은 index 그 다음부터 끝까지 찾겠다는 것이고 그 다음 n을 찾을 것이다.
# print(index)

# index = python.index("n")
# print(index)
# index = python.index("n",index + 1 ) # index + 1 means to search from the index found in the previous to the end, and the next n will be searched. 
# print(index)
# print(python.find("n"))       # return 값은 index를 반환한다.
# print(python.find("Java"))    # -1 문자열을 찾지 못하면 -1을 반환한다.
# # print(python.index("Java")) # 이 문장은 에러가 나며 프로그램이 종료된다. index는 해당 문자를 찾지 못하는 경우 에러라고 처리를 한다.
# print(python.count("n"))

# # print(python.find("n"))     # The return value returns the index.
# # print(python.find("Java"))  # -1 If the string is not found, -1 is returned.
# # print(python.index("Java")) # This statement causes an error and the program terminates. If the index cannot find the corresponding character, it is treated as an error. 
# print(python.count("n")) 

# # 문자열 포멧 string format
# # 방법 1  method
# print("나는 %d살입니다." % 20)
# print("나는 %s를 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요." % "A")
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
# print("나는 %s색과 %s색을 좋아해요." % (2, "빨간")) # %를 쓰는 경우는 숫자도 문자로 인식할 수 있다.

#Method and string format
# print("I am %d years old" % 20)
# print("I like %s" % "Python")
# print("Apple starts with %c" %"A")
# print("I like %s and %s colors" % ("blue","red"))
# print("I like %s and %s colors" % ("2", "red"))   #if % used numbers also can recognized like characters

# # 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "노랑"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "노랑"))
# print("나는 {1}색과 {0}색을 좋아3해요.".format("파란", "노랑"))  # {} 안의 숫자를 임의로 변경하여 출력할 수 있다.

## Method2
# print("Мен {} jastamyn."                .format(20))
# print("I like {} and colors"             .format("Blue ","Yellow"))
# print("I like colors {0} and {1}colors"  .format("Blue ","Yellow"))
# print("I like {1} color {0}colors."      .format("blue ","yellow"))

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# # Method 3
# print("I am {age} years old,And I like the {color}.".format(age=20, color="red"))
# print("I am {age} years old,And I like the {color}".format(color="red", age=20))

# # 방법 4
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")   # f 를 쓰면 실제 사용하는 변수를 가져다가 출력할 수 있다.

## Method4
# age = 20
# color = "red"
# print(f"I {age} years old, {color} is my fav color ") # if u use f you can that is actually used print it out


# print("백문이 불여일견\n백견이 불여일타")   # 줄바꿈은 \n
# print("나는 \"나도코딩\"입니다.")        # 문장 안에서 " 은 \" 로 쓰면 된다.
# print("경로는 C:\\Test 입니다.")       # 문장 안에서 \ 은 \\ 로 쓰면 된다.

# print("Nothing was wrong \n nothing was wrong") # \n
# print("Pred \"loj\"enie.") 
# print("C:\\Test.")

# print("Red Apple\rPine")            # 문장의 제일 앞으로 가라는 것은 \r
# print("Redd\bApple")                # 백스페이스는 \b
# print("Red\tApple")                 # tab \t

# print("Red Apple\rPine") #
# print("Redd\bApple") #
# print("Red\tApple") # tab ->||<-


# 퀴즈
# http://naver.com
# 위의 문장에서 http:// 는 제외
# 처음 만나는 .이후는 제외
    # 남은 글자 중 처음 3자리
    # 글자 개수 
    # e의 개수
    # 마지막은 !로 
# 구성하는 비밀번호를 만들어라.

# url = "http://google.com"

# password = url
# index = password.rfind("/")
# password = password[index+1:]

# index = password.rfind(".")
# password = password[:index]

# first_3_char= password[:3]
# length_str  = len(password)
# count_of_e  = password.count("e")

# password = first_3_char + str(length_str) + str(count_of_e) + "!"

# print(f"{url}의 비밀번호는 {password}입니다.")

# Quiz
# http://naver.com
# Exclude http:// in the above statement
# Excluding after the first meeting
     # First 3 digits of remaining characters
     # number of characters
     # number of e
     # Last with !
# Create a configuration password. 

# url=
# print(len("google.com"))

# var = 3.1234567
# var2 = 6
# my_string = f"the variable is {var+var2} and {var2} "
# print(my_string)

# from collections import Counter
# a = "aaaaaaaaaaaabbbbccc"
# my_counter = Counter(a)
# print(my_counter.items())

# my_list = ['a'] *6
# print(my_list)
# my_string = ''.join(my_list)
# print(my_string)

# qstn = "http//naver.com"
# print(qstn[:2])

qstn = "http\\naver.com"
fst3d = qstn[5:8] 
index = qstn.count("e")
d = len(qstn)

print(f"{fst3d}{d}{index}!")

#############################
# 1:22:31 초까지 공부함. To study untill seconds
#############################

# 리스트 []

# 지하철 칸별로 10명, 20명, 39명
# subway1 = 10
# subway2 = 20
# subway3 = 30


# subway = [10, 20, 30]
# print(subway)

# subway1 = 10
# subway2 = 20
# subway3 = 30
# subway = [10, 20 ,30]
# print(subway)

# subwayPerson = ["유재석", "조세호", "박명수"]
# print(subwayPerson)
# print(subwayPerson.index("조세호"))

# from re import U
# from tempita import sub


# subwayPerson = ["Jason","Joseph","Pavel"]
# print(subwayPerson)
# print(subwayPerson.index("Pavel"))

# # subwayPerson.append("하하")
# # print(subwayPerson)

# subwayPerson.append("haha")
# print(subwayPerson)

# subwayPerson.insert(1, "정형돈")
# print(subwayPerson)

# subwayPerson.insert(1, "Janibek")
# print(subwayPerson)
# print(subwayPerson.pop())
# print(subwayPerson)
# # print(subwayPerson.pop())
# # print(subwayPerson)
# # print(subwayPerson.pop())
# # print(subwayPerson)
# print(subwayPerson.pop())
# print(subwayPerson)
# print(subwayPerson.pop())
# print(subwayPerson)
# print(subwayPerson.pop()) ##  .pop() menshe popku srezaet
# print(subwayPerson)
# subwayPerson.append("유재석")
# print(subwayPerson)
# print(subwayPerson.count("유재석"))

# subwayPerson.append("YoJasik")
# print(subwayPerson)
# print(subwayPerson.count("YoJasik"))

# # 정렬도 가능
# num_list = [5, 3, 6, 2, 1]
# num_list.sort()
# print(num_list)

# num_list = [5,3,6,2,1]
# num_list.sort()

#               Также возможна сортировка
#num_list = [5,3,6,2,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기도 가능
# num_list.reverse()
# print(num_list)

#  #        Poryadok Mojet byt izmnen
# num_list.reverse()
# print(num_list)

# # 다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]
# print(mix_list)

# #         Razlichnie Tipy Dannyh
#mix_list = ["Josik", 20, True]
# print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# #         расширение списка
#num_list.extend(mix_list)
#print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# #             очистить все
# num_list.clear()
# print(num_list)
# # 사전
# cabinet = {3:"유재석", 100:"김태호"} # key, value 로 구성된다.
# print(cabinet[3])
# print(cabinet[100])

# # Словарь
#cabinet = { 3:"Jasik", 100: "Kitai"}
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))

# # print(cabinet[5])               # 5 라는 키가 없기 때문에 오류가 발생한다.
# print(cabinet.get(5))             # 5 라는 키가 없어도 None으로 처리하고 오류가 발생하지 않는다.
# print(cabinet.get(5, "사용 가능"))  # "사용 가능" 이라는 문자를 내보낸다. 그러나 5에 저장하지는 않는다.
#print(cabinet[5])
#print(cabinet.get(5))
#print(cabinet.get(5,"available"))

# print(3 in cabinet) # True
# print(5 in cabinet) # False

#print(3 in cabinet) # True
#print(5 in cabinet) # False

# cabinet2 = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet2["A-3"])      
# print(cabinet2["B-100"])    

#cabinet2 = {"A-3":"Kanat", "B-100":"Jenya"}
# print(cabinet2["A-3"])
# print(cabinet2["B-100"])

# # 새 손님
# cabinet2["C-20"] = "조세호" # 이미 사용중인 경우 업데이트 없는 경우 추가
# print(cabinet2)
# cabinet2["A-3"] = "김종국"
# print(cabinet2)

##              новый гость
#cabinet2["C-20"] = "Joseph" # Обновите, если уже используется
#print(cabinet2)
#cabinet2["A-3"] = "Kimchenkuk"
#print(cabinet2)

# # 간 손님
# del cabinet2["A-3"] # 삭제한다. key가 없는 경우 에러
# print(cabinet2)
# # cabinet2.pop("A-3") # 삭제인 경우 pop을 사용해도 된다. 키가 없는 경우 에러
# # print(cabinet2)

# #             Gost` kotoriy uwel
#del cabinet["A-3"] # # удалить Ошибку, если ключ не существует
#print(cabinet2)
#cabinet2.pop("A-3") # В случае удаления можно использовать pop. Ошибка, если ключ не существует
#print(cabinet2)

# # key 들만 출력
# print(cabinet2.keys())

##                key ғана шығу 
#print(cabinet2.keys())

# # value 들만 출력
# print(cabinet.values())

# #             value ғана шығу 
#print(cabinet.values())
# # key, value 쌍으로 출력
# print(cabinet2.items())

#print(cabinet2.items())

# cabinet2.clear()
# print(cabinet2)

# cabinet2.clear()
# print(cabinet2)

# # 튜플
# # 값을 추가하거나 변경하는 것은 불가능하다.
# ##########################################
# # list는 [], dict는 {}, tuple은 () 을 사용한다.
# ##########################################
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# # кортеж
# # Невозможно добавлять или изменять значения.
# #############################################
# # Используйте [] для списка, {} для dict и () для кортежа.
# #############################################
# меню = ("Свиная котлета", "Сырная котлета")
# menu = ("Котлета","Сыр")
# print(menu[0])
# print(menu[1])


# # 일반적으로 사용하는 방법...
# # name = "김종국"
# # age = 20
# # hobby = "코딩"
# # print(name, age, hobby)

#           Обычно используется...
# name = "KimChenKuk"
# age = 20
# hobby = "coding"
# print(name, age, hobby)

# # 튜플을 사용하는 방법
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)


# # # Как использовать кортежи 
# (name, age, hobby) = ("Kim", 20, "Coding")
# print(name, age, hobby)
# #             세트 (set)
#           중복이 안되고 순서가 없다.

# my_set = {1,2,3,3,3} # 중괄호는 사전에서 사용했는데 그곳에는 키와 벨류가 있었고 여기는 값만 있다.
# print(my_set) # 중복을 허용하지 않기 때문에 1, 2, 3만 나온다.

#my_set = {1,2,3,3,3}
#print(my_set)

#java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

java = {"Andy", "Bill", "Cindy"}
python = set(["Dana", "Edd"])
#print(java)
#print(python)

# print(java)
# print(python)

# # 교집합 (java와 python을 모두 할 수 있는 사람) : & 나 .intersection을 쓴다.
# print(java & python)
# print(java.intersection(python))

# # Intersection (кто-то, кто может делать и java, и python): & или .intersection
#print(java & python)
#print(java.intersection(python))

# # 합집합 (java와 python 중 하나를 할 수 있는 사람) : | 나 .union을 쓴다.
# print(java | python)
# print(java.union(python))

# #             United 
print(java | python)
print(java.union(python))

# # 차집합 (java는 할 수 있지만 python은 할 수 없는 사람) : - 나 .difference를 쓴다.
#print(java - python)
#print(java.difference(python))

#print(java - python)
#print(java.difference(python))
# # python을 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

#python.add("Frank")
#print(python)

# # java를 잊었어요
# java.remove("김태호")
# print(java)

# # Забыл Java
#java.remove("Bill")

# установить (установить)
# Без дубликатов и без порядка.

# # 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu)
# print(menu, type(menu))

# #         Структура данных

#menu = {"Coffee", "Tea", "Milk"}
#print(menu)
#print(menu, type(menu))

# menu = list(menu)   # list로 형변환
# print(menu, type(menu))

#menu = list(menu) # cast to list
#print(menu, type(menu))

# menu = tuple(menu)  # tuple로 형변환
# print(menu, type(menu))

#menu = tuple(menu)
#print(menu, type(menu))

# menu = set(menu)    # 다시 set으로 형변환
# print(menu, type(menu))

#menu = set(menu)
#print(menu, type(menu))

# # 아래의 경우 키가 필요한 디션너리다. 이 경우 하나의 값을 2개 이상으로 쪼개어 키와 값을 준다.
# # 그러나 글자가 1글자인 경우는 오류를 친다. 그리고 이미 있던 값도 깨지기 때문에 의미가 없다. 사용하지 않도록 한다.
# menu = dict(menu)
# print(menu, type(menu))

# #         В приведенном ниже случае это словарь, для которого требуется ключ.
#  В этом случае одно значение разбивается на два или более, и задаются ключ и значение.
# # Однако, если есть только один символ, выдается ошибка.
#  И это бессмысленно, потому что существующее значение также нарушено. Избегайте его использования. 
#menu = dict(menu)
#print(menu, type(menu))

# # 퀴즈
# from random import *
# # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 
# #        12, 13, 14, 15, 16, 17, 18, 19, 20]
# lst = list(range(1, 21))  # list 로 형변환

# #         Контрольный опрос
# from random import *
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
        # 12, 13, 14, 15, 16, 17, 18, 19, 20]
# lst = list(range(1, 21))

# print(lst)
# shuffle(lst)
# print(lst)

# print(lst)
# shuffle(lst)
# print(lst)

# chickin = sample(lst, 1)    # 20개 중 하나를 뽑는다.
# lst.remove(chickin[0])
# coffee = sample(lst, 3)

# chicken = sample(lst,1)
# lst.remove(chicken[0])
# coffee = sample(lst,3)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(chickin))
# # print("커피 당첨자 : {0}, {1}, {2}".format(coffee[0], coffee[1], coffee[2]))
# print("커피 당첨자 : {0}".format(coffee)) # 위의 코드보다 간단하다.
# print("-- 축하합니다 --")

# -- Объявление победителя --")
# Цыпленок Победитель: {0}.format(цыпленок))
# ("Победитель кофе: {0}, {1}, {2}".format(кофе[0], кофе[1], кофе[2]))
# Coffee Winner: {0}".format(coffee)) # Проще, чем код выше.
# -- Поздравляю --")

# print( "Объявление победителя")
# print("Цыпленок победитель : {0}".format(chicken))
# print("Победитель кофе : {0}, {1}, {2}".format(coffee[0], coffee[1], coffee[2]))
# print("Победитель кофе {0}".format(coffee)) # proshe chem kod vyshe
# print("Congratulations")

# # 분기
# # weather = "비"
# weather = input("오늘 날씨는 어때요? ")

# weather = "Дождь"
# weather = input("Какая сегодня погода?")

# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요.")
# else:
#     print("맑은 날이네요.")

#if weather == "Дождь" or weather == "Пасмурная":
#    print("Принеси зонт")
# elif weather == "Пыльно":
    # print("Принеси маску")
# else:
#     print("Ясный день")
# temper = int(input("기온은 어때요?"))

# temper = int(input("Какая температура?"))

# if 30 <= temper:
#     print("너무 더워요. 나가지 마세요.")
# elif 10 <= temper and temper < 30:
#     print("괜찮은 날이에요.")
# elif 0 <= temper and temper <= 10:
#     print("외투를 챙기세요.")
# else:
#     print("너무 추워요. 나가지 마세요.")

# if 30 <= temper:
    # print("Слишком жарко не выходи.")
# elif 10 <= temper and temper < 30:
    # print("Тепло Можно выходить")
# else:
    # print("Очень холодно не выходи")
# 

# # for
# # print("대기번호 : 1")
# # print("대기번호 : 2")
# # print("대기번호 : 3")
# # print("대기번호 : 4")
# # 위와 같이 적을 수 없다.

#for i in list(range(21)):
#     print("대기번호 : {0}".format(i))

#starbucks = ["아이언맨", "토르", "그루트"]
#for customer in starbucks:위와 같이 적을 수 없다.
#     print("{0} 커피가 준비되었습니다.".format(customer))


# for i in list(range(21)):
    #  print("Резервный номер: {0}".format(i))
#  
# starbucks = [ "Groot", "Tor", "Iron Man"]
# for costumer in starbucks: #Не могу сказать что указано выше.
    #  print("{} Ваше кофе готово".format(costumer))

# while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index)) kofe gotov
#     index -= 1
#     if index == 0:
#         print("커피가 폐기되었습니다.") kofe byl otdan klientu

#while
# costumer = "Tor"
# index =5
# while index >= 1:
    # print("{0} Kofe gotov.{1} ostalos".format(costumer, index))
    # index -= 1
    # if index == 0:
        # print("кофе был отдан.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0} 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

# absent = [2, 5]
# no_book = [7] # 책을 깜빡했네요.
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("{0}은 수업 끝나고 교무실로 따라와.".format(student))
#         break
    
#     print("{0}, 책을 읽어라.".format(student))

#customer = "Iron Man"
#index = 1
#while True:
#     print("{0} Kofe gotov. pozvonit{1} raz".format(customer,index))
#     index += 1

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# absent = [2, 5]
# no_book = [7] # forgot books
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("После занятий следуй за мной в офис".format(student))
#         break
# print("{0}, Прочитай книгу".format(student))

#   if index == 5 :
    #    break

#  посавить 100 впереди




# # 1,2,3,4,5 앞에 100을 붙이기 101,102,103,104,105
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

  # # Преобразовать учеников в длину   
# 학생 이름을 길이로 변환
# studentName = ["Iron man", "Thor", "I am groot"]
# print(studentName)
# studentName = [len(l) for l in studentName]
# print(studentName)

# studentName = ["Iron man", "Thor", "I am groot"]
# print(studentName)
# studentName = [len(l) for l in studentName]
# print(studentName)

# 학생 이름을 대문자로 변경
# studentName = ["Iron man", "Thor", "I am groot"]
# print(studentName)
# studentName = [name.upper() for name in studentName]
# print(studentName)

# #  Bolshymi bukvami
# studentName = [ "Iron man", "Thor", "I am groot"]
# print(studentName)
# studentName = [name.upper() for name in studentName]
# print(studentName)

# # 퀴즈

# #  Контрольный опрос 
# from random import *
# passengerCount = 50
# passengerList = []
# usingTime = 0
# rideOn = ""

# for index in range(1, passengerCount+1):
#     usingTime = randint(5, 50)
#     if(5 <= usingTime <=15):
#         rideOn = "[O]"
#         passengerList.append(index)
#     else:
#         rideOn = "[ ]"
#     print("{0} {1:02d} Второй гость :(Продолжительность {2:02d})".format(rideOn, index, usingTime))

# print("Всего пассажиров на посадку : {0} ".format(len(passengerList)))
# for index in range (0, len(passengerList)):
#     print("[{0:02d} : {1:02}] гость ".format(index+1, passengerList[index]))

# #from random import *

# passengerCount = 50
# passengerList = []
# usingTime = 0
# rideOn = ""

# for index in range(1, passengerCount+1):
#     usingTime = randint(5, 50)
#     if(5 <= usingTime <= 15):
#         rideOn = "[O]"
#         passengerList.append(index)
#     else:
#         rideOn = "[ ]"
        
#     print("{0} {1:02d}번째 손님 (소요시간 : {2:02d}분)".format(rideOn, index, usingTime))


# print("총 탑승 승객 : {0} 분".format(len(passengerList)))

# for index in range(0, len(passengerList)):
#     print("[{0:02d} : {1:02d}번 손님]".format(index+1, passengerList[index]))



# # 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
    
# open_account()

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금을 완료할 수 없습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance
    
# def withdraw_night(balance, money):
#     commission = 100 # 수수료 100원
#     return commission, withraw(balance, money + 100)

# balance = 0
# balance = deposit(balance, 1000)

# # balance = withraw(balance, 1000)
# # print(balance)

# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# # 같은 학교 같은 학년 같은 반 같은 수업
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"
#           .format(name, age, main_lang))
    
# profile("유재석")
# profile("김태호")


# def profile(name, age, main_lang):
#     print(name, age, main_lang)
    
# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")


# # def profile(name, age, lang1, lang2, lang3, lang4, lang5):
# #     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")    # end 라는 것을 정의하면 이 프린트 문은 줄바꿈을 하지 않는다는 의미이다.
# #     print(lang1, lang2, lang3, lang4, lang5)
    
# # profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# # profile("김태호", 25, "Kotlin", "Swift", "", "", "")
    
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()
        
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")



# # 지역변수와 전역변수

# gun = 10

# def checkpoint(solders):
#     global gun  # 위의 gun을 이 지역 함수에서 사용하겠다는 의미
#                 # 그냥 지역변수를 쓸 경우는 global을 빼기만 하면 된다.
#     gun = gun - solders
#     print("[함수 내] 남은 총 : {0}".format(gun))
    
# def checkpoint_ret(gun, solders):
#     gun = gun - solders
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun
    
# print("전체 총 : {0}".format(gun))
# # checkpoint(2)
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))



# # 퀴즈

# MALE_VAL = 22
# FEMALE_VAL = 21

# def std_weight(height_cm, gender):
    
#     weight = 0.0
#     height = height_cm * 0.01
    
#     if gender == "남자":
#         weight = height * height * MALE_VAL
#     elif gender == "여자":
#         weight = height * height * FEMALE_VAL
        
#     return round(weight, 2)

# height = 175
# gender = "남자"
# weight = std_weight(height, gender)

# print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, weight))




# 표준 입출력

# , 를 만날 때마다 " vs " 문장을 넣어주도록 한다.
# print("Python", "Java", "Javascript", sep=" vs ")

# end= 를 쓰면 마지막에 줄바꿈을 하지 않고 어떤 문장을 넣어줄 수 있다.
# print("Python", "Java", "Javascript", sep=",", end=" ")
# print("무엇이 더 재밌을까요?")

# import sys

# print("Python", "Java", file=sys.stdout)    # 표준 출력으로 내보내는 것이다.
# print("Python", "Java", file=sys.stderr)    # 표준 에러로 내보내는 것이다.

# # 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(4), str(score).rjust(4), sep=":")

# # 은행 대기순번표
# # 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))    # 빈공간은 0으로 채워달라.

# answer = input("아무 값이나 입력하세요 : ") # 항상 문자열로 받는다. 따라서 숫자로 쓰려면 형변환을 해야 한다.
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")    



# # 다양한 출력 포멧

# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 때는 +로 표시 음수일 때는 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 큰 숫자에 3자리마다 ,를 찍기
# print("{0:,}".format(50000000000000))
# # 3자리마다 콤마를 찍고, 부호도 붙이고, 자릿수 확보하기
# # 빈 자리는 ^로 채우기
# print("{0:^<+30,}".format(5000000000000))
# # 소숫점 출력
# print("{0:f}".format(3/5))
# # 소숫점 특정 자리수까지만 표시 (소숫점 3째 자리에서 반올림)
# print("{0:.2f}".format(3/5))



# 파일 입출력

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)  # print를 써도 화면에 출력이 안되고 파일로 출력된다.
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80\n")
# score_file.write("코딩 : 100\n")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")

# while True:
#     line = score_file.readline()
#     if line == "": # 읽어온 내용이 없다면
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")

# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()


# # 피클 : 파일을 데이터 형태로 저장하는 방식을 말한다.
# import pickle
# profile_file = open("profile.pickle", "wb") # wb : write + binary
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# with open("profile.pickle", "rb") as profile_file: # profile.pickle 파일을 열어서 profile_file 에 저장한다.
#     print(pickle.load(profile_file)) # 그리고 나서 파일의 내용을 화면에 보여준다.
#     # 여기서는 파일을 별도로 닫아 줄 필요는 없다. with 구문을 사용하였기에 자동으로 닫힌다.

# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")
    
# with open("study.txt", "r", encoding="utf-8") as study_file:
#     print(study_file.read())



# 퀴즈
# numberOfWeek = input("주차를 입력하세요 : ")

# with open("{0}주차.txt".format(numberOfWeek), "w", encoding="utf-8") as weekFile:
#     weekFile.write("- X 주차 주간보고 -\n")
#     part = input("부서 : ")
#     weekFile.write("부서 : {0}\n".format(part))
#     name = input("이름 : ")
#     weekFile.write("이름 : {0}\n".format(name))
#     summary = input("요약 : ")
#     weekFile.write("요약 : {0}\n".format(summary))





# 클래스

# # 스타크래프트를 예로 들어 설명
# # 마린
# name = "마린"    # 유닛의 이름
# hp = 40         # 유닛의 체력
# damage = 5      # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력:{2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# # 만약 tank 2를 만든다면? 만들 수 있지만 tank를 100대 만든다면? 어려울 것이다. 이 때 사용되는 것이 클래스이다.

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank1 = Unit("탱크", 150, 35)

# # 멤버 변수
# # 레이스를 만들어 본다.
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것.
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# ##########################
# wraith2.clocking = True # 파이썬은 이렇게 없는 변수도 외부에서 선언하여 정의할 수도 있다.
# ##########################

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))
            
# # 파이어뱃
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)




# 상속
# 메딕 : 의무병, 공격력이 없다.
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
#               .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 파이어뱃
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)



# 다중 상속
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
#               .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))


# # 드랍십 : 공중 유닛, 수송기, 공격 기능 없음.

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
        
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
        
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)
        
# # 발키리
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")
# valkyrie.attack("1시")
# valkyrie.damaged(50)




# 연산자 오버로딩

# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
        
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
#               .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
        
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
        
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)
        
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

#  # 벌처 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌처", 80, 10, 20)
 
#  # 배틀크루저 : 공중 유닛, 체력도 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
 
# vulture.move("11시")
# battlecruiser.move("9시")



# # pass
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass
    
    
# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over() 



# # super
# class Unit:
#     def __init__(self):
#         print("Unit 생성자")


# class Flyable:
#     def __init__(self) -> None:
#         print("Flyable 생성자")
        
# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         super().__init__() 
#         # self를 안써도 된다. 
#         # 그러나 생성자는 다중상속일 경우 제일 먼저 들어오는 클래스의 것을 호출하고 그 다음은 호출하지 않는다.
#         # 따라서 아래와 같이 명시적으로 다중상속한 클래스의 __init__ 생성자 함수를 호출해 줘야 한다.
#         # Unit.__init__(self)
#         # Flyable.__init__(self)
        
# dropship = FlyableUnit()


# 예외 처리하기
# try:
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요. : "))
#     num2 = int(input("두 번째 숫자를 입력하세요. : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError as err:
#     print("에러 잘못된 값을 입력하였습니다.{0}".format(err))
# except ZeroDivisionError as err:
#     print(err)



