# coding:utf-8

shu = '01老鼠'
niu = '02牛'
hu = '03老虎'
tu = '04兔'
long = '05龙'
she = '06蛇'
ma = '07马'
yang = '08羊'
hou = '09猴'
ji = '10鸡'
gou = '11狗'
zhu = '12猪'

shengxiao = []
shengxiao.append(gou)
shengxiao.append(ji)
shengxiao.append(zhu)
shengxiao.append(she)
shengxiao.append(tu)
shengxiao.append(hou)
shengxiao.append(hu)
shengxiao.append(niu)
shengxiao.append(shu)
shengxiao.append(long)
shengxiao.append(ma)
shengxiao.append(yang)

print(shengxiao)
print(len(shengxiao))
shengxiao.sort()
print(shengxiao)
shengxiao.sort(reverse=True)
print(shengxiao)
# 这个地方有点问题，一个列表经过反转 已经是倒序了，再次反转是不会变成正序的
# 他判断的方式：
#   如果当前列表已经满足了一开始定义的反转顺序了，就不会进行反转了
shengxiao.sort(reverse=True)
print(shengxiao)


mix = ['python', 1.2, {'name': 'dewei'}]
