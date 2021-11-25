'''
一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，
问第几天能出来？请编程求出。
'''
high=20
gua_high=0
day=0
while 1:
    gua_high=gua_high+3
    if gua_high>high-2:
        break
    gua_high=gua_high-2
    day+=1
print("青蛙爬出需要",day+1,"天")