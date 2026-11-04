# -*- coding: utf-8 -*-
# 第 11 週：函式與遞迴（Colab：py08_function）
from content._kit import *

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一節：內建函式與自訂函式', 'start': 2},
    {'name': '第二節：參數、回傳值與範圍', 'start': 7},
    {'name': '第三節：遞迴', 'start': 12},
    {'name': '實作與總結', 'start': 19},
]

SLIDES = [
    {'id': 1, 'title': '函式與遞迴', 'chapter': '封面', 'bg': 'navy',
     'html': cover('🧩', '函式與遞迴', 'Functions · Parameters · Return · Recursion',
                   ['🧰 def', '📥 參數', '📤 return', '🪞 遞迴'], '第 11 週')},

    # ── 第一節 ──
    {'id': 2, 'title': '你早就在用函式', 'chapter': '第一節：內建函式與自訂函式', 'bg': 'white',
     'html': title('🧰 其實你早就在用函式了')
     + table(['內建函式', '做什麼', '回傳'],
             [['print(x)', '輸出', '（沒有回傳值）'], ['input(提示)', '讀取輸入', '字串'], ['int(x)、float(x)', '轉換型態', '數字'],
              ['len(a)', '求長度', '整數'], ['max(a)、min(a)、sum(a)', '最大、最小、總和', '數字'], ['range(n)', '產生數列', '一串數字']],
             ['36%', '34%', '30%'])
     + note('📦 函式就像<strong>販賣機</strong>：投入東西（參數），按下按鈕（呼叫），掉出結果（回傳值）。你不用知道裡面怎麼運作，會用就好。')},

    {'id': 3, 'title': '為什麼要自訂函式', 'chapter': '第一節：內建函式與自訂函式', 'bg': 'white',
     'html': title('🤔 為什麼要自己寫函式？')
     + grid(3,
            card('blue', '不重複', '同樣的程式寫一次，到處呼叫', '♻️', True),
            card('green', '好維護', '要改只改一個地方', '🛠️', True),
            card('purple', '好分工', '大問題拆成小函式，組員各寫各的', '👥', True))
     + note('🧠 這就是運算思維的<strong>拆解（decomposition）</strong>與<strong>抽象化（abstraction）</strong>：把複雜的事包成一個有名字的工具。')},

    {'id': 4, 'title': 'def 語法', 'chapter': '第一節：內建函式與自訂函式', 'bg': 'white',
     'html': title('✍️ 用 def 定義函式')
     + two_col(py('def 函式名稱(參數1, 參數2):\n    函式主體（要縮排）\n    return 回傳值        # 沒有回傳值可省略', '語法'),
               steps([('def 開頭、冒號結尾', 'def = define（定義）'), ('名稱照變數命名規則', '不可用保留字'),
                      ('( ) 放參數', '可以 0 個或多個，用逗號隔開'), ('先定義、後呼叫', '定義要寫在呼叫之前')], 'blue'), '1fr 1fr')},

    {'id': 5, 'title': '無回傳與有回傳', 'chapter': '第一節：內建函式與自訂函式', 'bg': 'white',
     'html': title('📤 沒有回傳值 vs 有回傳值')
     + two_col(py('def sayhello():\n    print("Hello Python!")\n\nsayhello()\nsayhello()', '只「做事」：沒有 return', 'Hello Python!\nHello Python!'),
               py('def add(a, b):\n    return a + b\n\ns = add(6, 10)\nprint(s)\nprint(add(1, 2) * 3)', '「算出結果交回來」：有 return', '16\n9'), '1fr 1fr')
     + note('🔑 有 return 的函式可以放在運算式裡繼續用，例如 ' + ic('add(1, 2) * 3') + '。沒有 return 的函式回傳的是 ' + ic('None') + '。')},

    {'id': 6, 'title': '第一節 隨堂測驗', 'chapter': '第一節：內建函式與自訂函式', 'bg': 'purple', 'quiz': 'q1',
     'html': quiz_cover('第一節 隨堂測驗', '函式基本觀念 ｜ 4 題')},

    # ── 第二節 ──
    {'id': 7, 'title': '呼叫的過程', 'chapter': '第二節：參數、回傳值與範圍', 'bg': 'white',
     'html': title('🔄 呼叫函式時發生了什麼？')
     + steps([('執行 s = add(6, 10)', '先算等號右邊：呼叫 add'), ('傳入參數', '6 交給 a、10 交給 b（等同 a = 6, b = 10）'),
              ('執行函式主體', '計算 a + b = 16'), ('return 16', '函式結束，add(6, 10) 這個位置變成 16'),
              ('回到原處', '執行 s = 16')], 'purple')
     + note('📌 執行到 return 函式就<strong>立刻結束</strong>，return 後面的程式不會執行。')},

    {'id': 8, 'title': '範例：次方函式', 'chapter': '第二節：參數、回傳值與範圍', 'bg': 'white',
     'html': title('💪 範例：自己寫次方函式')
     + two_col(py('def power(a, b):\n    p = 1\n    for i in range(b):\n        p *= a\n    return p\n\nx, y = map(int, input().split())\nprint(power(x, y))', '',
                  '2 10\n1024'),
               py('def my_abs(n):\n    if n < 0:\n        return -n\n    return n\n\nprint(my_abs(-7), my_abs(3))', '絕對值：不同情況回傳不同值', '7 3'), '1fr 1fr')},

    {'id': 9, 'title': '範例：最大公因數', 'chapter': '第二節：參數、回傳值與範圍', 'bg': 'white',
     'html': title('🔢 範例：最大公因數與最小公倍數')
     + two_col(py('def gcd(a, b):\n    while b != 0:\n        a, b = b, a % b\n    return a\n\na, b = 12, 18\ng = gcd(a, b)\nprint("最大公因數", g)\nprint("最小公倍數", a * b // g)', '輾轉相除法', '最大公因數 6\n最小公倍數 36'),
               table(['a', 'b', 'a % b'], [['12', '18', '12'], ['18', '12', '6'], ['12', '6', '0'], ['<strong>6</strong>', '0', '停']], ['33%', '33%', '34%']), '1.5fr 1fr')
     + note('📐 兩數乘積 = 最大公因數 × 最小公倍數。輾轉相除法（歐幾里得演算法）是有記載以來最古老的演算法之一。')},

    {'id': 10, 'title': '變數範圍', 'chapter': '第二節：參數、回傳值與範圍', 'bg': 'white',
     'html': title('🏠 區域變數 vs 全域變數')
     + two_col(py('def area(r):\n    pi = 3.14          # 區域變數：只在函式裡有效\n    return pi * r * r\n\nprint(area(2))\nprint(pi)', '', '12.56\nNameError: name \'pi\' is not defined'),
               card('teal', '函式是一個房間', '在函式裡建立的變數（含參數），<strong>函式結束就消失</strong>，外面看不到。<br><br>'
                    '要把結果帶出來，就用 <strong>return</strong>。', '🚪'), '1.4fr 1fr')
     + note('✅ 好習慣：函式需要的資料用<strong>參數</strong>傳進去，結果用 <strong>return</strong> 傳出來，不要依賴外面的變數。')},

    {'id': 11, 'title': '第二節 隨堂測驗', 'chapter': '第二節：參數、回傳值與範圍', 'bg': 'purple', 'quiz': 'q2',
     'html': quiz_cover('第二節 隨堂測驗', '參數、回傳值與範圍 ｜ 4 題')},

    # ── 第三節 ──
    {'id': 12, 'title': '什麼是遞迴', 'chapter': '第三節：遞迴', 'bg': 'white',
     'html': title('🪞 遞迴：函式呼叫自己')
     + lead('如果一個問題可以<strong>拆成和自己長得一樣、但規模比較小的問題</strong>，就可以用遞迴解決。')
     + grid(3,
            card('blue', '俄羅斯娃娃', '打開一個，裡面是更小的同款娃娃，直到最小那個', '🪆', True),
            card('green', '排隊問人數', '問前面的人「你前面有幾人」，再 +1', '🧍', True),
            card('yellow', '兩面鏡子', '鏡中有鏡，一層一層變小', '🪞', True))},

    {'id': 13, 'title': '遞迴兩要素', 'chapter': '第三節：遞迴', 'bg': 'white',
     'html': title('🧱 寫遞迴的兩個要素')
     + two_col(card('blue', '① 遞迴關係式', '大問題怎麼用小問題表示？<br><br>f(n) = 1 + 2 + … + n<br>f(n−1) = 1 + 2 + … + (n−1)<br>所以 <strong>f(n) = f(n−1) + n</strong>', '🔗'),
               card('red', '② 終止條件', '最小的問題答案是什麼？<br><br><strong>f(1) = 1</strong><br><br>沒有終止條件會一直呼叫下去，'
                    'Python 會出現 <strong>RecursionError</strong>。', '🛑'), '1fr 1fr')
     + py('def f(n):\n    if n == 1:          # 終止條件\n        return 1\n    return f(n - 1) + n # 遞迴關係式\n\nprint(f(100))', '', '5050')},

    {'id': 14, 'title': '遞迴展開過程', 'chapter': '第三節：遞迴', 'bg': 'white',
     'html': title('🔍 f(4) 是怎麼算出來的？')
     + two_col(table(['往下呼叫', '往上回傳'],
                     [['f(4) = f(3) + 4', '= 6 + 4 = <strong>10</strong>'], ['f(3) = f(2) + 3', '= 3 + 3 = 6'],
                      ['f(2) = f(1) + 2', '= 1 + 2 = 3'], ['f(1) = 1（終止）', '回傳 1']], ['55%', '45%']),
               card('purple', '先下去、再回來', '呼叫會一層一層「疊」起來，直到碰到終止條件，'
                    '再一層一層把答案「傳」回去。<br><br>這個疊起來的結構叫做<strong>堆疊（stack）</strong>。', '📚'), '1.2fr 1fr')
     + note('🧾 對應線上練習 <strong>#508 遞迴結構</strong>、<strong>#509 1 + 2 + … n 的遞迴</strong>、<strong>#510</strong>。')},

    {'id': 15, 'title': '階乘', 'chapter': '第三節：遞迴', 'bg': 'white',
     'html': title('❗ 範例：n 階乘')
     + two_col(py('def fact(n):\n    if n <= 1:\n        return 1\n    return n * fact(n - 1)\n\nprint(fact(5))\nprint(fact(10))', '', '120\n3628800'),
               card('green', '關係式與終止條件', 'n! = 1 × 2 × … × n<br><strong>n! = n × (n−1)!</strong><br><strong>0! = 1! = 1</strong><br><br>'
                    '和第 4 章的累乘迴圈結果一樣，只是換個想法。', '🧮'))
     + note('🧾 對應線上練習 <strong>#513 使用遞迴計算 1 × 2 × 3 × … × n</strong>。')},

    {'id': 16, 'title': '費氏數列', 'chapter': '第三節：遞迴', 'bg': 'white',
     'html': title('🐇 範例：費氏數列')
     + lead('1, 1, 2, 3, 5, 8, 13, 21…　由義大利數學家費波那契於 1202 年在《計算之書》中以兔子繁殖問題提出：<strong>每一項是前兩項的和</strong>。')
     + two_col(py('def fib(n):\n    if n <= 2:\n        return 1\n    return fib(n - 1) + fib(n - 2)\n\nfor i in range(1, 11):\n    print(fib(i), end=" ")', '', '1 1 2 3 5 8 13 21 34 55 '),
               card('yellow', '終止條件有兩個', 'f(1) = f(2) = 1<br>f(n) = f(n−1) + f(n−2)<br><br>大自然中的向日葵種子、松果鱗片排列常出現費氏數列。', '🌻'), '1.3fr 1fr')
     + note('🧾 對應線上練習 <strong>#511 使用遞迴計算費氏數列第 n 項的值</strong>。')},

    {'id': 17, 'title': '遞迴的代價', 'chapter': '第三節：遞迴', 'bg': 'white',
     'html': title('🐢 遞迴不一定比較快')
     + two_col(card('red', 'fib(35) 為什麼那麼慢？', 'fib(5) 要算 fib(4) 和 fib(3)；fib(4) 又要算 fib(3)…<br>'
                    '同一個值被<strong>重複算了很多次</strong>，呼叫次數像樹枝一樣爆炸增加。', '🌳'),
               card('green', '改進方法', '① 改用迴圈從前往後算<br>② 把算過的答案存起來（記憶化，memoization）<br><br>'
                    '遞迴適合讓程式「好想、好寫」，但要注意效率。', '⚡'), '1fr 1fr')
     + note('🎓 延伸：二分搜尋也能寫成遞迴（#512）：在左半或右半「用同樣方法再找一次」，終止條件是 left > right 或找到。')},

    {'id': 18, 'title': '第三節 隨堂測驗', 'chapter': '第三節：遞迴', 'bg': 'purple', 'quiz': 'q3',
     'html': quiz_cover('第三節 隨堂測驗', '遞迴 ｜ 4 題')},

    # ── 實作與總結 ──
    {'id': 19, 'title': '本週實作', 'chapter': '實作與總結', 'bg': 'white',
     'html': title('✏️ 本週實作：Colab ＋ 線上練習')
     + colab('py08_function.ipynb', '第 8 課 Colab 練習（7 題）', '次方函式、圓面積函式、最大公因數、遞迴 1 加到 n、n!、費氏數列、遞迴二分搜尋（挑戰）')
     + oj([('#329', '函式（測驗）'), ('#508、#509', '遞迴結構觀念（測驗）'), ('#510', '使用遞迴計算 1 加到 n（VPL）'),
           ('#511', '費氏數列第 n 項（VPL）'), ('#512', '二分搜尋使用遞迴（VPL）'), ('#513', '遞迴計算 n!（VPL）')])},

    {'id': 20, 'title': '本週總結', 'chapter': '實作與總結', 'bg': 'navy',
     'html': recap('本週重點',
                   [('def', '定義函式：名稱、參數、主體、return'),
                    ('return', '把結果交回呼叫的地方，函式立刻結束'),
                    ('區域變數', '函式裡的變數離開函式就消失'),
                    ('遞迴', '關係式 + 終止條件，缺一不可')],
                   '「把大問題拆成小問題，是程式設計最重要的能力。」',
                   '下一章：Pandas 與機器學習——用 Python 分析真實的開放資料')},
]

