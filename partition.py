# -*- coding: utf-8 -*-
#解决Python2.7的UnicodeEncodeError: ‘ascii’ codec can’t encode异常错误
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
s = 'name,性别 as sex,userID,employee.员工姓名 aS username, department.部门名称 As department,department.ID'
print s
s = unicode(s,"utf-8")
print s
#替换大小写AS
s = s.replace("as", "AS")
s = s.replace("aS", "AS")
s = s.replace("As", "AS")
print s
#拆分字符串为数列
s=s.split(',')
print s
#检索数列中的field值
n = 0
for i in s:        
    if i.find('.') > 0: #检查是否包括表名.字段名之间那个.
        if len(i.partition(' AS ')[2]) > 0 :
            s[n] = i.partition(' AS ')[2]
        else:      
            s[n] = i.partition('.')[2]
    else:
        if len(i.partition(' AS ')[2]) > 0 :
            s[n] = i.partition(' AS ')[2]
        else:      
            s[n] = i
    n = n + 1
print s
#解码后的字符串的field值
n = 0
for i in s:
    print i.encode(encoding='UTF-8',errors='strict')
    s[n] = i.encode(encoding='UTF-8',errors='strict')
    n = n + 1
print s