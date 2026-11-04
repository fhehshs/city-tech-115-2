# -*- coding: utf-8 -*-
# 第 1 週（課程計畫 W15）：程式設計概念、Colab 與輸出入（Colab：py01_hello_colab）
from content._kit import *

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一節：程式與程式語言', 'start': 2},
    {'name': '第二節：Colab 開發環境', 'start': 7},
    {'name': '第三節：print 與 input', 'start': 12},
    {'name': '實作與總結', 'start': 18},
]

SLIDES = [
    {'id': 1, 'title': 'Hello Python!', 'chapter': '封面', 'bg': 'navy',
     'html': cover('🐍', 'Hello Python!', 'Programming Concepts · Google Colab · Input &amp; Output',
                   ['💡 什麼是程式', '📓 Google Colab', '🖨️ print()', '⌨️ input()'], '第 1 週')},

    # ── 第一節 ──
    {'id': 2, 'title': '這學期要做什麼', 'chapter': '第一節：程式與程式語言', 'bg': 'white',
     'html': title('🗺️ 這學期的地圖：從 Hello 到資料專題')
     + table(['階段', '週次', '章', '學什麼', '做出什麼'],
             [['🌱 語法與語意', '1–5', '1–5', '輸出入、變數、運算子、選擇、迴圈', '計算機、BMI、九九乘法表'],
              ['🧱 陣列資料結構', '6–8', '6', '串列、二維串列', '成績單'],
              ['🔎 演算法', '9–11', '7–8', '排序、搜尋、函式、遞迴', '商品搜尋、自己的工具函式'],
              ['🤖 資料與 AI', '12', '9', 'Pandas、機器學習入門', '開放資料分析、第一個 AI 模型'],
              ['🎯 期末專題', '13–15', '10', 'API、Gradio 互動網頁', '與人互動的資料小工具']],
             ['18%', '9%', '8%', '35%', '30%'])
     + note('🎯 3 學期制的第 2 學期，共 15 週、每週 2 節。期末要做出一個<strong>能和人互動、用真實資料</strong>的小工具，例如「輸入測站，回報空氣品質」。')},

    {'id': 3, 'title': '什麼是程式設計', 'chapter': '第一節：程式與程式語言', 'bg': 'white',
     'html': title('💡 程式設計 Programming 是什麼？')
     + lead('程式（Program）是一組<strong>讓電腦一步一步執行的指令</strong>。程式設計就是把「解決問題的方法」寫成電腦看得懂的指令。')
     + grid(3,
            card('blue', '① 分析問題', '輸入是什麼？要輸出什麼？', '🔍', True),
            card('green', '② 設計演算法', '用步驟、流程圖把方法想清楚', '🧭', True),
            card('yellow', '③ 寫程式＆測試', '用程式語言實作，再除錯', '🛠️', True))
     + note('🍳 比喻：演算法是<strong>食譜</strong>，程式是用某種語言（中文、英文…）寫下的食譜，電腦是照著做的<strong>廚師</strong>。')},

    {'id': 4, 'title': '程式語言的演進', 'chapter': '第一節：程式與程式語言', 'bg': 'white',
     'html': title('🕰️ 程式語言的演進')
     + table(['世代', '例子', '特色'],
             [['機器語言', '10110000 01100001', '只有 0 與 1，電腦直接執行，人很難讀'],
              ['組合語言', 'MOV AL, 61h', '用英文縮寫代替 0/1，仍和硬體綁在一起'],
              ['高階語言', 'C、Java、<strong>Python</strong>', '接近人類語言，需要編譯器或直譯器翻譯'],
              ['AI 協作時代', '自然語言提示＋程式', 'AI 幫忙寫、解釋程式，但人仍要<strong>看得懂、驗得了</strong>']],
             ['20%', '30%', '50%'])
     + note('🧠 AI 會寫程式，不代表不用學：看不懂程式的人，就沒辦法判斷 AI 給的答案對不對。', 'yellow', '')},

    {'id': 5, 'title': '為什麼學 Python', 'chapter': '第一節：程式與程式語言', 'bg': 'white',
     'html': title('🐍 為什麼選 Python？')
     + grid(2,
            card('green', '語法簡潔', '用縮排表示區塊，讀起來接近英文。<br>' + ic('print("Hello")') + ' 一行就能輸出', '✨'),
            card('blue', '套件豐富', '資料分析（Pandas）、AI（scikit-learn、PyTorch）、網頁、物聯網都能用', '📦'),
            card('purple', '應用廣泛', '資料科學、機器學習、自動化、教學；也是 APCS 可選用的語言之一', '🌏'),
            card('orange', '免安裝就能寫', '用瀏覽器開 Google Colab 就能寫，程式在雲端執行', '☁️'))
     + note('🇹🇼 在地應用：政府開放資料平臺上的 YouBike、空氣品質、公車動態，都能用 Python 抓下來分析——第 9、10 章就會做。')},

    {'id': 6, 'title': '第一節 隨堂測驗', 'chapter': '第一節：程式與程式語言', 'bg': 'purple', 'quiz': 'q1',
     'html': quiz_cover('第一節 隨堂測驗', '程式與程式語言 ｜ 4 題')},

    # ── 第二節 ──
    {'id': 7, 'title': '認識 Google Colab', 'chapter': '第二節：Colab 開發環境', 'bg': 'white',
     'html': title('📓 Google Colab：雲端的 Python 筆記本')
     + lead('Colab（Colaboratory）是 Google 提供的免費線上 Jupyter 筆記本，<strong>不用安裝</strong>，用學校 Google 帳號登入就能寫 Python。')
     + grid(3,
            card('blue', '雲端執行', '程式在 Google 的主機上跑，學校電腦、家裡電腦、平板都能用', '☁️', True),
            card('green', '自動存雲端硬碟', '筆記本存在你的 Google 雲端硬碟「Colab Notebooks」資料夾', '💾', True),
            card('yellow', '可分享', '像 Google 文件一樣，用連結分享給老師或組員', '🔗', True))
     + note('⏱️ 一段時間沒操作，Colab 會中斷連線，變數會清空；重新連線後要從上面的儲存格<strong>再執行一次</strong>。', 'yellow', '')},

    {'id': 8, 'title': '兩種儲存格', 'chapter': '第二節：Colab 開發環境', 'bg': 'white',
     'html': title('🧱 兩種儲存格：程式碼與文字')
     + two_col(card('blue', '💻 程式碼儲存格', '寫 Python 程式<br>▶ 按左邊播放鍵，或 <strong>Shift + Enter</strong> 執行<br>結果會顯示在下方', ''),
               card('green', '📝 文字儲存格', '寫說明、筆記、題目<br>支援 Markdown：' + ic('# 標題') + '、' + ic('**粗體**')
                    + '<br>也能寫數學式：' + ic('$x^2$'), ''), '1fr 1fr')
     + table(['快捷鍵', '功能'],
             [['Shift + Enter', '執行目前儲存格並跳到下一格'],
              ['Ctrl + Enter', '執行但停在原儲存格'],
              ['Ctrl + /', '把選取的程式行加上／取消 # 註解'],
              ['Ctrl + M  B', '在下方新增程式碼儲存格']], ['35%', '65%'])},

    {'id': 9, 'title': '建議設定', 'chapter': '第二節：Colab 開發環境', 'bg': 'white',
     'html': title('⚙️ 上課前先做的兩個設定')
     + steps([('關掉自動完成', '工具 → 設定 → 編輯器 → <strong>取消</strong>勾選「自動觸發程式碼完成功能」。初學時自己打字，語法才記得住。'),
              ('儲存副本', '開啟老師的練習檔後，先按 <strong>檔案 → 在雲端硬碟中儲存副本</strong>，再在副本上作答。否則關掉頁面就不見了。'),
              ('改檔名', '副本檔名改成「座號_姓名_py01」，繳交時老師才找得到。')], 'blue')
     + note('🤖 Colab 內建 AI 助手（Gemini）。這學期的練習請<strong>先自己寫</strong>，卡住超過 10 分鐘再問 AI，而且要能解釋 AI 給的每一行。', 'red', '')},

    {'id': 10, 'title': '打開第 1 課練習', 'chapter': '第二節：Colab 開發環境', 'bg': 'white',
     'html': title('📓 打開第 1 課 Colab 練習')
     + colab('py01_hello_colab.ipynb', '第 1 課：認識 Colab 與輸出入',
             '包含 print()、input()、註解的示範，以及 3 題實作。記得先「在雲端硬碟中儲存副本」！')
     + grid(2,
            card('gray', '🧪 示範儲存格', '已經寫好程式，按 ▶ 執行，觀察結果，再試著改改看'),
            card('orange', '✏️ 練習儲存格', '開頭寫著「# ✏️ 練習」，只有提示，要自己完成'))
     + note('💬 遇到紅字錯誤訊息不要怕！先看<strong>最後一行</strong>：它會告訴你錯誤種類（如 SyntaxError、NameError）和出錯的行號。')},

    {'id': 11, 'title': '第二節 隨堂測驗', 'chapter': '第二節：Colab 開發環境', 'bg': 'purple', 'quiz': 'q2',
     'html': quiz_cover('第二節 隨堂測驗', 'Colab 開發環境 ｜ 3 題')},

    # ── 第三節 ──
    {'id': 12, 'title': 'print() 基本用法', 'chapter': '第三節：print 與 input', 'bg': 'white',
     'html': title('🖨️ print()：讓電腦說話')
     + lead('語法：' + ic("print(資料1, 資料2, ..., sep=' ', end='\\n')") + '　多個資料用逗號隔開；預設以<strong>空格</strong>分隔、輸出完<strong>換行</strong>。')
     + two_col(py('print("Hello", "Python")\nprint(1 + 2)\nprint("1+2=", 1 + 2)', '字串要加引號，數字和運算式不用',
                  'Hello Python\n3\n1+2= 3'),
               card('blue', '引號很重要', ic('print("1+2")') + ' 輸出 <strong>1+2</strong>（字串原樣輸出）<br>'
                    + ic('print(1+2)') + ' 輸出 <strong>3</strong>（先計算）<br><br>單引號 \' 或雙引號 " 都可以，但前後要一致。', '💡'))},

    {'id': 13, 'title': '字串串接與重複', 'chapter': '第三節：print 與 input', 'bg': 'white',
     'html': title('➕ 字串可以「加」也可以「乘」')
     + two_col(py('print("Hello" + "Python!")\nprint("Go! " * 3)\nprint("2026", "11", "04", sep="/")\nprint("不換行", end="")\nprint("…接在後面")',
                  '', 'HelloPython!\nGo! Go! Go! \n2026/11/04\n不換行…接在後面'),
               table(['寫法', '效果'],
                     [['+', '把兩個字串接起來（中間沒空格）'],
                      ['*', '把字串重複 n 次'],
                      ['sep="/"', '資料之間改用 / 分隔'],
                      ['end=""', '輸出完不換行']], ['30%', '70%']))
     + note('⚠️ ' + ic('"年齡" + 16') + ' 會出錯（TypeError）：字串不能直接和數字相加。用逗號 ' + ic('print("年齡", 16)') + ' 就沒問題。', 'red', '')},

    {'id': 14, 'title': 'input() 取得輸入', 'chapter': '第三節：print 與 input', 'bg': 'white',
     'html': title('⌨️ input()：讓使用者輸入')
     + lead('語法：' + ic('變數 = input("提示字串")') + '　程式會停下來等使用者輸入，按 Enter 後把輸入的內容存進變數。')
     + py('name = input("請輸入您的名字：")\nprint("你好，", name)', '執行後在下方框框輸入名字，按 Enter',
          '請輸入您的名字：小安\n你好， 小安')
     + note('🔑 <strong>input() 拿到的一定是字串</strong>。輸入 16，得到的是 "16"。要計算的話，下週會學用 '
            + ic('int()') + '、' + ic('float()') + ' 轉成數字。', 'yellow', '')},

    {'id': 15, 'title': '註解與 f-string', 'chapter': '第三節：print 與 input', 'bg': 'white',
     'html': title('📝 註解 # 與 f-string')
     + two_col(card('gray', '# 註解', '從 # 到行尾都不會被執行，用來<strong>說明程式</strong>。<br>好的註解寫「為什麼這樣做」，'
                    '不是重複程式在做什麼。<br>多行一起加註解：選取後按 Ctrl + /', '💬'),
               py('city = "台北"\nyear = 2026\n# f-string：字串前加 f，變數放在 { } 裡\nprint(f"{year} 年我在{city}")', 'f-string（Python 3.6 起）',
                  '2026 年我在台北'), '1fr 1.2fr')
     + note('✨ f-string 是現在最常見的輸出寫法，之後還可以控制小數位數，例如 ' + ic('f"{3.14159:.2f}"') + ' → 3.14')},

    {'id': 16, 'title': '常見錯誤', 'chapter': '第三節：print 與 input', 'bg': 'white',
     'html': title('🐞 新手最常見的 4 種錯誤')
     + table(['錯誤寫法', '錯誤訊息', '原因'],
             [[ic('Print("Hi")'), 'NameError', 'Python 大小寫有別，要寫 print'],
              [ic('print("Hi)'), 'SyntaxError', '引號沒有成對'],
              [ic('print（"Hi"）'), 'SyntaxError', '用了<strong>全形</strong>括號，要切換成半形'],
              [ic('print(name)'), 'NameError', 'name 還沒有被指定值（或上面的儲存格沒執行）']],
             ['30%', '22%', '48%'])
     + note('🔍 除錯口訣：<strong>看最後一行 → 找行號 → 檢查拼字、引號、括號、全形半形</strong>。')},

    {'id': 17, 'title': '第三節 隨堂測驗', 'chapter': '第三節：print 與 input', 'bg': 'purple', 'quiz': 'q3',
     'html': quiz_cover('第三節 隨堂測驗', 'print 與 input ｜ 5 題')},

    # ── 實作與總結 ──
    {'id': 18, 'title': '本週實作', 'chapter': '實作與總結', 'bg': 'white',
     'html': title('✏️ 本週實作：Colab ＋ 線上練習')
     + colab('py01_hello_colab.ipynb', '第 1 課 Colab 練習（3 題）', '① 說出你的身高　② 自我介紹機　③ 用 f-string 改寫')
     + oj([('#301', '輸出指令（測驗）'), ('#302', '讓電腦說哈囉（VPL）'), ('#303', '輸入指令（測驗）'),
           ('#304', '讓電腦對您說 Hello（VPL）')])
     + rubric_box('3 題都正確，輸出格式整齊，並加上自己的註解',
                  '3 題都能執行，結果正確',
                  '完成 2 題，或有小錯誤',
                  '完成 1 題以下')},

    {'id': 19, 'title': '本週總結', 'chapter': '實作與總結', 'bg': 'navy',
     'html': recap('本週重點',
                   [('程式設計', '分析問題 → 設計演算法 → 寫程式與測試'),
                    ('Colab', '雲端 Python 筆記本；先「儲存副本」再作答'),
                    ('print()', '逗號隔開多個資料；sep 改分隔、end 改結尾'),
                    ('input()', '取得的一定是字串，要計算需轉型')],
                   '「程式不是寫給電腦看的，是寫給人看、順便讓電腦執行的。」',
                   '下一章：變數、資料型態與運算子——讓程式真的會「算」')},
]