QUIZZES = {
    'q1': {'title': '第一節 隨堂測驗', 'questions': [
        {'q': 'Python 定義函式要用哪個保留字？',
         'options': ['function', 'def', 'func', 'define'],
         'answer': 1,
         'explain': 'Python 用 def（define 的縮寫）定義函式，最後要加冒號。'},
        {'q': '下列何者「不是」自訂函式的好處？',
         'options': ['同樣的程式可以重複使用', '要修改時只改一個地方', '程式一定跑得比較快', '方便分工合作'],
         'answer': 2,
         'explain': '函式讓程式好讀、好維護、好重複使用，但不保證執行速度變快。'},
        {'q': '以下程式輸出？\ndef add(a, b):\n    return a + b\nprint(add(2, 3) * 2)',
         'options': ['5', '10', '2323', '錯誤'],
         'answer': 1,
         'explain': 'add(2, 3) 回傳 5，再乘以 2 得到 10。'},
        {'q': '一個函式沒有寫 return，呼叫後得到的值是？',
         'options': ['0', '空字串', 'None', '錯誤'],
         'answer': 2,
         'explain': '沒有 return 的函式執行完會回傳 None，代表「沒有值」。'},
    ]},
    'q2': {'title': '第二節 隨堂測驗', 'questions': [
        {'q': '以下程式輸出？\ndef f(x):\n    return x * 2\n    print("Hi")\nprint(f(4))',
         'options': ['8', 'Hi 和 8', '8 和 Hi', 'Hi'],
         'answer': 0,
         'explain': '執行到 return 函式就結束，後面的 print("Hi") 永遠不會執行。'},
        {'q': '輾轉相除法 gcd(12, 18) 的結果是？',
         'options': ['2', '3', '6', '36'],
         'answer': 2,
         'explain': '12 和 18 的最大公因數是 6；最小公倍數是 12 × 18 ÷ 6 = 36。'},
        {'q': '在函式裡建立的變數，在函式外面使用會怎樣？',
         'options': ['可以正常使用', '出現 NameError', '自動變成 0', '自動變成全域變數'],
         'answer': 1,
         'explain': '函式內的變數是區域變數，函式結束就消失。要把結果帶出來請用 return。'},
        {'q': '呼叫 power(2, 5) 時，參數 a 和 b 分別是？',
         'options': ['a = 5, b = 2', 'a = 2, b = 5', 'a = 7, b = 0', '都是 2'],
         'answer': 1,
         'explain': '參數依照位置對應：第一個值 2 給 a，第二個值 5 給 b。'},
    ]},
    'q3': {'title': '第三節 隨堂測驗', 'questions': [
        {'q': '撰寫遞迴函式一定要有哪兩個要素？',
         'options': ['迴圈和串列', '遞迴關係式和終止條件', 'input 和 print', '全域變數和 break'],
         'answer': 1,
         'explain': '關係式描述「大問題如何變成小問題」，終止條件讓遞迴能停下來，兩者缺一不可。'},
        {'q': 'def f(n):\n    if n == 1: return 1\n    return f(n-1) + n\nf(4) 的值是？',
         'options': ['4', '10', '24', '無限遞迴'],
         'answer': 1,
         'explain': 'f(4) = f(3) + 4 = (f(2) + 3) + 4 = ((1 + 2) + 3) + 4 = 10。'},
        {'q': '費氏數列 1, 1, 2, 3, 5, 8, … 的第 9 項是？',
         'options': ['21', '34', '55', '13'],
         'answer': 1,
         'explain': '接著寫：13（第 7 項）、21（第 8 項）、34（第 9 項）。每一項都是前兩項的和。'},
        {'q': '遞迴函式忘了寫終止條件，執行時會？',
         'options': ['回傳 0', '自動停止', '一直呼叫自己，最後出現 RecursionError', '變成迴圈'],
         'answer': 2,
         'explain': '沒有終止條件就會無限呼叫，Python 有呼叫深度上限，超過就出現 RecursionError。'},
    ]},
}

QUIZZES = safe_quizzes(QUIZZES)
