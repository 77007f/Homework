################## HOME WORK 1 ##################
#################################################


import pandas as pd
file_name1 = 'seoul_j.xls'
file_name2 = 'seoul_y.xls'

save_path = './gen/'
save_name = 'homework_merge.xls'

############# 파일 각각 불러오기 ##############

df1 = pd.read_excel(save_path + file_name1)
df2 = pd.read_excel(save_path + file_name2)

############## df1 데이터 내용 보기 

df1.head(50)

############## df2 데이터 내용보기

df2.head(50)

############## 파일을 MERGE

df = pd.merge(df1, df2, left_on = 'sigoodong', right_on ='sigoodong')

############# 데이터 내용보기

print(df)


############# 파일 저장하여 내보내기

df.to_excel(save_path + save_name)

######### 내용보기 

df.head(50)




