

def is_odd(n):
    return n%2==1

#print(list(filter(is_odd,list(range(1,20)))))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        print('_odd_iter_n=',n)
        yield n


def _not_divisible(n):
    print('__not_divisible_n=',n)
    return lambda x: x % n > 0




def primes():
    yield 2
    it = _odd_iter() # 初始序列
    index = 1
    while True:
        index = index+1
        n = next(it) # 返回序列的第一个数
        print(' n = ',n)
        print(' index = ',index)
        yield n
        print(" befer filter = ",index)
        it = filter(_not_divisible(n), it) # 构造新序列, 猜测是增加新的数据过滤规则
        print(" after filter = ",index)


# 打印1000以内的素数:

pr = primes()

print(next(pr)) #2
print(next(pr)) #3
print(next(pr))	#5
print(next(pr)) #7
print(next(pr)) #11



#its = _odd_iter() # 初始序列
#next(its)
#next(its)

