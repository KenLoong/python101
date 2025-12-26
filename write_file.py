text = 'hahah\nssss'

f = open('./aaa.txt','w')
f.write(text)
f.close()

append_txt = '\nenenenen'
# with open(...) 语句。它会在代码块结束后自动关闭文件，确保数据写入并释放资源。
with open('./aaa.txt','a') as f:
    f.write(append_txt)


rf = open('./aaa.txt','r')
for line in rf.readlines():
    print(line.strip())
