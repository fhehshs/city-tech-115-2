# -*- coding: utf-8 -*-
# 第 4 週（課程計畫 W18）：重複結構 for 與 while（Colab：py04_loops）
from content._kit import *

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一節：for 迴圈與 range()', 'start': 2},
    {'name': '第二節：累加與雙重迴圈', 'start': 8},
    {'name': '第三節：while 與 break', 'start': 14},
    {'name': '實作與總結', 'start': 20},
]

SLIDES = [
    {'id': 1, 'title': '重複結構', 'chapter': '封面', 'bg': 'navy',
     'html': cover('🔁', '重複結構：迴圈', 'Repetition · for · range() · while · break',
                   ['🔢 range()', '➕ 累加器', '⭐ 雙重迴圈', '⏳ while'], '第 4 週')},

    # ── 第一節 ──
    {'id': 2, 'title': '為什麼要迴圈', 'chapter': '第一節：for 迴圈與 range()', 'bg': 'white',
     'html': title('😩 印 50 行 Hello Python!，你要寫 50 次 print 嗎？')
     + two_col(py('print("Hello Python!")\nprint("Hello Python!")\nprint("Hello Python!")\n# ……還要再 47 行', '沒有迴圈', ''),
               py('for i in range(50):\n    print("Hello Python!")', '有迴圈：2 行搞定', 'Hello Python!\nHello Python!\n…（共 50 行）'), '1fr 1fr')
     + note('🔁 <strong>重複結構</strong>：重複執行某些敘述，直到滿足特定條件為止，也叫<strong>迴圈（loop）</strong>。電腦最擅長做重複又不會累的事。')},

    {'id': 3, 'title': 'for 語法', 'chapter': '第一節：for 迴圈與 range()', 'bg': 'white',
     'html': title('🔢 for 迴圈語法')
     + lead(ic('for 變數 in range(起始值, 結束值, 間隔):') + '　→ 變數依序取 range 產生的每個數，每取一個就執行一次區塊。')
     + steps([('結束值「不包含」', 'range(1, 6) 是 1～5，不是 1～6'),
              ('起始值可省略', '省略時從 0 開始：range(6) 等於 range(0, 6)'),
              ('間隔可省略', '省略時每次加 1；可以是負數（倒數）'),
              ('別忘了冒號和縮排', '和 if 一樣，迴圈區塊要縮排')], 'green')},

    {'id': 4, 'title': 'range 實例', 'chapter': '第一節：for 迴圈與 range()', 'bg': 'white',
     'html': title('🧪 range() 實例：先猜再看')
     + table(['寫法', '產生的數', '重複幾次'],
             [['range(6)', '0, 1, 2, 3, 4, 5', '6'],
              ['range(2, 6)', '2, 3, 4, 5', '4'],
              ['range(2, 15, 3)', '2, 5, 8, 11, 14', '5'],
              ['range(10, 0, -2)', '10, 8, 6, 4, 2', '5'],
              ['range(1, n + 1)', '1, 2, …, n', 'n']], ['32%', '44%', '24%'])
     + py('for i in range(2, 15, 3):\n    print(i, end=" ")', '', '2 5 8 11 14 ')
     + note('🧮 小技巧：range(a, b) 會重複 <strong>b − a</strong> 次。')},

    {'id': 5, 'title': 'for 搭配字串', 'chapter': '第一節：for 迴圈與 range()', 'bg': 'white',
     'html': title('🔤 for 也可以「走過」一串東西')
     + two_col(py('for ch in "Python":\n    print(ch, end="-")', '逐一取出字串的每個字', 'P-y-t-h-o-n-'),
               py('for city in ["台北", "台中", "高雄"]:\n    print(city, "加油！")', '逐一取出串列的每個元素（第 6 章詳細學）',
                  '台北 加油！\n台中 加油！\n高雄 加油！'), '1fr 1fr')
     + note('📌 Python 的 for 是「<strong>對一串東西裡的每一個</strong>做事」，range() 只是其中一種「一串數字」。')},

    {'id': 6, 'title': '流程圖', 'chapter': '第一節：for 迴圈與 range()', 'bg': 'white',
     'html': title('🗺️ 計數迴圈的流程圖')
     + two_col(flow([('process', 'i = 1', ''), ('decision', 'i <= 5 ?', '否 → 離開迴圈'), ('process', '輸出 i', ''),
                     ('process', 'i = i + 1', '→ 回到判斷')], 170),
               card('blue', 'for 幫你做了三件事', '① 設定起始值 i = 1<br>② 每次檢查是否還在範圍內<br>③ 每輪結束自動把 i 往下一個<br><br>'
                    '下一節的 while 迴圈，這三件事要<strong>自己寫</strong>。', '🤖'), '1fr 1fr')},

    {'id': 7, 'title': '第一節 隨堂測驗', 'chapter': '第一節：for 迴圈與 range()', 'bg': 'purple', 'quiz': 'q1',
     'html': quiz_cover('第一節 隨堂測驗', 'for 迴圈與 range() ｜ 4 題')},

    # ── 第二節 ──
    {'id': 8, 'title': '累加器', 'chapter': '第二節：累加與雙重迴圈', 'bg': 'white',
     'html': title('➕ 累加器：計算 1 + 2 + … + n')
     + two_col(py('n = int(input("n="))\ntotal = 0                # ① 迴圈前先歸零\nfor i in range(1, n + 1):\n    total = total + i    # ② 每輪加上 i\nprint("1 加到", n, "的和", total)', '',
                  'n=5\n1 加到 5 的和 15'),
               table(['i', 'total'], [['（開始）', '0'], ['1', '1'], ['2', '3'], ['3', '6'], ['4', '10'], ['5', '15']], ['50%', '50%']), '1.5fr 1fr')
     + note('⚠️ 變數別叫 ' + ic('sum') + '：它是 Python 內建函式，蓋掉之後 ' + ic('sum([1,2,3])') + ' 就會出錯。', 'yellow', '')},

    {'id': 9, 'title': '累加變化題', 'chapter': '第二節：累加與雙重迴圈', 'bg': 'white',
     'html': title('🧩 累加的變化題')
     + table(['題目', '關鍵寫法'],
             [['3 + 6 + 9 + … + 150', 'for i in range(3, 151, 3)'],
              ['1～n 的偶數和', 'for i in range(2, n + 1, 2)'],
              ['1～n 中 7 的倍數或個位數是 7', 'if i % 7 == 0 or i % 10 == 7:'],
              ['1 × 2 × 3 × … × n（n!）', 'p = 1 開始，p = p * i（乘法要從 1 開始！）'],
              ['n + (n−1) + … + 1', 'for i in range(n, 0, -1)']], ['46%', '54%'])
     + note('🧾 對應線上練習 <strong>#323 計算 1 加到 n 的值</strong>。')},

    {'id': 10, 'title': '雙重迴圈', 'chapter': '第二節：累加與雙重迴圈', 'bg': 'white',
     'html': title('🔁🔁 雙重迴圈：迴圈裡還有迴圈')
     + two_col(py('for i in range(4):          # 外圈：4 列\n    for j in range(6):      # 內圈：每列 6 個\n        print("*", end="")\n    print()                 # 換行', '',
                  '******\n******\n******\n******'),
               card('purple', '時鐘的比喻', '外圈像<strong>時針</strong>、內圈像<strong>分針</strong>：時針走 1 格，分針要轉完一整圈。'
                    '<br><br>總共執行 4 × 6 = <strong>24</strong> 次 print("*")', '🕐'))
     + note('💡 ' + ic('print()') + ' 括號裡什麼都沒有，就是「只換行」。')},

    {'id': 11, 'title': '星號三角形', 'chapter': '第二節：累加與雙重迴圈', 'bg': 'white',
     'html': title('⭐ 範例：星號三角形')
     + two_col(py('n = int(input("n="))\nfor i in range(1, n + 1):\n    for j in range(i):     # 第 i 列印 i 個\n        print("*", end="")\n    print()', '',
                  'n=4\n*\n**\n***\n****'),
               card('green', '關鍵：內圈次數跟著外圈變', '第 1 列印 1 個、第 2 列印 2 個…<br>所以內圈是 ' + ic('range(i)') + '。'
                    '<br><br>挑戰：改成倒三角形？或置中的金字塔？（提示：先印空白）', '🔺'))
     + note('🧾 對應線上練習 <strong>#325 印出星號三角形</strong>。Python 也可以用 ' + ic('print("*" * i)') + ' 一行完成，但要先會用迴圈想。')},

    {'id': 12, 'title': '九九乘法表', 'chapter': '第二節：累加與雙重迴圈', 'bg': 'white',
     'html': title('✖️ 範例：九九乘法表')
     + py('for i in range(1, 10):\n    for j in range(1, 10):\n        print(f"{i}x{j}={i*j:2d}", end="  ")\n    print()', 'f"{i*j:2d}" 讓結果佔 2 格，排版才會對齊',
          '1x1= 1  1x2= 2  1x3= 3 … 1x9= 9\n2x1= 2  2x2= 4  2x3= 6 … 2x9=18\n…\n9x1= 9  9x2=18  9x3=27 … 9x9=81')
     + note('🤔 想一想：如果要印成「直的」（一欄是一個數的乘法），i 和 j 要怎麼調換？')},

    {'id': 13, 'title': '第二節 隨堂測驗', 'chapter': '第二節：累加與雙重迴圈', 'bg': 'purple', 'quiz': 'q2',
     'html': quiz_cover('第二節 隨堂測驗', '累加與雙重迴圈 ｜ 4 題')},

    # ── 第三節 ──
    {'id': 14, 'title': 'while 語法', 'chapter': '第三節：while 與 break', 'bg': 'white',
     'html': title('⏳ while：條件成立就一直做')
     + two_col(py('i = 1               # ① 起始值\nwhile i < 6:        # ② 條件\n    print(i)\n    i = i + 1       # ③ 更新（不能忘！）', '', '1\n2\n3\n4\n5'),
               card('red', '⚠️ 無窮迴圈', '忘了寫 ' + ic('i = i + 1') + '，i 永遠是 1，條件永遠成立，程式就停不下來。'
                    '<br><br>在 Colab 按儲存格左邊的 <strong>■ 停止</strong>可以中斷。', '♾️'))
     + note('🧾 對應線上練習 <strong>#326 while 練習（輸出 1～5）</strong>、<strong>#327 輸出 1 加到 n</strong>。')},

    {'id': 15, 'title': 'for 和 while 怎麼選', 'chapter': '第三節：while 與 break', 'bg': 'white',
     'html': title('⚖️ for 和 while 怎麼選？')
     + table(['', 'for', 'while'],
             [['適合', '<strong>知道要做幾次</strong>', '<strong>不知道要做幾次</strong>，只知道何時停'],
              ['例子', '印 50 行、1 加到 n、走過串列', '存錢到目標金額、猜數字猜對為止、輸入密碼'],
              ['計數', '自動', '要自己初始化、自己更新']], ['16%', '42%', '42%'])
     + note('🇹🇼 生活例子：捷運「坐 5 站」用 for；「坐到台北車站才下車」用 while。')},

    {'id': 16, 'title': 'while 範例：成績加分', 'chapter': '第三節：while 與 break', 'bg': 'white',
     'html': title('📈 範例：多寫幾個作業才能達標？')
     + lead('每多寫一個作業，成績 ×1.05（去除小數）。例如 70 → 73 → 76…。輸入起始與期望成績，輸出至少要多寫幾個。')
     + two_col(py('s = int(input("起始成績："))\ngoal = int(input("期望成績："))\ncount = 0\nwhile s < goal:\n    s = int(s * 1.05)\n    count += 1\nprint("至少要多完成", count, "個作業")', '',
                  '起始成績：70\n期望成績：85\n至少要多完成 5 個作業'),
               table(['次數', '成績'], [['0', '70'], ['1', '73'], ['2', '76'], ['3', '79'], ['4', '82'], ['5', '86 ✔']], ['50%', '50%']), '1.6fr 1fr')
     + note('🧾 對應線上練習 <strong>#328 業績計算</strong>：結構相同，換成業績成長率。')},

    {'id': 17, 'title': 'break 與 continue', 'chapter': '第三節：while 與 break', 'bg': 'white',
     'html': title('🛑 break 跳出、⏭️ continue 跳過')
     + two_col(py('wrong = 0\nwhile True:                 # 先無限循環\n    pw = input("密碼：")\n    if pw == "":\n        continue            # 空白不算，重來\n    if pw == "fhehs2027":\n        print("登入成功")\n        break               # 跳出迴圈\n    wrong += 1\n    if wrong == 3:\n        print("拒絕存取")\n        break', '密碼驗證：錯 3 次就鎖住', ''),
               table(['指令', '作用'], [['break', '<strong>立刻結束</strong>整個迴圈'], ['continue', '<strong>跳過</strong>這一輪剩下的部分，回到迴圈開頭']], ['35%', '65%']), '1.5fr 1fr')
     + note('🔐 這就是手機、網站「錯太多次就鎖定」的基本原理，用來防止有人一直亂猜密碼（暴力破解）。')},

    {'id': 18, 'title': '常見迴圈錯誤', 'chapter': '第三節：while 與 break', 'bg': 'white',
     'html': title('🐞 迴圈常見錯誤')
     + table(['症狀', '可能原因'],
             [['少算一次（例如只加到 n−1）', 'range(1, n) 少了 +1：結束值不包含'],
              ['答案是 0 或很奇怪', '累加器放在迴圈<strong>裡面</strong>，每輪都被歸零'],
              ['乘積永遠是 0', '乘法的累乘器從 0 開始，應該從 1 開始'],
              ['程式停不下來', 'while 的條件變數沒有更新'],
              ['只印出最後一個結果', 'print 沒有縮排在迴圈裡（或反過來）']], ['40%', '60%'])
     + note('🔍 除錯法寶：在迴圈裡加一行 ' + ic('print(i, total)') + '，看每一輪變數怎麼變——就是程式版的追蹤表。')},

    {'id': 19, 'title': '第三節 隨堂測驗', 'chapter': '第三節：while 與 break', 'bg': 'purple', 'quiz': 'q3',
     'html': quiz_cover('第三節 隨堂測驗', 'while 與 break ｜ 4 題')},

    # ── 實作與總結 ──
    {'id': 20, 'title': '本週實作', 'chapter': '實作與總結', 'bg': 'white',
     'html': title('✏️ 本週實作：Colab ＋ 線上練習')
     + colab('py04_loops.ipynb', '第 4 課 Colab 練習（7 題）', '50 行 Hello、1 加到 n、累加變化題、星號三角形、九九乘法表、成績加分、密碼驗證')
     + oj([('#320、#322、#324', 'range()、for 雙重迴圈觀念（測驗）'), ('#321', 'for 練習：輸出 50 行字串（VPL）'),
           ('#323', '計算 1 加到 n 的值（VPL）'), ('#325', '印出星號三角形（VPL）'),
           ('#326、#327', 'while 練習（VPL）'), ('#328', '業績計算（VPL）')])},

    {'id': 21, 'title': '本週總結', 'chapter': '實作與總結', 'bg': 'navy',
     'html': recap('本週重點',
                   [('for + range()', '知道次數用 for；range 的結束值不包含'),
                    ('累加器', '迴圈前歸零（乘法從 1），迴圈中累加'),
                    ('雙重迴圈', '外圈控制列、內圈控制每列內容'),
                    ('while / break', '不知道次數用 while；記得更新條件')],
                   '「重複的事交給迴圈，人只要想清楚規則。」',
                   '下一章：學習挑戰——綜合題目大練兵')},
]

