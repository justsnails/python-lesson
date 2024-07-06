while True:
    mode = input('請輸入遊戲模式: ')
    if mode == 'q' or mode == 'Q':
        print('已經離開遊戲')
        break
    elif mode == '1':
        print('已經進入模式一')
    elif mode == '2':
        print('已經進入模式二')
    else:
        print('請輸入1 / 2 / q')