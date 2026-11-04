# -*- coding: utf-8 -*-
# 第 5 週（課程計畫 W19）：學習挑戰——綜合應用題（Colab：py05_challenge）
from content._kit import *

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一節：解題方法與 Online Judge', 'start': 2},
    {'name': '第二節：計算型題目', 'start': 8},
    {'name': '第三節：判斷與迴圈型題目', 'start': 13},
    {'name': '挑戰賽與總結', 'start': 19},
]

SLIDES = [
    {'id': 1, 'title': '學習挑戰', 'chapter': '封面', 'bg': 'navy',
     'html': cover('🏆', '學習挑戰', 'Problem Solving · Online Judge · Challenge Week',
                   ['🧭 解題四步驟', '💻 Online Judge', '🧮 計算題', '🔁 迴圈題'], '第 5 週')},

    # ── 第一節 ──
    {'id': 2, 'title': '解題四步驟', 'chapter': '第一節：解題方法與 Online Judge', 'bg': 'white',
     'html': title('🧭 解題四步驟')
     + steps([('讀題：找出輸入與輸出', '輸入有幾個數？用空白還是換行隔開？輸出要什麼格式？'),
              ('舉例：自己手算 2～3 組', '用題目的範例，再自己想一組「邊界」的例子'),
              ('寫程式：先求對，再求好', '從輸入 → 處理 → 輸出，一段一段寫、一段一段測'),
              ('測試：包含特殊情況', '0、負數、剛好等於條件的值、最大值')], 'blue')
     + note('🧠 這就是<strong>運算思維</strong>：拆解問題、找出規律、抽象化、設計演算法。上學期的 Bebras 挑戰賽練的也是這些能力。')},

    {'id': 3, 'title': '認識 Online Judge', 'chapter': '第一節：解題方法與 Online Judge', 'bg': 'white',
     'html': title('💻 Online Judge：讓系統幫你改程式')
     + lead('Online Judge（線上評測系統）會用<strong>好幾組測試資料</strong>執行你的程式，比對輸出是否和標準答案<strong>完全一樣</strong>，自動給分。')
     + grid(3,
            card('green', '本課程練習網站', 'Moodle VPL<br>115芳和高中資訊科技Py<br>#301～#513', '🏫', True),
            card('blue', 'ZeroJudge', '高中生線上解題系統<br>zerojudge.tw<br>題庫最多、有排名', '⚖️', True),
            card('purple', 'APCS', '大學程式設計先修檢測<br>觀念題＋實作題<br>可作為申請入學參考', '🎓', True))
     + oj([('使用方式', '登入 → 點題目 → 編輯程式 → 「評估」看分數'), ('注意', '「評估」沒有滿分不要緊，看系統提示修正後可以再評估')],
          head='💻 本課程的線上練習網站')},

    {'id': 4, 'title': '輸出格式要一模一樣', 'chapter': '第一節：解題方法與 Online Judge', 'bg': 'white',
     'html': title('🎯 輸出要「一字不差」')
     + table(['題目要求', '你的輸出', '結果'],
             [['15', '答案是 15', '❌ 多了文字'],
              ['15', '15（後面多一個空格）', '⚠️ 有些系統會判錯'],
              ['大吉', '大 吉', '❌ 多了空白'],
              ['3.50', '3.5', '❌ 小數位數不對']], ['30%', '40%', '30%'])
     + two_col(card('red', '線上練習時', ic('input()') + ' 括號內<strong>不要寫提示字</strong>，<br>'
                    + ic('print()') + ' 只印題目要求的內容。', '🚫'),
               card('green', '小數位數', ic('print(f"{x:.2f}")') + ' → 固定 2 位小數<br>' + ic('round(x, 2)') + ' → 四捨五入到 2 位（但 3.50 會變 3.5）', '🔢'), '1fr 1fr')},

    {'id': 5, 'title': '讀懂題目格式', 'chapter': '第一節：解題方法與 Online Judge', 'bg': 'white',
     'html': title('📄 讀懂題目格式')
     + table(['題目寫法', '代表', 'Python 讀法'],
             [['一行一個整數 N', '只輸入一個數', 'n = int(input())'],
              ['一行兩個整數，以空白隔開', '同一行兩個數', 'a, b = map(int, input().split())'],
              ['第一行 n，第二行 n 個整數', '先給個數，再給一串', 'n = int(input())<br>a = list(map(int, input().split()))'],
              ['輸入有多行，每行一筆', '要讀很多次', '用 for 迴圈讀 n 次 input()']], ['32%', '24%', '44%'])
     + note('📌 第三種寫法會得到一個<strong>串列</strong>，第 6 章會詳細學。')},

    {'id': 6, 'title': '錯誤訊息看懂', 'chapter': '第一節：解題方法與 Online Judge', 'bg': 'white',
     'html': title('🧯 評測結果看不懂？')
     + table(['狀況', '意思', '常見原因'],
             [['輸出不符（Wrong Answer）', '程式能跑，答案錯', '邏輯錯、格式多空白、多了提示字'],
              ['執行錯誤（Runtime Error）', '執行到一半當掉', '輸入讀錯（ValueError）、除以 0、索引超出範圍'],
              ['逾時（Time Limit）', '跑太久', '無窮迴圈、演算法太慢'],
              ['編譯／語法錯誤', '程式本身寫錯', '少冒號、縮排錯、全形符號']], ['30%', '26%', '44%'])
     + note('💡 先在 Colab 用題目的範例測過、結果完全一樣，再貼到線上練習網站評估。')},

    {'id': 7, 'title': '第一節 隨堂測驗', 'chapter': '第一節：解題方法與 Online Judge', 'bg': 'purple', 'quiz': 'q1',
     'html': quiz_cover('第一節 隨堂測驗', '解題方法與 Online Judge ｜ 4 題')},

    # ── 第二節 ──
    {'id': 8, 'title': '梯形面積', 'chapter': '第二節：計算型題目', 'bg': 'white',
     'html': title('📐 計算題 1：梯形面積')
     + two_col(py('a = int(input())\nb = int(input())\nh = int(input())\nprint((a + b) * h / 2)', '輸入上底、下底、高', '3\n5\n4\n16.0'),
               card('blue', '想一想', '為什麼輸出是 16.0 而不是 16？<br><br>因為 / 的結果一定是 float。如果題目要整數，可以改用 '
                    + ic('(a + b) * h // 2') + '，但要小心奇數會被捨去。', '🤔'))},

    {'id': 9, 'title': '三角形與海龍公式', 'chapter': '第二節：計算型題目', 'bg': 'white',
     'html': title('🔺 計算題 2：三角形周長與面積')
     + lead('海龍公式：s = (a + b + c) / 2，面積 = √(s(s−a)(s−b)(s−c))。Python 開根號：' + ic('x ** 0.5'))
     + py('a = int(input())\nb = int(input())\nc = int(input())\nif a + b > c and a + c > b and b + c > a:\n    s = (a + b + c) / 2\n    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5\n    print("周長 =", a + b + c)\n    print("面積 =", round(area, 2))\nelse:\n    print("無法構成三角形")', '',
          '3\n4\n5\n周長 = 12\n面積 = 6.0')
     + note('🧩 計算前先<strong>檢查輸入是否合理</strong>——這個習慣在處理真實資料（第 9、10 章）時非常重要。')},

    {'id': 10, 'title': '滿千折百', 'chapter': '第二節：計算型題目', 'bg': 'white',
     'html': title('🛒 計算題 3：百貨週年慶滿千折百')
     + two_col(py('m = int(input())\nk = m // 1000          # 滿了幾個 1000\nprint(m - k * 100)', '', '2350\n2150'),
               card('green', '不用 if 也能做', '用 // 算出「滿幾個 1000」，乘以 100 就是折抵金額。'
                    '<br><br>很多題目用 // 和 % 就能處理，不一定要用判斷。', '💡'))
     + note('🧾 對應線上練習 <strong>#310 計算滿千折百後應付金額</strong>。')},

    {'id': 11, 'title': 'Sagit 計分程式', 'chapter': '第二節：計算型題目', 'bg': 'white',
     'html': title('🧮 計算題 4：Sagit\'s 計分程式（ZeroJudge a053）')
     + two_col(table(['答對題數', '計分方式'], [['0～10', '每題 6 分'], ['11～20', '前 10 題 60 分，之後每題 2 分'],
                                           ['21～40', '前 20 題 80 分，之後每題 1 分'], ['40 以上', '一律 100 分']], ['35%', '65%']),
               py('n = int(input())\nif n <= 10:\n    s = n * 6\nelif n <= 20:\n    s = 60 + (n - 10) * 2\nelif n <= 40:\n    s = 80 + (n - 20)\nelse:\n    s = 100\nprint(s)', '', '25\n85'), '1fr 1.1fr')
     + note('🔗 題目原文：zerojudge.tw 題號 a053。<strong>分段計分</strong>和電費、計程車資的算法一樣。')},

    {'id': 12, 'title': '第二節 隨堂測驗', 'chapter': '第二節：計算型題目', 'bg': 'purple', 'quiz': 'q2',
     'html': quiz_cover('第二節 隨堂測驗', '計算型題目 ｜ 3 題')},

    # ── 第三節 ──
    {'id': 13, 'title': '兩光法師占卜', 'chapter': '第三節：判斷與迴圈型題目', 'bg': 'white',
     'html': title('🔮 判斷題：兩光法師占卜術（ZeroJudge a003）')
     + two_col(py('m, d = map(int, input().split())\ns = (m * 2 + d) % 3\nif s == 0:\n    print("普通")\nelif s == 1:\n    print("吉")\nelse:\n    print("大吉")', '', '1 1\n普通'),
               card('purple', '規則', 'S = (M × 2 + D) % 3<br>S = 0 → 普通<br>S = 1 → 吉<br>S = 2 → 大吉<br><br>'
                    '% 3 的結果只可能是 0、1、2，所以 else 就是 2。', '📜'))},

    {'id': 14, 'title': '糖果分裝', 'chapter': '第三節：判斷與迴圈型題目', 'bg': 'white',
     'html': title('🍬 迴圈題 1：糖果分裝')
     + lead('最多 3000 個糖果，7 個一數餘 5、11 個一數餘 5、17 個一數餘 5，可能有幾個糖果？')
     + two_col(py('for i in range(1, 3001):\n    if i % 7 == 5 and i % 11 == 5 and i % 17 == 5:\n        print(i)', '暴力法：一個一個試', '5\n1314\n2623'),
               card('yellow', '數學觀點', '7、11、17 的最小公倍數是 1309，所以答案是 5、5 + 1309、5 + 2 × 1309。'
                    '<br><br>電腦很會「一個一個試」，這叫<strong>窮舉法（暴力法）</strong>。', '🔢'))},

    {'id': 15, 'title': '盈數虧數完全數', 'chapter': '第三節：判斷與迴圈型題目', 'bg': 'white',
     'html': title('🔍 迴圈題 2：盈數、虧數和完全數（ZeroJudge d010）')
     + two_col(py('n = int(input())\ns = 0\nfor i in range(1, n):\n    if n % i == 0:     # i 是 n 的因數\n        s += i\nif s > n:\n    print("盈數")\nelif s < n:\n    print("虧數")\nelse:\n    print("完全數")', '', '28\n完全數'),
               card('green', '迴圈＋判斷＋累加', '用迴圈把 1 到 n−1 都試一次，<br>能整除的就是因數，累加起來，<br>最後再判斷大小。'
                    '<br><br>6、28、496 都是完全數。', '🧩'))},

    {'id': 16, 'title': '儲蓄計畫', 'chapter': '第三節：判斷與迴圈型題目', 'bg': 'white',
     'html': title('💰 迴圈題 3：儲蓄計畫')
     + lead('第 1 個月存 100 元，之後每月比前月多 10%（去除小數），存到累計超過 1000 元為止。')
     + py('m = 100\ntotal = 100\ni = 1\nprint(f"第{i}個月存{m}元，共{total}元")\nwhile total <= 1000:\n    m = int(m * 1.1)\n    total += m\n    i += 1\n    print(f"第{i}個月存{m}元，共{total}元")', '',
          '第1個月存100元，共100元\n第2個月存110元，共210元\n…\n第7個月存176元，共946元\n第8個月存193元，共1139元')
     + note('🏦 這就是<strong>複利</strong>的概念；銀行存款、通膨、人口成長都可以用類似的迴圈模擬。')},

    {'id': 17, 'title': '印出長方形', 'chapter': '第三節：判斷與迴圈型題目', 'bg': 'white',
     'html': title('🧱 迴圈題 4：印出長方形')
     + two_col(py('x, y = map(int, input().split())\nfor i in range(x):\n    for j in range(y):\n        print("*", end="")\n    print()', '雙重迴圈寫法', '3 5\n*****\n*****\n*****'),
               py('x, y = map(int, input().split())\nfor i in range(x):\n    print("*" * y)', 'Python 字串重複寫法', '3 5\n*****\n*****\n*****'), '1fr 1fr')
     + note('🤔 兩種寫法結果相同。考試或線上練習，選你<strong>最有把握不出錯</strong>的寫法。')},

    {'id': 18, 'title': '第三節 隨堂測驗', 'chapter': '第三節：判斷與迴圈型題目', 'bg': 'purple', 'quiz': 'q3',
     'html': quiz_cover('第三節 隨堂測驗', '判斷與迴圈型題目 ｜ 3 題')},

    # ── 挑戰賽 ──
    {'id': 19, 'title': '挑戰賽規則', 'chapter': '挑戰賽與總結', 'bg': 'white',
     'html': title('🏁 課堂挑戰賽：出題、說題、解題、教題')
     + grid(4,
            card('blue', '① 出題', '各組抽一題（Colab 第 5 課的 9 題）', '🎲', True),
            card('green', '② 說題', '用流程圖說明解法，不急著寫程式', '🗺️', True),
            card('yellow', '③ 解題', '寫出程式，用範例和邊界值測試', '💻', True),
            card('purple', '④ 教題', '上台 3 分鐘，教會全班', '🎤', True))
     + colab('py05_challenge.ipynb', '第 5 課 Colab：學習挑戰 9 題', '梯形、絕對值、三角形、糖果、儲蓄、a053 計分、a003 占卜、d010 盈虧數、長方形')
     + rubric_box('程式正確且有測邊界值；說明清楚，同學能聽懂並照著做出來', '程式正確，說明大致清楚',
                  '程式部分正確，或說明不夠清楚', '未完成或無法說明')},

    {'id': 20, 'title': '本週總結', 'chapter': '挑戰賽與總結', 'bg': 'navy',
     'html': recap('本週重點',
                   [('解題四步驟', '讀題 → 舉例 → 寫程式 → 測試'),
                    ('Online Judge', '輸出要一字不差，input() 不寫提示字'),
                    ('常用技巧', '// 與 % 拆數字、分段計分、窮舉法'),
                    ('前 5 週', '輸出入＋運算＋選擇＋重複 = 能解很多題目了！')],
                   '「會教別人的時候，才是真的學會了。」',
                   '下一章：串列與二維串列——一次處理一整班的成績')},
]

