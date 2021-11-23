print("	日期	服装名称 价格/件库存数量 销售量/每日")
print("	1号	    羽绒服	253.6	500	     10	")
print("	2号	    牛仔裤	86.3	600	     60	")
print("	3号	    风衣	96.8	335	     43	")
print("	4号	    皮草	135.9	855	     63	")
print("	5号  	T血	    65.8	632      63	")
print("	6号 	衬衫	49.3	562	     120")
print("	7号	    牛仔裤	86.3	600	     72	")
print("	8号	    羽绒服	253.6	500	     69	")
print("	9号	    牛仔裤	86.3	600	     35	")
print("	10号	羽绒服	253.6	500	     140")
print("	11号	牛仔裤	86.3	600	     90	")
print("	12号	皮草	135.9	855	     24	")
print("	13号	T血	    65.8	632	     45	")
print("	14号	风衣	96.8	335	     25	")
print("	15号	牛仔裤	86.3	600	     60	")
print("	16号	T血	    65.8	632	     129")
print("	17号	羽绒服	253.6	500	     10	")
print("	18号	风衣	96.8	335	     43	")
print("	19号	T血	    65.8	632	     63	")
print("	20号	牛仔裤	86.3	600	     60	")
print("	21号	皮草	135.9	855	     63	")
print("	22号	风衣	96.8	335	     60	")
print("	23号	T血	    65.8	632	     58	")
print("	24号	牛仔裤	86.3	600	     140")
print("	25号	T血	    65.8	632	     48	")
print("	26号	风衣	96.8	335	     43	")
print("	27号	皮草	135.9	855	     57	")
print("	28号	羽绒服	253.6	500	     10	")
print("	29号	T血	    65.8	632	     63	")
print("	30号	风衣	96.8	335	     78	")
total=0#总销售额
average=0#平均每日销售数量
list_price=[253.6,86.3,96.8,135.9,65.8,49.3,86.3,253.6,86.3,253.6,86.3,135.9,65.8,96.8,86.3,65.8,253.6,96.8,65.8,86.3,135.9,96.8,65.8,86.3,65.8,96.8,135.9,253.6,65.8,96.8]
# 价格
list_day=[10,60,43,63,63,120,72,69,35,140,90,24,45,25,60,129,10,43,63,60,63,60,58,140,48,43,57,10,63,78]
# 每日销售量
yrf_month=[10,69,140,10,10]#羽绒服月销售量
nzk_month=[60,72,35,90,60,60,140,]#牛仔裤月销售量
fy_month=[43,25,43,60,43,78]#风衣月销售量
pc_month=[63,24,63,57]#皮草月销售量
Ts_month=[63,45,129,63,58,48,63]#T恤月销售量
cs_monrh=120
for i in range(len(list_price)):
        a=list_price[i]*list_day[i]
        total=total+a
print("总销售额为：",total)#总销售额

for i in range(len(list_day)):
        average=average+list_day[i]
print("平均每日销售数量为：",average/30)

yrf=0
for i in range(len(yrf_month)):
        yrf=yrf+yrf_month[i]
nzk=0
for i in range(len(nzk_month)):
        nzk=nzk+nzk_month[i]
fy=0
for i in range(len(fy_month)):
        fy=fy+fy_month[i]
Ts=0
for i in range(len(Ts_month)):
        Ts=Ts+Ts_month[i]
pc=0
for i in range(len(pc_month)):
        pc=pc+pc_month[i]
print("羽绒服的月销售占比为：",yrf/average*100,"%")
print("牛仔裤的月销售占比为：",nzk/average*100,"%")
print("风衣的月销售占比为：",fy/average*100,"%")
print("皮草的月销售占比为：",pc/average*100,"%")
print("T恤的月销售占比为：",Ts/average*100,"%")
print("衬衫的月销售占比为：",cs_monrh/average*100,"%")