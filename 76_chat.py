# 76. [程式練習] 對話紀錄2 - part1
#    讀取 LINE-Viki.txt
#    計數對話中的字數,貼圖數,圖片數...
#    輸出 print()
#
#
# 沿用程式 :  61. 建立記帳程式專案 (+二維清單 2 dimension)
#
### 選取原有程式按Tab即會呈現內縮空4格空白
###   tab及空白混用會發生 IndentationError 錯誤
#
#  utf-8 / utf-8-sig 說明
#    https://www.796t.com/article.php?id=14537
#    如果寫入csv亂碼,改用 utf-8-sig
#  

import os  # operating system 作業系統

### 讀取檔案 : 這個版本是只有讀檔不parse
def read_file(filename):
    contents = []
    with open(filename, 'r', encoding='utf-8-sig') as f: #用utf-8-sig 會出現<0xfeff>符號
        for line in f:
            contents.append(line.strip())
    return contents


def convert(contents):
    new_contents = []
    str_name = None
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in contents:
        #print(line)  # 改版前先印出讀取內容...OK
        s = line.split(' ')  # split()回傳清單
        str_time = s[0]
        str_name = s[1]
        if str_name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:  # 計算加總每個element字數
                    allen_word_count += len(m)
        elif str_name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:  # 計算加總每個element字數
                    viki_word_count += len(m)
        #elif str_name:  # 這寫法即str_name有值才進入if判斷
        #    contents.append([str_name, line.strip()])  # (1)寫入list (2)每一個element是[人名, 一行內文]
    print('Allen說了', allen_word_count, ' 字')
    print('Allen傳了', allen_sticker_count, ' 張貼圖')
    print('Allen傳了', allen_image_count, '張圖片')
    
    print('Viki說了', viki_word_count, ' 字')
    print('Viki傳了', viki_sticker_count, ' 張貼圖')
    print('Viki傳了', viki_image_count, '張圖片')
    #return new_contents


#####  62. 寫入檔案
#    參考 52. 讀取檔案
#####  64. 寫入欄位名稱 + 編碼問題
#    檔案寫入跟讀取都與編碼有關 
#       (到課程64, open('w') 是寫入新的檔案,原始資料會被覆蓋,所以課程65在讓使用者輸入前,先讀取檔案 )
#    在開檔open()時, 要指定編號 UTF-8

# 寫入檔案-(1) txt
def write_txt(filename, contents):
    with open(filename, 'w') as f:
        for c in contents:
            f.write(c[0] + ' : ' + c[1] + '\n')


def main():
    filename_input = 'LINE-Viki.txt'
    # 檢查檔案在不在
    if os.path.isfile(filename_input):  #非工作目錄下要給絕對路徑  #Refactor: 檔名'products.csv'改成參數
        print('file exists!')

        contents = read_file(filename_input)
        #print_contents(contents)
        # write_txt('output.txt', contents)  # 寫檔先 mark
        convert(contents)
    else:
        print('No such file : ', filename_input)

main()