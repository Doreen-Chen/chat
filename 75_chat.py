# 75. [程式練習] 對話紀錄1 - 格式改寫
#    讀取input.txt
#    每行格式 人名+":"+空格+對話內容
#    輸出output.txt
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

### 讀取檔案
def read_file(filename):
    contents = []
    str_name = None  # 預設值 / 即 null
    with open(filename, 'r', encoding='utf-8-sig') as f: #用utf-8-sig 會出現<0xfeff>符號
        for line in f:
            if 'Allen' in line: #這裡寫 line == 'Allen' 印出沒有任何東西
                str_name = line.strip() #或直接寫人名
                continue  # 讀取人名, 下一筆
            elif 'Tom' in line: #這裡寫 line == 'Tome' 印出沒有任何東西
                str_name = line.strip()
                continue  # 讀取人名, 下一筆
            elif str_name:  # 這寫法即str_name有值有進入if判斷
                contents.append([str_name, line.strip()])  # (1)寫入list (2)每一個element是[人名, 一行內文]
    return contents


# 印出所有記錄
def print_contents(contents):
    print('印出所有內文 : ')
    for c in contents:
        print(c[0], ' : ', c[1]) # 人名 + 冒號 + 內文


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


# 寫入檔案-(2) csv
def write_csv(wrt_filename, contents):
    with open(wrt_filename, 'w') as f:  #Refactor: 檔名'products.csv'改成參數
        f.write('Name,Content\n')  # 64. 寫入欄位名稱 + 編碼問題
        for c in contents:
            f.write(c[0] + ' : ' + c[1] + '\n')


def main():
    filename_input = 'input.txt'
    # 檢查檔案在不在
    if os.path.isfile(filename_input):  #非工作目錄下要給絕對路徑  #Refactor: 檔名'products.csv'改成參數
        print('file exists!')
        contents = read_file(filename_input)
        print_contents(contents)
        write_txt('output.txt', contents)
    else:
        print('No such file : ', filename_input)

main()