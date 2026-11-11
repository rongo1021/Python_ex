리스트 = [ '삼성전자', '카카오', '네이버', '신풍제약' ]


for i in 리스트:
    if i == 리스트[0] :
        파일 = open('company.txt', 'w')
        파일.write(i)
        파일.write('\n')
        파일.close()
    else :
        파일 = open('company.txt', 'a')
        파일.write(i)
        파일.write('\n')
        파일.close()

파일 = open('company.txt','r')
print(파일.read())
파일.close()