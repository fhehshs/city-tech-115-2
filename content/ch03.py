# -*- coding: utf-8 -*-
# 第 3 週（課程計畫 W17）：循序與選擇結構（Colab：py03_if）
from content._kit import *

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一節：結構化程式與循序結構', 'start': 2},
    {'name': '第二節：if 與 if-else', 'start': 7},
    {'name': '第三節：if-elif-else 多重選擇', 'start': 13},
    {'name': '實作與總結', 'start': 19},
]

SLIDES = [
    {'id': 1, 'title': '循序與選擇結構', 'chapter': '封面', 'bg': 'navy',
     'html': cover('🔀', '讓程式學會判斷', 'Sequence &amp; Selection Structures',
                   ['➡️ 循序', '🔁 兩數交換', '❓ if / else', '🪜 elif 多重選擇'], '第 3 週')},

    # ── 第一節 ──
    {'id': 2, 'title': '三種基本結構', 'chapter': '第一節：結構化程式與循序結構', 'bg': 'white',
     'html': title('🧱 結構化程式設計：只用三種結構')
     + grid(3,
            card('blue', '循序 Sequence', '一步一步、由上往下執行', '➡️', True),
            card('yellow', '選擇 Selection', '依條件決定走哪條路<br>if / elif / else', '🔀', True),
            card('green', '重複 Repetition', '條件成立就反覆執行<br>for / while（下週）', '🔁', True))
     + note('🧠 1966 年 Böhm 與 Jacopini 證明：<strong>任何演算法都能只用這三種結構組合出來</strong>。七年級學過的 Scratch 也是同樣的三種結構。')},

    {'id': 3, 'title': '流程圖複習', 'chapter': '第一節：結構化程式與循序結構', 'bg': 'white',
     'html': title('🗺️ 流程圖符號複習')
     + two_col(flow([('start', '開始', ''), ('io', '輸入半徑 r', ''), ('process', 'area = 3.14 * r * r', ''),
                     ('io', '輸出 area', ''), ('start', '結束', '')], 180),
               table(['形狀', '意義'],
                     [['橢圓', '開始／結束'], ['平行四邊形', '輸入／輸出'], ['矩形', '處理（計算、指定）'],
                      ['菱形', '判斷（是／否兩條路）']], ['40%', '60%']), '1fr 1fr')
     + note('✏️ 左邊就是上週「圓面積」程式的流程圖——只有循序結構，從上到下一路走完。')},

    {'id': 4, 'title': '兩數交換', 'chapter': '第一節：結構化程式與循序結構', 'bg': 'white',
     'html': title('🔄 循序結構的經典：兩數交換')
     + two_col(card('red', '❌ 錯誤寫法', ic('x = y') + '<br>' + ic('y = x') + '<br><br>x 原本的值被蓋掉了，兩個變數最後一樣。', ''),
               card('green', '✅ 用暫存變數 t', ic('t = x') + '　先把 x 存起來<br>' + ic('x = y') + '<br>' + ic('y = t') + '　再把原本的 x 給 y', ''), '1fr 1fr')
     + two_col(py('x, y = 1, 0\nt = x\nx = y\ny = t\nprint(x, y)', '想像兩杯飲料要互換，需要第三個空杯', '0 1'),
               py('x, y = 1, 0\nx, y = y, x      # Python 專屬的簡潔寫法\nprint(x, y)', '', '0 1'), '1fr 1fr')},

    {'id': 5, 'title': '追蹤程式', 'chapter': '第一節：結構化程式與循序結構', 'bg': 'white',
     'html': title('🔍 用追蹤表看懂程式')
     + lead('追蹤表（trace table）：每執行一行，就記下每個變數的值。這是除錯和寫 APCS 觀念題最有用的方法。')
     + table(['執行的程式', 'x', 'y', 't'],
             [['x, y = 1, 0', '1', '0', '—'], ['t = x', '1', '0', '1'], ['x = y', '0', '0', '1'], ['y = t', '0', '<strong>1</strong>', '1']],
             ['40%', '20%', '20%', '20%'])
     + note('📌 每一列只改變「等號左邊」那個變數，其他照抄上一列。')},

    {'id': 6, 'title': '第一節 隨堂測驗', 'chapter': '第一節：結構化程式與循序結構', 'bg': 'purple', 'quiz': 'q1',
     'html': quiz_cover('第一節 隨堂測驗', '結構化程式與循序結構 ｜ 3 題')},

    # ── 第二節 ──
    {'id': 7, 'title': 'if 語法', 'chapter': '第二節：if 與 if-else', 'bg': 'white',
     'html': title('❓ if：條件成立才執行')
     + two_col(py('age = int(input("年齡："))\nif age >= 18:\n    print("你的年齡", age)\n    print("成年")\nprint("謝謝使用")', '',
                  '年齡：20\n你的年齡 20\n成年\n謝謝使用'),
               steps([('條件式後加冒號 :', '忘了冒號會出現 SyntaxError'),
                      ('區塊要縮排', '同一區塊縮排要一樣（常用 4 格空白）'),
                      ('縮排結束 = 區塊結束', '「謝謝使用」沒有縮排，不管條件都會執行')], 'yellow'))},

    {'id': 8, 'title': '縮排的重要', 'chapter': '第二節：if 與 if-else', 'bg': 'white',
     'html': title('📏 縮排錯一格，意思就變了')
     + two_col(py('age = 10\nif age >= 18:\n    print("你的年齡", age)\n    print("成年")', '兩行都縮排：條件不成立，兩行都不執行', ''),
               py('age = 10\nif age >= 18:\n    print("你的年齡", age)\nprint("成年")', '只縮排一行：「成年」一定會被印出來', '成年'), '1fr 1fr')
     + note('⚠️ 第二個程式沒有語法錯誤，卻輸出了錯的結果——這叫<strong>語意錯誤（邏輯錯誤）</strong>，電腦不會提醒你，最難抓！', 'red', '')},

    {'id': 9, 'title': 'if-else 二選一', 'chapter': '第二節：if 與 if-else', 'bg': 'white',
     'html': title('🔀 if - else：二選一')
     + two_col(flow([('io', '輸入 n', ''), ('decision', 'n % 2 == 0 ?', '是 → 偶數；否 → 奇數'), ('io', '輸出結果', '')], 170),
               py('n = int(input("n="))\nif n % 2 == 0:\n    print("偶數")\nelse:\n    print("奇數")', '判斷奇偶數', 'n=7\n奇數'), '1fr 1.1fr')
     + note('💡 else 後面<strong>不寫條件</strong>，代表「以上都不成立的其他情況」，也要加冒號。')},

    {'id': 10, 'title': '範例：自動加分', 'chapter': '第二節：if 與 if-else', 'bg': 'white',
     'html': title('🎁 範例：59 分自動加 1 分')
     + two_col(py('s = int(input("成績："))\nif s == 59:\n    s = s + 1\nprint("最後成績", s)', '只有 if、沒有 else 也可以', '成績：59\n最後成績 60'),
               card('blue', '想一想', '如果改成「55～59 分一律變 60 分」，條件式要怎麼寫？<br><br>'
                    + ic('if s >= 55 and s <= 59:') + '<br>　' + ic('s = 60'), '🤔'))
     + note('🧾 對應線上練習 <strong>#317 自動加 1 元</strong>：題目情境不同，結構完全一樣。')},

    {'id': 11, 'title': '範例：三數最大', 'chapter': '第二節：if 與 if-else', 'bg': 'white',
     'html': title('🏆 範例：三個數找最大（打擂台法）')
     + two_col(py('a, b, c = map(int, input().split())\nmx = a              # 先讓 a 當擂台主\nif b > mx:\n    mx = b\nif c > mx:\n    mx = c\nprint("最大數", mx)', '',
                  '85 92 78\n最大數 92'),
               card('green', '打擂台法', '① 先假設第一個最大<br>② 後面的人一個一個上台挑戰<br>③ 比擂台主大就換人<br><br>'
                    '這個想法第 6 章處理「一整串成績」時會再用到！', '🥊'))
     + note('🧾 對應線上練習 <strong>#318 計算最高銷量</strong>。')},

    {'id': 12, 'title': '第二節 隨堂測驗', 'chapter': '第二節：if 與 if-else', 'bg': 'purple', 'quiz': 'q2',
     'html': quiz_cover('第二節 隨堂測驗', 'if 與 if-else ｜ 4 題')},

    # ── 第三節 ──
    {'id': 13, 'title': 'if-elif-else', 'chapter': '第三節：if-elif-else 多重選擇', 'bg': 'white',
     'html': title('🪜 if - elif - else：多選一')
     + lead('elif ＝ else if。程式<strong>由上往下</strong>檢查，遇到<strong>第一個成立</strong>的條件就執行它，其餘全部跳過。')
     + two_col(py('s = int(input("成績："))\nif s >= 90:\n    print("優")\nelif s >= 80:\n    print("甲")\nelif s >= 70:\n    print("乙")\nelif s >= 60:\n    print("丙")\nelse:\n    print("丁")', '成績等第',
                  '成績：85\n甲'),
               card('yellow', '為什麼 elif s >= 80 就夠？', '能走到這一行，代表上面的 ' + ic('s >= 90') + ' 不成立，'
                    '也就是 s &lt; 90 已經確定了，所以不用再寫 ' + ic('s < 90') + '。', '💡'))},

    {'id': 14, 'title': '條件的順序', 'chapter': '第三節：if-elif-else 多重選擇', 'bg': 'white',
     'html': title('⚠️ 條件順序寫反會怎樣？')
     + two_col(py('s = 95\nif s >= 60:\n    print("丙")\nelif s >= 70:\n    print("乙")\nelif s >= 90:\n    print("優")', '從小的條件開始判斷', '丙'),
               card('red', '95 分竟然是丙！', '因為 95 >= 60 第一個成立，後面就不檢查了。<br><br>'
                    '<strong>規則：用 >= 判斷時，從大的往小的寫</strong>；用 &lt; 判斷時則從小的往大的寫。', '😱'), '1fr 1fr')
     + note('🧪 測試時一定要試<strong>邊界值</strong>：剛好 90、89、60、59、0、100。')},

    {'id': 15, 'title': '範例：購物折扣', 'chapter': '第三節：if-elif-else 多重選擇', 'bg': 'white',
     'html': title('🛍️ 範例：購物節折扣')
     + two_col(table(['購物金額', '折扣'], [['4000 以上', '8 折'], ['3000 以上', '85 折'], ['2000 以上', '9 折'],
                                        ['1000 以上', '95 折'], ['未滿 1000', '不打折']], ['55%', '45%']),
               py('m = int(input("購物金額："))\nif m >= 4000:\n    m = m * 0.8\nelif m >= 3000:\n    m = m * 0.85\nelif m >= 2000:\n    m = m * 0.9\nelif m >= 1000:\n    m = m * 0.95\nprint("實付", int(m))', '',
                  '購物金額：3200\n實付 2720'), '1fr 1.3fr')
     + note('🧾 對應線上練習 <strong>#319 購物折扣計算</strong>。')},

    {'id': 16, 'title': '範例：BMI', 'chapter': '第三節：if-elif-else 多重選擇', 'bg': 'white',
     'html': title('⚖️ 範例：BMI 判定')
     + two_col(py('h = float(input("身高(cm)：")) / 100\nw = float(input("體重(kg)："))\nbmi = w / (h * h)\nprint(f"BMI = {bmi:.2f}")\nif bmi < 18.5:\n    print("過輕")\nelif bmi < 24:\n    print("正常範圍")\nelif bmi < 27:\n    print("過重")\nelse:\n    print("肥胖")', '',
                  '身高(cm)：165\n體重(kg)：55\nBMI = 20.20\n正常範圍'),
               table(['BMI', '判定'], [['&lt; 18.5', '過輕'], ['18.5 ～ &lt; 24', '正常範圍'], ['24 ～ &lt; 27', '過重'], ['≥ 27', '肥胖']], ['55%', '45%']), '1.3fr 1fr')
     + note('🇹🇼 標準：衛生福利部國民健康署成人肥胖定義。這裡用 &lt; 判斷，所以條件<strong>從小的往大的</strong>寫。')},

    {'id': 17, 'title': '巢狀 if', 'chapter': '第三節：if-elif-else 多重選擇', 'bg': 'white',
     'html': title('🪆 巢狀 if：if 裡面還有 if')
     + two_col(py('a, b, c = map(int, input().split())\nif a + b > c and a + c > b and b + c > a:\n    if a == b == c:\n        print("正三角形")\n    elif a == b or b == c or a == c:\n        print("等腰三角形")\n    else:\n        print("一般三角形")\nelse:\n    print("無法構成三角形")', '',
                  '3 3 5\n等腰三角形'),
               card('purple', '先大後小', '先判斷「能不能成為三角形」，成立之後才判斷是哪一種。<br><br>'
                    '縮排的層次就是邏輯的層次：內層的 if 屬於外層 if 的區塊。', '🧩'))},

    {'id': 18, 'title': '第三節 隨堂測驗', 'chapter': '第三節：if-elif-else 多重選擇', 'bg': 'purple', 'quiz': 'q3',
     'html': quiz_cover('第三節 隨堂測驗', 'if-elif-else ｜ 4 題')},

    # ── 實作與總結 ──
    {'id': 19, 'title': '本週實作', 'chapter': '實作與總結', 'bg': 'white',
     'html': title('✏️ 本週實作：Colab ＋ 線上練習')
     + colab('py03_if.ipynb', '第 3 課 Colab 練習（7 題）', '兩數交換、奇偶數、59 分加 1 分、三數最大、成績等第、購物折扣、BMI')
     + oj([('#314', '循序結構（測驗）'), ('#315', '兩數交換（VPL）'), ('#316', '選擇結構（測驗）'),
           ('#317', '自動加 1 元（VPL）'), ('#318', '計算最高銷量（VPL）'), ('#319', '購物折扣計算（VPL）')])
     + rubric_box('全部正確，並用邊界值測試過（截圖或註解說明測了哪些值）', '全部能執行且結果正確',
                  '大部分完成，少數條件判斷有誤', '完成一半以下')},

    {'id': 20, 'title': '本週總結', 'chapter': '實作與總結', 'bg': 'navy',
     'html': recap('本週重點',
                   [('循序結構', '由上往下執行；兩數交換要用暫存變數'),
                    ('if / else', '條件後加冒號、區塊要縮排'),
                    ('elif', '第一個成立就執行，其餘跳過；注意順序'),
                    ('測試', '一定要試邊界值，抓出邏輯錯誤')],
                   '「電腦永遠照你寫的做，不是照你想的做。」',
                   '下一章：for 與 while 迴圈——讓程式不怕重複')},
]