QUIZZES = {
    'q1': {'title': '第一節 隨堂測驗', 'questions': [
        {'q': '在線上練習網站寫題目時，下列哪個寫法最可能被判錯？',
         'options': ['n = int(input())', 'n = int(input("請輸入一個整數："))', 'a, b = map(int, input().split())', 'print(n * 2)'],
         'answer': 1,
         'explain': 'input() 括號裡的提示字會被印到輸出，和標準答案不一樣就會被判錯。線上練習只印題目要求的內容。'},
        {'q': '題目說「一行輸入兩個整數，以空白隔開」，正確的讀法是？',
         'options': ['a = int(input())\nb = int(input())', 'a, b = map(int, input().split())', 'a, b = input()', 'a, b = int(input().split())'],
         'answer': 1,
         'explain': '兩個數在同一行，要先 split() 切開，再用 map(int, …) 轉成整數。分兩次 input() 會讀兩行。'},
        {'q': '程式在 Colab 能執行，送到 Online Judge 卻顯示「輸出不符」，最先該檢查什麼？',
         'options': ['電腦是否太舊', '輸出格式是否和題目範例一字不差', '網路速度', '程式是否太短'],
         'answer': 1,
         'explain': 'Wrong Answer 代表程式能跑，但輸出和標準答案不同。最常見的是多了提示字、多空白、小數位數不同。'},
        {'q': '解題四步驟中，「自己手算 2～3 組例子」的主要目的是？',
         'options': ['浪費時間', '確認自己真的懂題目，也可當成測試資料', '讓程式跑更快', '讓老師看'],
         'answer': 1,
         'explain': '手算能確認你理解規則；算出來的答案也能拿來測試程式是否正確。'},
    ]},
    'q2': {'title': '第二節 隨堂測驗', 'questions': [
        {'q': '消費 3999 元，滿千折百，應付多少？（m - (m // 1000) * 100）',
         'options': ['3599', '3699', '3899', '3999'],
         'answer': 1,
         'explain': '3999 // 1000 = 3，折 300 元，3999 − 300 = 3699。'},
        {'q': 'Python 計算 x 的平方根，下列何者正確？',
         'options': ['x ^ 0.5', 'x ** 0.5', 'sqrt x', 'x // 2'],
         'answer': 1,
         'explain': '** 是次方，開根號就是 0.5 次方。^ 在 Python 是位元運算，不是次方。也可以 import math 後用 math.sqrt(x)。'},
        {'q': 'Sagit 計分：答對 15 題得幾分？',
         'options': ['70', '80', '90', '60'],
         'answer': 0,
         'explain': '前 10 題 × 6 = 60 分，第 11～15 題共 5 題 × 2 = 10 分，合計 70 分。'},
    ]},
    'q3': {'title': '第三節 隨堂測驗', 'questions': [
        {'q': '占卜規則 S = (M*2 + D) % 3，3 月 5 日的 S 是？',
         'options': ['0', '1', '2', '11'],
         'answer': 2,
         'explain': '3 × 2 + 5 = 11，11 % 3 = 2，所以是「大吉」。'},
        {'q': '判斷 n 的因數時，條件式應該寫？',
         'options': ['i % n == 0', 'n % i == 0', 'n // i == 0', 'n / i == 1'],
         'answer': 1,
         'explain': 'i 是 n 的因數，代表 n 除以 i 沒有餘數：n % i == 0。'},
        {'q': '用 for i in range(1, 3001) 一個一個測試條件，找出所有答案，這種方法叫？',
         'options': ['二分搜尋', '窮舉法（暴力法）', '遞迴', '排序'],
         'answer': 1,
         'explain': '把所有可能都試一遍就是窮舉法。範圍不大時簡單又可靠；範圍很大時就需要更聰明的演算法。'},
    ]},
}

QUIZZES = safe_quizzes(QUIZZES)
