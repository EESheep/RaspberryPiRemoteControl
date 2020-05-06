def check_play_button(button, play_button, mouse_x, mouse_y):
    if mouse_x < play_button.rect.right and mouse_x >= play_button.rect.left:
        if mouse_y > play_button.rect.top and mouse_y <= play_button.rect.bottom:
            button.stats = True

def ch9329_kbencode(keyvalue,modvalue):
    """
    组合串口发送的键盘按键信息

    :param keyvalue: 按下的普通按键，目前该函数只能单个
    :param modvalue: 按下的组合键，最多8个
    :returns: 返回串口发送的信息
    """
    str_head = "\x57\xAB\x00\x02\x08"
    str_tail = chr((0x0C+keyvalue+modvalue)&0xff) 
    mod = chr(modvalue) 
    key = chr(keyvalue) 
    str_a = str_head + mod + '\x00'  + key + '\x00\x00\x00\x00\x00'  + str_tail

    return str_a

def ch9329_msencode(x,y):
    """
    组合串口发送的信息

    :param x: 鼠标位置的横坐标
    :param y: 鼠标位置的纵坐标
    """
    str_head = "\x57\xAB\x00\x04\x02\x00" 

    x = int(x*4096/1280)
    y = int(y*4096/768)

    x_str1 = chr(x&0xff) 
    x_str2 = chr((x>>8)&0xff)
    y_str1 = chr(y&0xff) 
    y_str2 = chr((y>>8)&0xff) 

    str_tail = 0x57+0xAB+4+7+2+ int(y&0xff) +  int((y>>8)&0xff) + int(x&0xff) +  int((x>>8)&0xff)

    str = str_head + x_str1 +x_str2 + y_str1 + y_str2 + '\x00' + chr(str_tail&0xff)

    return str