# -*- coding: utf-8 -*-
# 第 2 週（課程計畫 W16）：變數、資料型態與運算子（Colab：py02_variables）
from content._kit import *

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一節：變數與資料型態', 'start': 2},
    {'name': '第二節：指定與算術運算', 'start': 8},
    {'name': '第三節：關係與邏輯運算', 'start': 14},
    {'name': '實作與總結', 'start': 19},
]

SLIDES = [
    {'id': 1, 'title': '變數與運算子', 'chapter': '封面', 'bg': 'navy',
     'html': cover('🧮', '變數與運算子', 'Variables · Data Types · Operators',
                   ['📦 變數', '🔢 int / float / str / bool', '➗ // 與 %', '⚖️ and / or / not'], '第 2 週')},

    # ── 第一節 ──
    {'id': 2, 'title': '變數是什麼', 'chapter': '第一節：變數與資料型態', 'bg': 'white',
     'html': title('📦 變數：貼了名字的盒子')
     + two_col(card('blue', '比喻', '變數就像貼了標籤的置物盒：標籤是<strong>變數名稱</strong>，盒子裡放的是<strong>值</strong>。'
                    '<br>需要時叫名字就能拿出來用，也可以換放別的東西。', '🗃️'),
               py('score = 85\nname = "小安"\nprint(name, score)\nscore = 90      # 換成新的值\nprint(name, score)', '', '小安 85\n小安 90'))
     + note('💡 變數在電腦裡其實是一塊<strong>記憶體空間</strong>，名稱讓我們不用記住記憶體位址。')},

    {'id': 3, 'title': '變數命名規則', 'chapter': '第一節：變數與資料型態', 'bg': 'white',
     'html': title('🏷️ 變數命名規則')
     + table(['規則', '✅ 可以', '❌ 不行'],
             [['第 1 個字是英文字母或底線 _', 'score、_tmp', '2nd、$money'],
              ['之後可以是字母、數字、底線', 'score2、max_score', 'max-score（減號）、my score（空格）'],
              ['大小寫視為不同', 'Score 和 score 是兩個變數', '—'],
              ['不能用保留字', 'total、count', 'if、for、while、class、True']],
             ['38%', '31%', '31%'])
     + note('✨ 好名字要「看得懂」：' + ic('bmi') + '、' + ic('total_price') + ' 比 ' + ic('a') + '、' + ic('x1')
            + ' 好。也別用 ' + ic('sum') + '、' + ic('max') + '、' + ic('print') + ' 這些內建函式名稱當變數，會把它們蓋掉。', 'yellow', '')},

    {'id': 4, 'title': '四種基本資料型態', 'chapter': '第一節：變數與資料型態', 'bg': 'white',
     'html': title('🔢 四種基本資料型態')
     + grid(4,
            card('blue', 'int 整數', ic('16') + '、' + ic('-3') + '<br>座號、人數、年份', '1️⃣', True),
            card('green', 'float 浮點數', ic('3.14') + '、' + ic('2.0') + '<br>身高、成績平均', '🌊', True),
            card('yellow', 'str 字串', ic('"台北"') + '、' + ic("'A'") + '<br>姓名、地址', '🔤', True),
            card('purple', 'bool 布林', ic('True') + '、' + ic('False') + '<br>是否及格', '✅', True))
     + py('print(type(2), type(2.0), type("2"), type(True))', '用 type() 查型態',
          "<class 'int'> <class 'float'> <class 'str'> <class 'bool'>")
     + note('⚠️ ' + ic('2') + ' 是整數、' + ic('2.0') + ' 是浮點數、' + ic('"2"') + ' 是字串——看起來像，電腦卻當成完全不同的東西。', 'red', '')},

    {'id': 5, 'title': '型態轉換', 'chapter': '第一節：變數與資料型態', 'bg': 'white',
     'html': title('🔄 型態轉換：int()、float()、str()')
     + two_col(py('a = input("輸入一個數字：")   # 輸入 5\nprint(a + a)\nprint(int(a) + int(a))', '', '55\n10'),
               table(['函式', '轉成', '例子'],
                     [['int()', '整數', 'int("16") → 16<br>int(3.9) → 3（直接捨去）'],
                      ['float()', '浮點數', 'float("1.5") → 1.5'],
                      ['str()', '字串', 'str(16) → "16"']], ['22%', '20%', '58%']))
     + note('🔑 公式：<strong>要計算的輸入 → 先轉型</strong>。' + ic('h = float(input("身高："))') + '。輸入 "abc" 再 int() 會出現 ValueError。')},

    {'id': 6, 'title': '一次輸入多個數', 'chapter': '第一節：變數與資料型態', 'bg': 'white',
     'html': title('⌨️ 進階：一行輸入多個數字')
     + py('a, b = map(int, input("輸入兩個整數（空白隔開）：").split())\nprint(a + b)', '線上練習的題目常常這樣輸入', '輸入兩個整數（空白隔開）：3 5\n8')
     + steps([('input()', '讀到字串 "3 5"'),
              ('.split()', '依空白切開 → ["3", "5"]'),
              ('map(int, …)', '把每一個都轉成整數'),
              ('a, b = …', '依序存進 a 和 b')], 'teal')
     + note('📌 先會用就好，第 6 章學串列後會更清楚它的原理。')},

    {'id': 7, 'title': '第一節 隨堂測驗', 'chapter': '第一節：變數與資料型態', 'bg': 'purple', 'quiz': 'q1',
     'html': quiz_cover('第一節 隨堂測驗', '變數與資料型態 ｜ 4 題')},

    # ── 第二節 ──
    {'id': 8, 'title': '指定運算', 'chapter': '第二節：指定與算術運算', 'bg': 'white',
     'html': title('⬅️ 指定運算 = ：不是數學的等於')
     + lead('<strong>= 是「把右邊算好的值，存進左邊的變數」</strong>。所以 ' + ic('total = total + 3') + ' 在數學上不成立，在程式裡卻很常見：把 total 加 3 再存回去。')
     + two_col(py('total = 0\ntotal = total + 3\ntotal += 5      # 等於 total = total + 5\nprint(total)', '', '8'),
               table(['簡寫', '等於'], [['x += 2', 'x = x + 2'], ['x -= 2', 'x = x - 2'], ['x *= 2', 'x = x * 2'],
                                       ['x //= 2', 'x = x // 2']], ['45%', '55%']))},

    {'id': 9, 'title': '想一想：交換', 'chapter': '第二節：指定與算術運算', 'bg': 'white',
     'html': title('🤔 想一想：x、y 的值是多少？')
     + two_col(py('x = 1\ny = 0\nx = y\ny = x\nprint(x, y)', '', '0 0'),
               card('orange', '為什麼不是 0 1？', '程式<strong>一行一行依序執行</strong>：<br>① x = y → x 變成 0（原本的 1 被蓋掉了）'
                    '<br>② y = x → y 拿到的是「新的」x，也就是 0<br><br>想交換兩個變數，下週會學到正確寫法。', '💡'))
     + note('🧠 這就是<strong>循序結構</strong>：先寫的先做，後面的指令看到的是前面執行完的結果。')},

    {'id': 10, 'title': '算術運算子', 'chapter': '第二節：指定與算術運算', 'bg': 'white',
     'html': title('➗ 算術運算子')
     + table(['運算子', '意義', '例子', '結果'],
             [['+  -  *', '加、減、乘', '7 * 2', '14'],
              ['/', '除法（結果一定是 float）', '7 / 2', '3.5'],
              ['//', '整數除法（取商）', '7 // 2', '3'],
              ['%', '取餘數', '7 % 2', '1'],
              ['**', '次方', '2 ** 10 ／ 16 ** 0.5', '1024 ／ 4.0']], ['16%', '40%', '24%', '20%'])
     + note('📐 優先順序：<strong>** → * / // % → + -</strong>，同級由左到右；不確定就加括號。例：' + ic('3 * 5 % 2 - 1') + ' = 15 % 2 - 1 = 1 - 1 = <strong>0</strong>')},

    {'id': 11, 'title': '// 和 % 的妙用', 'chapter': '第二節：指定與算術運算', 'bg': 'white',
     'html': title('🧩 // 和 % 的妙用')
     + grid(3,
            card('blue', '幾打幾支', '30 支筆，一打 12 支<br>30 // 12 = <strong>2 打</strong><br>30 % 12 = <strong>6 支</strong>', '✏️'),
            card('green', '判斷奇偶', 'n % 2 == 0 → 偶數<br>n % 2 == 1 → 奇數<br>（下週 if 會用到）', '🎲'),
            card('yellow', '拆數字', '1234 % 10 = <strong>4</strong>（個位）<br>1234 // 10 = <strong>123</strong>（去掉個位）', '🔢'))
     + py('m = int(input("消費金額："))      # 例如 2350\nprint("折抵", (m // 1000) * 100, "元")\nprint("應付", m - (m // 1000) * 100, "元")',
          '滿千折百：每滿 1000 元折 100 元', '消費金額：2350\n折抵 200 元\n應付 2150 元')},

    {'id': 12, 'title': '實作示範：圓面積', 'chapter': '第二節：指定與算術運算', 'bg': 'white',
     'html': title('⭕ 實作示範：輸入半徑，算面積與周長')
     + two_col(py('pi = 3.14\nr = float(input("請輸入半徑："))\narea = pi * r * r\nperi = 2 * pi * r\nprint("面積", area)\nprint(f"周長 {peri:.2f}")', '',
                  '請輸入半徑：2\n面積 12.56\n周長 12.56'),
               steps([('輸入', '半徑可能有小數 → float()'), ('處理', '面積 πr²、周長 2πr'), ('輸出', '用 f"{x:.2f}" 控制小數 2 位')], 'blue'))
     + note('💡 Python 也有精確的圓周率：' + ic('import math') + ' 之後用 ' + ic('math.pi') + '。')},

    {'id': 13, 'title': '第二節 隨堂測驗', 'chapter': '第二節：指定與算術運算', 'bg': 'purple', 'quiz': 'q2',
     'html': quiz_cover('第二節 隨堂測驗', '指定與算術運算 ｜ 5 題')},

    # ── 第三節 ──
    {'id': 14, 'title': '關係運算子', 'chapter': '第三節：關係與邏輯運算', 'bg': 'white',
     'html': title('⚖️ 關係運算子：比較的結果是 True / False')
     + two_col(table(['運算子', '意義', 'a=3, b=5'],
                     [['>', '大於', 'a > b → False'], ['>=', '大於等於', 'a >= 3 → True'], ['<', '小於', 'a < b → True'],
                      ['<=', '小於等於', 'b <= 4 → False'], ['==', '等於', 'a == b → False'], ['!=', '不等於', 'a != b → True']],
                     ['22%', '30%', '48%']),
               card('red', '= 和 == 不一樣！', ic('a = 3') + '：把 3 存進 a（指定）<br>' + ic('a == 3') + '：問「a 等於 3 嗎？」（比較）'
                    '<br><br>寫 ' + ic('if a = 3:') + ' 會出現 SyntaxError。', '⚠️'), '1.3fr 1fr')},

    {'id': 15, 'title': '邏輯運算子', 'chapter': '第三節：關係與邏輯運算', 'bg': 'white',
     'html': title('🔗 邏輯運算子：and、or、not')
     + table(['運算子', '意義', '例子', '結果'],
             [['and', '兩個都成立才 True', '1 &lt; 7 and 3 &lt; 10', 'True'],
              ['or', '至少一個成立就 True', '5 &lt; 7 or 3 > 10', 'True'],
              ['not', '相反', 'not 3 * 2 == 6', 'False']], ['16%', '34%', '32%', '18%'])
     + note('🍱 生活例子：「有帶學生證 <strong>and</strong> 有預約」才能進圖書館研討室；「下雨 <strong>or</strong> AQI 超過 100」體育課就改在室內。')},

    {'id': 16, 'title': '數學式轉成程式', 'chapter': '第三節：關係與邏輯運算', 'bg': 'white',
     'html': title('✍️ 把數學條件翻譯成程式')
     + table(['數學／中文', 'Python 條件式'],
             [['80 ≤ s ≤ 89', 's >= 80 and s &lt;= 89（也可寫 80 &lt;= s &lt;= 89）'],
              ['n 是偶數', 'n % 2 == 0'],
              ['n 不能被 3 整除', 'n % 3 != 0'],
              ['n 是偶數但不是 3 的倍數', 'n % 2 == 0 and n % 3 != 0'],
              ['a、b、c 能構成三角形', 'a + b > c and b + c > a and a + c > b'],
              ['閏年', '(y % 4 == 0 and y % 100 != 0) or y % 400 == 0']], ['40%', '60%'])
     + note('📌 這些條件式下週會放進 <strong>if</strong>，讓程式依條件做不同的事。')},

    {'id': 17, 'title': '運算綜合練習', 'chapter': '第三節：關係與邏輯運算', 'bg': 'white',
     'html': title('🧠 綜合：先猜再執行')
     + py('x, y = 1, 2\nprint(x != y)\nprint("x + y =", x + y)\nprint(x > 0 and y > 5)\nprint(not (x == 1))\nprint(10 % 3 == 1 or 10 // 3 == 4)',
          '把答案先寫在紙上，再到 Colab 驗證', 'True\nx + y = 3\nFalse\nFalse\nTrue')
     + note('🎯 會「預測程式的輸出」是 APCS 觀念題的核心能力，也是除錯的基本功。')},

    {'id': 18, 'title': '第三節 隨堂測驗', 'chapter': '第三節：關係與邏輯運算', 'bg': 'purple', 'quiz': 'q3',
     'html': quiz_cover('第三節 隨堂測驗', '關係與邏輯運算 ｜ 4 題')},

    # ── 實作與總結 ──
    {'id': 19, 'title': '本週實作', 'chapter': '實作與總結', 'bg': 'white',
     'html': title('✏️ 本週實作：Colab ＋ 線上練習')
     + colab('py02_variables.ipynb', '第 2 課 Colab 練習（9 題）',
             '兩科成績、指定運算、算術預測、圓面積、英呎換公分、幾打幾支、滿千折百、關係運算、條件式')
     + oj([('#305–#306', '程式執行的概念、變數和基本資料型態（測驗）'), ('#307', '計算兩銷量之和（VPL）'),
           ('#308–#309', '指定運算、算術運算子（測驗）'), ('#310', '計算滿千折百後應付金額（VPL）'),
           ('#311', '計算銷量總和與平均銷量（VPL）'), ('#312–#313', '關係運算子、邏輯運算子（測驗）')])},

    {'id': 20, 'title': '本週總結', 'chapter': '實作與總結', 'bg': 'navy',
     'html': recap('本週重點',
                   [('變數', '有名字的記憶體空間；命名要有意義、不用保留字'),
                    ('資料型態', 'int、float、str、bool；input() 要轉型才能算'),
                    ('算術', '/ 得小數、// 取商、% 取餘數、** 次方'),
                    ('比較與邏輯', '== 是比較、= 是指定；and / or / not 組合條件')],
                   '「先猜輸出，再按執行」——每次都這樣做，進步最快。',
                   '下一章：循序與選擇結構——讓程式學會「判斷」')},
]

