driving = input('請問你開過車嗎? ')
if driving != '有' and driving != '沒有':
    print('只能回答有或沒有')
    raise SystemExit
age = input('請問你的年齡? ')
age = int(age)
if driving == '有':
    if age >= 18:
        print('你通過測驗')
    else:
        print('奇怪，你怎麼有開過車')
elif driving == '沒有':
    if age < 18:
        print('等成年再來吧')
    else:
        print('趕緊去報名駕照課程吧')