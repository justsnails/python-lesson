# 密碼重設程式
# 先在程式碼中設定好密碼 password = 'a123456'
# 讓使用者【最多輸入3次密碼】
# 不對的話，就印出"密碼錯誤! 還有_次機會"
# 對的話，就印出"登入成功!"
# 輸入錯誤三次帳號就會鎖住!

pw = 'a123456'
i = 2
while True:
    ps = input('請輸入密碼: ')
    if ps == pw:
        print('登入成功!')
        break
    elif ps != pw and i >= 1:
        print('密碼錯誤，剩下', i,'次嘗試機會')
        i -= 1
    else:
        print('密碼錯誤三次，帳號已鎖住!')
        break
