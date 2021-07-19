# 79. [程式練習] 對話紀錄3 - 格式改寫

lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())  # strip()去除空白and換行符號and特殊符號


# 針對清單的element, 指定index取值
for line in lines:
    s = line.split(' ')
    print(s)
    str_time = s[0][:5]  # 時間位於s[0]的index=0開始5位
    str_name = s[0][5:]  # 人名位於s[0]的index=5開始到最後
    print(str_time, str_name)
