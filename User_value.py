# #Task 1  -> Userden alinan 5 deyer siralama-----------------------------------------------------------------------

# Metod 1
# value_1=int(input('İlk dəyəri daxil edin : '))
# value_2=int(input('İkinci dəyəri daxil edin : '))
# value_3=int(input('Üçüncü dəyəri daxil edin : '))
# value_4=int(input('Dördüncü dəyəri daxil edin : '))
# value_5=int(input('Beşinci dəyəri daxil edin : '))

# user_values=[value_1,value_2,value_3,value_4,value_5]

#Metod 2
i=0
user_values=[]
while i<5:
    i+=1
    value_1=int(input(f'{i}. dəyəri daxil edin : '))
    user_values.append(value_1)
    
user_values.sort()
print(f'Daxil olunan dəyərlər : {user_values}')



# #Task 2 =>Alfabetik siralama--------------------------------------------------------------------------------------
# user_word=input('Sözü daxil edin : ')

# words=user_word.split()
# change_word=''
# for x in words:
#     x=list(x)
#     x.sort()
#     x=''.join(x)
#     change_word+=x+' '
       
# print(f'{user_word} => {change_word}')



#Task 3 -> Ədəd təxmin oyunu  --------------------------------------------------------------------------------------

# count=1
# find_numb=int(input(f'{count}. təxmin  Ədədi daxil edin : '))
# while find_numb!=17:
#     count+=1
#     find_numb=int(input(f'{count}. təxmin  Ədədi daxil edin : '))
# else:
#     print(f"Təbriklər, {count}. təxmində doğru cavabı tapdınız.")

#Task 4 -> 1-100 arası sadə ədədlər --------------------------------------------------------------------------------
# prime_numb=[]
# for i in range(1,100):
#     for j in range(1,i+1):
#         if i%j==0 and j!=i and j!=1:
#             break
    
#         elif j==i and i!=1:
#             prime_numb.append(i)
# print(f'1-100 arası sadə ədədlər :  {prime_numb}')