QUIZZES = {
    'q1': {'title': '第一節 隨堂測驗', 'questions': [
        {'q': 'range(2, 6) 會產生哪些數？',
         'options': ['2, 3, 4, 5, 6', '2, 3, 4, 5', '3, 4, 5, 6', '2, 6'],
         'answer': 1,
         'explain': 'range 的結束值「不包含」在內，所以是 2 到 5。'},
        {'q': 'range(1, 10, 3) 會產生哪些數？',
         'options': ['1, 4, 7', '1, 4, 7, 10', '3, 6, 9', '1, 3, 10'],
         'answer': 0,
         'explain': '從 1 開始每次加 3：1、4、7；下一個是 10，但結束值 10 不包含，所以停止。'},
        {'q': 'for i in range(5): print("Hi") 會印出幾次 Hi？',
         'options': ['4 次', '5 次', '6 次', '無限次'],
         'answer': 1,
         'explain': 'range(5) 產生 0、1、2、3、4 共 5 個數，迴圈執行 5 次。'},
        {'q': '想讓 i 依序是 10, 8, 6, 4, 2，應該寫？',
         'options': ['range(10, 2, -2)', 'range(10, 0, -2)', 'range(2, 10, 2)', 'range(10, 1, 2)'],
         'answer': 1,
         'explain': '間隔是 -2 代表倒數；結束值不包含，所以要寫到 0 才會包含 2。range(10, 2, -2) 只到 4。'},
    ]},
    'q2': {'title': '第二節 隨堂測驗', 'questions': [
        {'q': '以下程式輸出？\ntotal = 0\nfor i in range(1, 4):\n    total = total + i\nprint(total)',
         'options': ['3', '6', '10', '0'],
         'answer': 1,
         'explain': 'i 是 1、2、3，total 依序變成 1、3、6。'},
        {'q': '想計算 1 × 2 × 3 × 4 × 5，累乘的變數 p 一開始應該設為？',
         'options': ['0', '1', '5', '不用設定'],
         'answer': 1,
         'explain': '乘法的「起點」是 1。如果 p = 0，乘任何數都是 0。'},
        {'q': '以下程式總共會印出幾個 * ？\nfor i in range(3):\n    for j in range(4):\n        print("*", end="")',
         'options': ['7', '12', '3', '4'],
         'answer': 1,
         'explain': '外圈 3 次，每次內圈 4 次，共 3 × 4 = 12 次。'},
        {'q': '印星號三角形時，第 i 列要印 i 個 *，內圈應該寫？',
         'options': ['for j in range(5):', 'for j in range(i):', 'for j in range(n):', 'for j in range(1):'],
         'answer': 1,
         'explain': '內圈次數要跟著外圈的 i 變化，第 1 列 1 次、第 2 列 2 次…，所以是 range(i)。'},
    ]},
    'q3': {'title': '第三節 隨堂測驗', 'questions': [
        {'q': '下列程式會發生什麼事？\ni = 1\nwhile i < 5:\n    print(i)',
         'options': ['印出 1 到 4', '印出 1 到 5', '一直印 1，停不下來', '什麼都不印'],
         'answer': 2,
         'explain': '迴圈內沒有更新 i，i 永遠是 1，條件 i < 5 永遠成立，形成無窮迴圈。'},
        {'q': '下列哪個情境「最適合」用 while 迴圈？',
         'options': ['印 100 行字', '計算 1 加到 100', '一直讓使用者猜數字，直到猜對為止', '走過串列中每個元素'],
         'answer': 2,
         'explain': '猜數字不知道要猜幾次，只知道「猜對就停」，適合用 while。其他都知道次數，用 for 比較簡潔。'},
        {'q': '在迴圈中執行到 break 時會？',
         'options': ['跳過這一輪，繼續下一輪', '立刻結束整個迴圈', '程式當機', '重新開始迴圈'],
         'answer': 1,
         'explain': 'break 立刻跳出迴圈，接著執行迴圈之後的程式。跳過這一輪的是 continue。'},
        {'q': '以下程式輸出？\ni = 0\nwhile i < 10:\n    i += 3\nprint(i)',
         'options': ['9', '10', '12', '3'],
         'answer': 2,
         'explain': 'i 依序變成 3、6、9、12。i = 9 時條件仍成立，再加 3 變 12，此時 12 < 10 不成立，離開迴圈印出 12。'},
    ]},
}

QUIZZES = safe_quizzes(QUIZZES)