QUIZZES = {
    'q1': {'title': '第一節 隨堂測驗', 'questions': [
        {'q': '下列哪一個是「程式設計」的正確步驟順序？',
         'options': ['寫程式 → 分析問題 → 設計演算法', '分析問題 → 設計演算法 → 寫程式並測試',
                     '設計演算法 → 測試 → 分析問題', '直接寫程式，錯了再說'],
         'answer': 1,
         'explain': '先弄清楚輸入和輸出（分析問題），再想清楚步驟（演算法），最後才用程式語言實作並測試。跳過前兩步，常常寫到一半才發現方向錯了。'},
        {'q': '電腦可以「直接」執行的是哪一種語言？',
         'options': ['Python', '組合語言', '機器語言', '中文'],
         'answer': 2,
         'explain': 'CPU 只認得 0 與 1 組成的機器語言。Python 等高階語言要經過直譯器或編譯器翻譯成機器語言才能執行。'},
        {'q': '下列關於 Python 的敘述，何者「錯誤」？',
         'options': ['用縮排表示程式區塊', '有很多資料分析與 AI 套件', '只能在安裝了 Python 的電腦上寫，瀏覽器不行', '語法接近英文，適合初學'],
         'answer': 2,
         'explain': '用 Google Colab，只要有瀏覽器和 Google 帳號就能寫 Python，程式在雲端主機上執行。'},
        {'q': '現在 AI 也會寫程式，為什麼還要學程式設計？最好的理由是？',
         'options': ['AI 寫的程式一定是錯的', '要能看懂並驗證 AI 給的程式是否正確', '因為考試要考', '學程式就不用學數學'],
         'answer': 1,
         'explain': 'AI 給的程式可能對、也可能有錯或不符合需求。看得懂程式，才能判斷、修改並負責自己交出去的成果。'},
    ]},
    'q2': {'title': '第二節 隨堂測驗', 'questions': [
        {'q': '在 Colab 中，執行目前的程式碼儲存格並跳到下一格，快捷鍵是？',
         'options': ['Ctrl + S', 'Shift + Enter', 'Alt + F4', 'Ctrl + Z'],
         'answer': 1,
         'explain': 'Shift + Enter 會執行目前儲存格並移到下一格；Ctrl + Enter 則是執行後停在原處。'},
        {'q': '打開老師分享的 Colab 練習檔後，第一件事應該做什麼？',
         'options': ['直接在老師的檔案上作答', '檔案 → 在雲端硬碟中儲存副本', '把所有儲存格刪掉', '關掉重開'],
         'answer': 1,
         'explain': '老師分享的檔案你沒有編輯權，直接寫不會被儲存。先儲存副本到自己的雲端硬碟，作答才會保留下來。'},
        {'q': 'Colab 閒置一段時間後重新連線，執行 print(name) 出現 NameError，最可能的原因是？',
         'options': ['print 拼錯', '重新連線後變數被清空，要重新執行上面指定 name 的儲存格', 'Colab 壞了', '網路太慢'],
         'answer': 1,
         'explain': '中斷連線後執行環境會重置，之前存在記憶體裡的變數都不見了。從上往下重新執行一次就好。'},
    ]},
    'q3': {'title': '第三節 隨堂測驗', 'questions': [
        {'q': 'print("1+2=", 1+2) 的輸出是？',
         'options': ['1+2= 1+2', '1+2= 3', '3= 3', '1+2=3'],
         'answer': 1,
         'explain': '引號內的 "1+2=" 原樣輸出；沒有引號的 1+2 會先計算成 3。兩個資料之間預設用一個空格隔開。'},
        {'q': 'print("A", "B", "C", sep="-") 的輸出是？',
         'options': ['A B C', 'A-B-C', 'ABC', '-A-B-C-'],
         'answer': 1,
         'explain': 'sep 指定資料之間的分隔符號，預設是空格，這裡改成 "-"，所以輸出 A-B-C。'},
        {'q': 'print("Hi" * 3) 的輸出是？',
         'options': ['Hi3', 'HiHiHi', 'Hi Hi Hi', '錯誤'],
         'answer': 1,
         'explain': '字串乘以整數 n 代表重複 n 次，中間不會自動加空格。'},
        {'q': 'x = input("輸入：")，使用者輸入 16，x 的資料型態是？',
         'options': ['整數 int', '浮點數 float', '字串 str', '布林 bool'],
         'answer': 2,
         'explain': 'input() 回傳的一定是字串。要當成數字計算，必須用 int(x) 或 float(x) 轉換。'},
        {'q': '執行 print（"Hello"） 出現 SyntaxError，最可能的原因是？',
         'options': ['Hello 拼錯', '括號是全形的', '沒有寫分號', '要先 import print'],
         'answer': 1,
         'explain': 'Python 的符號都要用半形。全形括號（）、全形引號「」或＂是新手最常見的錯誤之一。'},
    ]},
}

QUIZZES = safe_quizzes(QUIZZES)