QUIZZES = {
    'q1': {'title': '第一節 隨堂測驗', 'questions': [
        {'q': '下列哪一個是「合法」的 Python 變數名稱？',
         'options': ['2score', 'max-score', 'max_score', 'for'],
         'answer': 2,
         'explain': '變數名稱不能以數字開頭（2score）、不能有減號（max-score 會被當成 max 減 score）、不能用保留字（for）。底線是可以的。'},
        {'q': 'type(2.0) 的結果是？',
         'options': ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'bool'>"],
         'answer': 1,
         'explain': '有小數點的數字就是浮點數 float，即使小數部分是 0。'},
        {'q': 'a = input()，使用者輸入 5，print(a + a) 的結果是？',
         'options': ['10', '55', '5 5', '錯誤'],
         'answer': 1,
         'explain': 'input() 得到字串 "5"，字串相加是「接起來」，所以是 "55"。要得到 10 必須寫 int(a) + int(a)。'},
        {'q': 'int(3.9) 的結果是？',
         'options': ['4', '3', '3.9', '錯誤'],
         'answer': 1,
         'explain': 'int() 把浮點數轉整數時會直接捨去小數部分（不是四捨五入），所以是 3。要四捨五入可以用 round()。'},
    ]},
    'q2': {'title': '第二節 隨堂測驗', 'questions': [
        {'q': 'total = 0，依序執行 total = total + 3、total += 5 之後，total 是？',
         'options': ['3', '5', '8', '0'],
         'answer': 2,
         'explain': '先變成 0 + 3 = 3，再 3 + 5 = 8。total += 5 是 total = total + 5 的簡寫。'},
        {'q': '7 / 2、7 // 2、7 % 2 的結果依序是？',
         'options': ['3.5、3、1', '3、3、1', '3.5、3.5、1', '3.5、4、1'],
         'answer': 0,
         'explain': '/ 是一般除法，結果是浮點數 3.5；// 取商得 3；% 取餘數得 1。'},
        {'q': 'x = 3 * 5 % 2 - 1，x 的值是？',
         'options': ['0', '-1', '4', '7'],
         'answer': 0,
         'explain': '* 和 % 同級，由左到右：3 * 5 = 15，15 % 2 = 1，最後 1 - 1 = 0。'},
        {'q': '有 50 顆糖果，每袋裝 12 顆，要算「裝滿幾袋、剩幾顆」，正確的運算是？',
         'options': ['50 / 12 和 50 * 12', '50 // 12 和 50 % 12', '50 % 12 和 50 // 12', '50 - 12 和 50 + 12'],
         'answer': 1,
         'explain': '50 // 12 = 4（裝滿 4 袋），50 % 12 = 2（剩 2 顆）。'},
        {'q': 'x = 1, y = 0，執行 x = y 再執行 y = x 後，(x, y) 是？',
         'options': ['(0, 1)', '(1, 0)', '(0, 0)', '(1, 1)'],
         'answer': 2,
         'explain': '程式依序執行：x = y 讓 x 變成 0；y = x 時 x 已經是 0，所以 y 也是 0。原本 x 的 1 已經被蓋掉了。'},
    ]},
    'q3': {'title': '第三節 隨堂測驗', 'questions': [
        {'q': '想判斷變數 a 是否等於 3，應該寫？',
         'options': ['a = 3', 'a == 3', 'a := 3', 'a === 3'],
         'answer': 1,
         'explain': '比較是否相等用兩個等號 ==。一個等號 = 是指定運算，會把 3 存進 a。'},
        {'q': '「成績 s 在 80 到 89 之間（含）」的正確條件式是？',
         'options': ['s >= 80 or s <= 89', 's > 80 and s < 89', 's >= 80 and s <= 89', '80 >= s <= 89'],
         'answer': 2,
         'explain': '兩個條件都要成立，用 and；含 80 和 89 所以用 >= 和 <=。用 or 的話，任何數都會成立。'},
        {'q': 'not (5 > 3) or 2 == 2 的結果是？',
         'options': ['True', 'False', '錯誤', '2'],
         'answer': 0,
         'explain': 'not (5 > 3) 是 not True = False；2 == 2 是 True；False or True = True。'},
        {'q': '「n 可以被 2 整除，但不能被 3 整除」的條件式是？',
         'options': ['n % 2 == 0 or n % 3 != 0', 'n % 2 == 0 and n % 3 != 0', 'n / 2 == 0 and n / 3 != 0', 'n // 2 == 0 and n // 3 == 0'],
         'answer': 1,
         'explain': '「被 2 整除」是餘數為 0：n % 2 == 0；「不能被 3 整除」是 n % 3 != 0；「但」表示兩者都要成立，用 and。'},
    ]},
}

QUIZZES = safe_quizzes(QUIZZES)
