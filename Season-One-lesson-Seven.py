# list_comprehension
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

out = [i**2 for i in lst if i % 2 == 0]

print(out)
#-----------------------------------------------------
# decorators   ansi_colors
print("\033[30;4m  hello \033[0m")
print("\033[31;4m  hello \033[0m")
print("\033[32;4m  hello \033[0m")
print("\033[33;4m  hello \033[0m")
print("\033[34;4m  hello \033[0m")
print("\033[35;4m  hello \033[0m")
print("\033[36;4m  hello \033[0m")
#----------------------------------------------------------
# html_tag_new
def tag_maker(tag):
    def decorator(f):
        def out(x):
            res = f(x)
            if type(res) == str:
                res = "<" + tag + ">" + res + "</" + tag + ">"
            return res

        return out

    return decorator


@tag_maker("span")
def echo(s):
    return s


print(echo("Hello"))
print(echo(10))
#----------------------------------------------------------------------
# html_tags
def bold(f):
    def out(x):
        res = "<b>" + f(x) + "</b>"
        return res
    return out


def italic(f):
    def out(x):
        res = "<i>" + f(x) + "</i>"
        return res
    return out


@bold
@italic
def echo(s):
    return s


# echo = italic(echo)
# echo = bold(echo)

# echo = bold(italic(echo))

print(echo("hello"))
#-------------------------------------------------------------------------
# markdown_decorator     timer_decorator
import time
import math


def timer(f):
    def f_decorated(*args, **kwargs):
        t1 = time.time()
        res = f(*args, **kwargs)
        t2 = time.time()
        print("Elapsed time : ", t2 - t1)

        return res
    return f_decorated


def tired(f):
    def f_decorated(*args, **kwargs):
        print("gonna start it in a minute")
        res = f(*args, **kwargs)
        time.sleep(2)
        return res
    return f_decorated


@timer
@tired
def fact(n):
    return math.factorial(n)


@timer
def fact_old(n):
    out = 1
    for i in range(1, n + 1):
        out = out * i

    return out


num = 10000
res = fact(num)
print(res)
res = fact_old(num)
print(res)
# -----------------------------------------------------------------
# what_is_decorator
import math

def decorator(f):
    def out(*args, **kwargs):
        res = f(*args, **kwargs)
        return res
    return out


@decorator   # echo = decorator(echo)
def echo(s, n):
    return s


res = echo("Hello", 7)
print(res)
#-------------------------------------------------------------------------
# file_manipulation assignment
f = open('input.txt')
text = f.read()
f.close()
n, c = text.split()
n = int(n)

f2 = open('output.txt', mode='w')
for i in range(1, n+1):
    f2.write(i*c)
    f2.write('\n')

#----------------------------------------------------------------------------
# read_data_from_file
f = open('input.txt')
# f = open('C:/Users/Administrator/PycharmProjects/mft-sk/S07/file_manipulation/input.txt')
#          C:/Users/Administrator/PycharmProjects/mft-sk/S07/file_manipulation/    .
#          C:/Users/Administrator/PycharmProjects/mft-sk/S07/                      ..   ./..
#          C:/Users/Administrator/PycharmProjects/mft-sk/                          ../..
#          C:/Users/Administrator/PycharmProjects/                                 ../../..
#          C:/Users/Administrator/PycharmProjects/mft-sk/S07/                      ..
#          C:/Users/Administrator/PycharmProjects/mft-sk/S07/                      ..

text = f.read(10)
print(text)
text = f.read(10)
print(text)
#----------------------------------------------------------------------------
# write_into_file
# r --> readable
# w --> writeable
# a --> append

# t --> text
# b --> bytes

# +

f = open("output.txt", mode='r+')
# text = f.read()
f.seek(10, 2)
f.write("hello")

# print(text)
#-----------------------------------------------------------------------------------
# functions review
def timer(f):
    def f_decorated(*args, **kwargs):
        t1 = time.time()
        res = f(*args, **kwargs)
        t2 = time.time()
        print("Elapsed time : ", t2 - t1)

        return res
    return f_decorated
#---------------------------------------------------------------------------------------
# std_library reading_from_internet
import urllib.request


f = urllib.request.urlopen('https://www.python.org')
text = f.read()
text_str = text.decode('utf-8')
print(text_str)
#-------------------------------------------------------------------------
#time_python
import time


def fact(n):
    out = 1
    for i in range(1, n + 1):
        out = out * i

    return out


t1 = time.time()
res = fact(1000)
t2 = time.time()


print("Elapsed time : ", t2-t1)
# print(res)
#---------------------------------------------------------------------------
# list_comprehension
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

out = [i**2 for i in lst if i % 2 == 0]

print(out)




#-----------------------------------END------------------------------------------#