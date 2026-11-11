리스트 = [ '삼성전자', '카카오', '네이버', '신풍제약' ]

파일 = open('company.txt', 'w')
for i in 리스트:
    파일.write(i+'\n')
파일.close()


파일 = open('company.txt','r')
print(파일.read())
파일.close()