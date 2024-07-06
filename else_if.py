# else if 另外如果
age = input('彥宇，請輸入年齡: ') # input 回傳到age成為字串
age = int(age) # casting 型態轉換

if 2 <= age <= 6:
    print('彥宇在親子田幼稚園')
elif 7 <= age <= 12: 
    print('彥宇在育英國小')
elif 13 <= age <=15:
    print('彥宇在大成國中')
elif 16 <= age <= 18:
    print('彥宇在快樂高中')
elif 18 < age <= 24:
    print('彥宇進入大學')
elif 70 <= age < 100:
    print('彥宇已經是老頭子了') 
elif 100 <= age:
    print('彥宇已經成為太空人了')
else: print('彥宇不用去讀書了')