QUIZZES = {
    'q1': {'title': '第一節 隨堂測驗', 'questions': [
        {'q': '結構化程式設計的三種基本結構是？',
         'options': ['輸入、處理、輸出', '循序、選擇、重複', '變數、函式、串列', '編譯、執行、除錯'],
         'answer': 1,
         'explain': '任何演算法都能用循序（依序執行）、選擇（依條件分支）、重複（迴圈）這三種結構組合出來。'},
        {'q': '流程圖中，「菱形」代表什麼？',
         'options': ['開始／結束', '輸入／輸出', '處理', '判斷（決策）'],
         'answer': 3,
         'explain': '菱形是判斷符號，會依條件分出「是／否」兩條路，對應程式的 if。'},
        {'q': 'x = 5, y = 8，執行 t = x、x = y、y = t 後，x、y 依序是？',
         'options': ['5, 8', '8, 5', '8, 8', '5, 5'],
         'answer': 1,
         'explain': 't 先暫存 x 的 5，x 改成 8，最後 y 拿到 t 的 5。兩數成功交換。'},
    ]},
    'q2': {'title': '第二節 隨堂測驗', 'questions': [
        {'q': '下列哪一行 if 敘述的寫法正確？',
         'options': ['if score >= 60', 'if score >= 60:', 'if (score >= 60) then:', 'if score => 60:'],
         'answer': 1,
         'explain': 'Python 的 if 條件後要加冒號；大於等於是 >=（不是 =>）；不需要 then。括號可加可不加。'},
        {'q': '以下程式輸出什麼？\nage = 10\nif age >= 18:\n    print("A")\nprint("B")',
         'options': ['A', 'B', 'A 和 B', '什麼都不印'],
         'answer': 1,
         'explain': '條件不成立，縮排的 print("A") 不執行；print("B") 沒有縮排，不屬於 if 區塊，一定會執行。'},
        {'q': '判斷 n 是奇數還是偶數，else 區塊在什麼時候執行？',
         'options': ['n % 2 == 0 成立時', 'n % 2 == 0 不成立時', '一定會執行', '永遠不執行'],
         'answer': 1,
         'explain': 'else 是 if 條件「不成立」時才執行的區塊。if 和 else 兩個區塊一定剛好執行其中一個。'},
        {'q': '程式沒有出現錯誤訊息，但輸出的結果不對，這叫做？',
         'options': ['語法錯誤', '語意（邏輯）錯誤', '網路錯誤', '硬體錯誤'],
         'answer': 1,
         'explain': '語法錯誤電腦會直接報錯；語意錯誤的程式能執行，只是結果不是你要的，例如縮排錯一格。要靠測試和追蹤才找得到。'},
    ]},
    'q3': {'title': '第三節 隨堂測驗', 'questions': [
        {'q': 's = 85，下列程式輸出？\nif s >= 90: print("優")\nelif s >= 80: print("甲")\nelif s >= 70: print("乙")\nelse: print("丙")',
         'options': ['優', '甲', '甲 和 乙', '丙'],
         'answer': 1,
         'explain': '85 >= 90 不成立；85 >= 80 成立，印出「甲」後就跳出整個 if-elif-else，不會再檢查 >= 70。'},
        {'q': 's = 95，下列程式輸出？\nif s >= 60: print("丙")\nelif s >= 90: print("優")',
         'options': ['丙', '優', '丙 和 優', '什麼都不印'],
         'answer': 0,
         'explain': '95 >= 60 第一個成立，印出「丙」後就結束了。這就是條件順序寫反造成的邏輯錯誤，應該從大的條件開始判斷。'},
        {'q': '購物滿 1000 打 95 折、滿 2000 打 9 折。消費 2500 元時，正確的判斷順序是？',
         'options': ['先判斷 >= 1000，再判斷 >= 2000', '先判斷 >= 2000，再判斷 >= 1000', '順序不影響結果', '要用兩個獨立的 if 都執行'],
         'answer': 1,
         'explain': '2500 同時滿足 >= 1000 和 >= 2000。要讓它得到 9 折，必須先檢查 >= 2000。'},
        {'q': '測試成績等第程式時，下列哪一組測試值「最」能找出錯誤？',
         'options': ['50, 75, 95', '90, 89, 80, 79, 60, 59', '1, 2, 3', '100, 100, 100'],
         'answer': 1,
         'explain': '錯誤最常發生在條件的邊界（例如 >= 和 > 寫錯）。剛好等於分界值以及差 1 的值，最容易發現問題。'},
    ]},
}

QUIZZES = safe_quizzes(QUIZZES)
