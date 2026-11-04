# -*- coding: utf-8 -*-
# 第 6–8 週：串列與二維串列（Colab：py06_list）
from content._kit import *

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一節：認識串列與索引', 'start': 2},
    {'name': '第二節：串列操作', 'start': 7},
    {'name': '第三節：最大、最小、總和', 'start': 12},
    {'name': '第四節：二維串列', 'start': 16},
    {'name': '實作與總結', 'start': 21},
]

SLIDES = [
    {'id': 1, 'title': '串列與二維串列', 'chapter': '封面', 'bg': 'navy',
     'html': cover('📚', '串列 List', 'Lists · Index · 2D Lists',
                   ['🗄️ 串列', '🔢 索引從 0 開始', '🏆 最大與最小', '📊 二維成績單'], '第 6–8 週')},

    # ── 第一節 ──
    {'id': 2, 'title': '為什麼需要串列', 'chapter': '第一節：認識串列與索引', 'bg': 'white',
     'html': title('🤯 1000 位學生的成績，要開 1000 個變數？')
     + two_col(py('a1 = 81\na2 = 82\na3 = 83\n# ……a1000 = ??', '用變數：不可能', ''),
               py('score = [81, 82, 83, 84, 85]\nprint(score)\nprint(len(score))', '用串列：一個名字裝全部', '[81, 82, 83, 84, 85]\n5'), '1fr 1fr')
     + note('🗄️ 串列（list）是 Python 最重要的<strong>資料結構</strong>：用中括號 [ ] 把資料包起來，元素之間用逗號隔開，型態可以不同。')},

    {'id': 3, 'title': '索引', 'chapter': '第一節：認識串列與索引', 'bg': 'white',
     'html': title('🔢 索引（index）：從 0 開始編號')
     + lead('串列像一排置物櫃，每一格都有編號。<strong>第 1 格的編號是 0</strong>，第 i 個元素是 ' + ic('a[i-1]') + '。')
     + table(['元素', '81', '82', '83', '84', '85'],
             [['正向索引', 'a[0]', 'a[1]', 'a[2]', 'a[3]', 'a[4]'],
              ['反向索引', 'a[-5]', 'a[-4]', 'a[-3]', 'a[-2]', 'a[-1]']])
     + note('⚠️ ' + ic('a[5]') + ' 超出範圍，會出現 <strong>IndexError: list index out of range</strong>。這是使用串列最常見的錯誤。', 'red', '')},

    {'id': 4, 'title': '小試身手', 'chapter': '第一節：認識串列與索引', 'bg': 'white',
     'html': title('🧪 小試身手：先猜再看')
     + py('b = [1, 2, 3, 4, 5, 6]\nprint(b[0], b[5], b[-1], b[-6])\nprint(b[6])', '', '1 6 6 1\nIndexError: list index out of range')
     + note('🧠 串列長度是 n，正向索引是 <strong>0 ～ n−1</strong>，反向索引是 <strong>−1 ～ −n</strong>。')},

    {'id': 5, 'title': '在地例子', 'chapter': '第一節：認識串列與索引', 'bg': 'white',
     'html': title('🚇 生活中的「串列」')
     + grid(3,
            card('blue', '捷運文湖線', '["動物園", "木柵", "萬芳社區", "萬芳醫院", "辛亥", …]<br>站的順序就是索引', '🚇'),
            card('green', '一週 AQI', '[52, 61, 48, 95, 110, 73, 66]<br>索引 0 是星期一', '🌫️'),
            card('yellow', '購物車', '["筆記本", "原子筆", "便當"]<br>可以加入、刪除、修改', '🛒'))
     + note('📌 只要是「<strong>一串同類的資料，而且有順序</strong>」，就適合用串列。')},

    {'id': 6, 'title': '第一節 隨堂測驗', 'chapter': '第一節：認識串列與索引', 'bg': 'purple', 'quiz': 'q1',
     'html': quiz_cover('第一節 隨堂測驗', '串列與索引 ｜ 4 題')},

    # ── 第二節 ──
    {'id': 7, 'title': '走訪串列', 'chapter': '第二節：串列操作', 'bg': 'white',
     'html': title('🚶 走訪串列：兩種 for 寫法')
     + two_col(py('n = [10, 20, 30, 40]\nfor x in n:\n    print(x, end=" ")', '直接取元素（只需要值時）', '10 20 30 40 '),
               py('n = [10, 20, 30, 40]\nfor i in range(len(n)):\n    print(i, n[i])', '用索引取（需要位置時）', '0 10\n1 20\n2 30\n3 40'), '1fr 1fr')
     + note('💡 要「改」元素、或要知道「第幾個」時，用索引寫法。')},

    {'id': 8, 'title': '成員、串接、重複', 'chapter': '第二節：串列操作', 'bg': 'white',
     'html': title('🔍 in、+、* ')
     + py('fruits = ["蘋果", "橘子", "香蕉"]\nprint("蘋果" in fruits)\nprint("西瓜" not in fruits)\nprint(fruits + ["芒果"])\nprint([0] * 4)', '',
          "True\nTrue\n['蘋果', '橘子', '香蕉', '芒果']\n[0, 0, 0, 0]")
     + note('🧰 ' + ic('[0] * 4') + ' 很常用來建立「一開始全部是 0」的計數串列，例如統計每個等第有幾人。')},

    {'id': 9, 'title': '切片', 'chapter': '第二節：串列操作', 'bg': 'white',
     'html': title('✂️ 切片 slice：a[開始:結束]')
     + two_col(py('a = [81, 82, 83, 84, 85]\nprint(a[1:3])\nprint(a[:4])\nprint(a[3:])\nprint(a[::-1])', '', '[82, 83]\n[81, 82, 83, 84]\n[84, 85]\n[85, 84, 83, 82, 81]'),
               card('purple', '和 range 一樣', '「結束」不包含。<br>' + ic('a[1:3]') + ' 是索引 1、2<br>' + ic('a[:4]') + ' 從頭到索引 3<br>'
                    + ic('a[3:]') + ' 索引 3 到最後<br>' + ic('a[::-1]') + ' 反轉', '📐'))},

    {'id': 10, 'title': '修改與新增刪除', 'chapter': '第二節：串列操作', 'bg': 'white',
     'html': title('🛠️ 修改、新增、刪除')
     + two_col(py('cart = ["筆記本", "原子筆"]\ncart.append("便當")     # 加在最後\ncart[0] = "活頁紙"       # 修改\ncart.remove("原子筆")    # 刪除指定元素\nprint(cart, len(cart))', '',
                  "['活頁紙', '便當'] 2"),
               table(['寫法', '作用'], [['a.append(x)', '在最後加入 x'], ['a.insert(i, x)', '在索引 i 插入 x'], ['a.remove(x)', '刪除第一個 x'],
                                     ['a.pop()', '取出並刪除最後一個'], ['a.sort()', '由小到大排序'], ['a.index(x)', '找 x 的索引']], ['45%', '55%']), '1.2fr 1fr')},

    {'id': 11, 'title': '第二節 隨堂測驗', 'chapter': '第二節：串列操作', 'bg': 'purple', 'quiz': 'q2',
     'html': quiz_cover('第二節 隨堂測驗', '串列操作 ｜ 4 題')},

    # ── 第三節 ──
    {'id': 12, 'title': '找最高分', 'chapter': '第三節：最大、最小、總和', 'bg': 'white',
     'html': title('🏆 找最高分：打擂台法再登場')
     + two_col(py('score = [88, 51, 84, 58, 91, 86, 75, 92, 66, 82]\nmx = score[0]\nfor s in score:\n    if s > mx:\n        mx = s\nprint("最高分", mx)', '', '最高分 92'),
               steps([('先假設第一個最大', 'mx = score[0]'), ('一個一個比', '比 mx 大就換掉'), ('走完就是答案', '時間跟資料量成正比')], 'yellow'), '1.3fr 1fr')
     + note('⚠️ 別寫 ' + ic('mx = 0') + '：如果成績全是負數（例如溫度），答案就錯了。從第一個元素開始最保險。', 'yellow', '')},

    {'id': 13, 'title': '最低分與位置', 'chapter': '第三節：最大、最小、總和', 'bg': 'white',
     'html': title('📉 最低分，順便記住是第幾號')
     + py('score = [88, 51, 84, 58, 91, 86, 75, 92, 66, 82]\nmn, pos = score[0], 0\nfor i in range(len(score)):\n    if score[i] < mn:\n        mn, pos = score[i], i\nprint("最低分", mn, "是", pos + 1, "號")', '要知道位置 → 用索引寫法',
          '最低分 51 是 2 號')
     + note('🧾 對應線上練習 <strong>#403 計算最高銷售量</strong>、<strong>#404 計算最高與最低銷售量</strong>。')},

    {'id': 14, 'title': '總和與平均', 'chapter': '第三節：最大、最小、總和', 'bg': 'white',
     'html': title('➕ 總和與平均')
     + two_col(py('score = [88, 51, 84, 58, 91, 86, 75, 92, 66, 82]\ntotal = 0\nfor s in score:\n    total += s\nprint("總分", total)\nprint("平均", total / len(score))', '自己寫迴圈', '總分 773\n平均 77.3'),
               py('print(max(score), min(score))\nprint(sum(score), sum(score) / len(score))\nprint(sorted(score))', '內建函式驗算',
                  '92 51\n773 77.3\n[51, 58, 66, 75, 82, 84, 86, 88, 91, 92]'), '1fr 1fr')
     + note('🎯 平常用內建函式很方便；但<strong>考試和線上練習常常要求自己寫</strong>，而且懂原理才能處理變化題（例如「第二高分」）。')},

    {'id': 15, 'title': '第三節 隨堂測驗', 'chapter': '第三節：最大、最小、總和', 'bg': 'purple', 'quiz': 'q3',
     'html': quiz_cover('第三節 隨堂測驗', '最大、最小、總和 ｜ 3 題')},

    # ── 第四節 ──
    {'id': 16, 'title': '二維串列', 'chapter': '第四節：二維串列', 'bg': 'white',
     'html': title('📊 二維串列：串列裡放串列')
     + lead('5 位同學、3 科成績 → 5 列 × 3 行的表格。<strong>先列後行</strong>：' + ic('c[i][j]') + ' 是第 i 列、第 j 行（都從 0 開始）。')
     + two_col(py('c = [[85, 90, 78],\n     [72, 65, 80],\n     [95, 88, 92],\n     [60, 75, 70],\n     [88, 94, 85]]\nprint(c[2])\nprint(c[2][1])\nprint(len(c), len(c[0]))', '', '[95, 88, 92]\n88\n5 3'),
               table(['', '國文 j=0', '英文 j=1', '數學 j=2'],
                     [['i=0', '85', '90', '78'], ['i=1', '72', '65', '80'], ['i=2', '95', '<strong>88</strong>', '92'], ['i=3', '60', '75', '70'], ['i=4', '88', '94', '85']]), '1fr 1.2fr')},

    {'id': 17, 'title': '走訪二維串列', 'chapter': '第四節：二維串列', 'bg': 'white',
     'html': title('🔁🔁 用雙重迴圈走訪二維串列')
     + py('for i in range(len(c)):          # 外圈：每一列（每位同學）\n    for j in range(len(c[i])):   # 內圈：每一行（每一科）\n        print(c[i][j], end=" ")\n    print()', '',
          '85 90 78\n72 65 80\n95 88 92\n60 75 70\n88 94 85')
     + note('🔗 和上週的「雙重迴圈印星號」是同一個結構，只是把 * 換成 ' + ic('c[i][j]') + '。')},

    {'id': 18, 'title': '成績單', 'chapter': '第四節：二維串列', 'bg': 'white',
     'html': title('🧾 範例：成績單——每人總分與平均')
     + two_col(py('for i in range(len(c)):\n    t = 0                     # 每位同學重新歸零\n    for j in range(len(c[i])):\n        t += c[i][j]\n    print(f"{i+1}號 總分 {t} 平均 {t/len(c[i]):.1f}")', '',
                  '1號 總分 253 平均 84.3\n2號 總分 217 平均 72.3\n3號 總分 275 平均 91.7\n4號 總分 205 平均 68.3\n5號 總分 267 平均 89.0'),
               card('orange', '關鍵：t = 0 放哪裡？', '放在<strong>外圈裡、內圈前</strong>：每換一位同學就重新累加。<br><br>'
                    '放在最外面 → 總分會一直累積到下一個人。', '📍'), '1.5fr 1fr')
     + note('🧾 對應線上練習 <strong>#408 計算銷售總和</strong>。挑戰：改成計算「每一科」的平均（外圈換成 j）。')},

    {'id': 19, 'title': '二維串列的應用', 'chapter': '第四節：二維串列', 'bg': 'white',
     'html': title('🗺️ 二維串列在哪裡？')
     + grid(3,
            card('blue', '試算表', 'Google 試算表、Excel 的每一格就是 [列][欄]', '📊', True),
            card('green', '圖片', '數位影像是像素的二維陣列，每格存顏色值', '🖼️', True),
            card('yellow', '地圖與遊戲', '棋盤、踩地雷、迷宮都是二維格子', '♟️', True))
     + note('📌 第 9 章的 <strong>Pandas DataFrame</strong> 就是「加上欄位名稱、功能超強」的二維表格。')},

    {'id': 20, 'title': '第四節 隨堂測驗', 'chapter': '第四節：二維串列', 'bg': 'purple', 'quiz': 'q4',
     'html': quiz_cover('第四節 隨堂測驗', '二維串列 ｜ 3 題')},

    # ── 實作與總結 ──
    {'id': 21, 'title': '本週實作', 'chapter': '實作與總結', 'bg': 'white',
     'html': title('✏️ 本週實作：Colab ＋ 線上練習')
     + colab('py06_list.ipynb', '第 6 課 Colab 練習（6 題）', '索引小試身手、最高分、最低分、總和平均、成績單、等差數列')
     + oj([('#401、#402', '認識串列、串列的實作（測驗）'), ('#403', '計算最高銷售量（VPL）'), ('#404', '計算最高與最低銷售量（VPL）'),
           ('#405', '計算總銷量與平均銷量（VPL）'), ('#406、#407', '二維串列的表示、索引與元素（測驗）'),
           ('#408', '計算銷售總和（VPL）'), ('#409', 'Ch4 學習評量')])},

    {'id': 22, 'title': '本週總結', 'chapter': '實作與總結', 'bg': 'navy',
     'html': recap('本週重點',
                   [('串列', '[ ] 裝一串資料；len() 取長度'),
                    ('索引', '從 0 開始到 n−1；−1 是最後一個'),
                    ('打擂台', '從第一個開始比，找最大最小'),
                    ('二維串列', 'c[i][j] 先列後行；雙重迴圈走訪')],
                   '「資料結構選對了，程式就簡單了一半。」',
                   '下一章：排序與搜尋——讓資料井然有序、一找就到')},
]

QUIZZES = {
    'q1': {'title': '第一節 隨堂測驗', 'questions': [
        {'q': 'a = [81, 82, 83, 84, 85]，a[1] 是？',
         'options': ['81', '82', '83', '錯誤'],
         'answer': 1,
         'explain': '索引從 0 開始，a[0] 是 81，a[1] 是第 2 個元素 82。'},
        {'q': '串列有 10 個元素，最後一個元素的索引是？',
         'options': ['10', '9', '-0', '11'],
         'answer': 1,
         'explain': 'n 個元素的索引是 0 到 n−1，所以最後一個是 9，也可以寫 a[-1]。'},
        {'q': 'b = [1, 2, 3, 4, 5, 6]，b[-2] 是？',
         'options': ['2', '5', '4', '錯誤'],
         'answer': 1,
         'explain': '反向索引 −1 是最後一個（6），−2 是倒數第 2 個（5）。'},
        {'q': '執行 a = [1, 2, 3] 後 print(a[3]) 會？',
         'options': ['印出 3', '印出 0', '出現 IndexError', '印出 None'],
         'answer': 2,
         'explain': '長度 3 的串列索引只有 0、1、2。a[3] 超出範圍，出現 IndexError: list index out of range。'},
    ]},
    'q2': {'title': '第二節 隨堂測驗', 'questions': [
        {'q': 'a = [81, 82, 83, 84, 85]，a[1:3] 是？',
         'options': ['[81, 82, 83]', '[82, 83]', '[82, 83, 84]', '[81, 82]'],
         'answer': 1,
         'explain': '切片從索引 1 開始，到索引 3「之前」為止，所以是索引 1、2：[82, 83]。'},
        {'q': '想在購物車串列 cart 的最後加入 "便當"，應該寫？',
         'options': ['cart + "便當"', 'cart.append("便當")', 'cart[len(cart)] = "便當"', 'cart.add("便當")'],
         'answer': 1,
         'explain': 'append() 在串列最後加入一個元素。cart[len(cart)] 超出範圍會出錯；list 沒有 add 方法。'},
        {'q': 'print("西瓜" in ["蘋果", "橘子", "香蕉"]) 的結果是？',
         'options': ['True', 'False', '-1', '錯誤'],
         'answer': 1,
         'explain': 'in 判斷是否為成員，西瓜不在串列中，所以是 False。'},
        {'q': '[0] * 3 的結果是？',
         'options': ['[0]', '0', '[0, 0, 0]', '[3]'],
         'answer': 2,
         'explain': '串列乘以整數 n，代表把元素重複 n 次，得到 [0, 0, 0]。'},
    ]},
    'q3': {'title': '第三節 隨堂測驗', 'questions': [
        {'q': '用「打擂台法」找最大值，mx 的初始值最好設為？',
         'options': ['0', 'score[0]', '100', '-1'],
         'answer': 1,
         'explain': '用串列的第一個元素當初始值，不管資料是正是負都正確。設 0 的話，如果全部是負數就會錯。'},
        {'q': '以下程式輸出？\na = [3, 8, 2]\nt = 0\nfor x in a:\n    t += x\nprint(t / len(a))',
         'options': ['13', '4.333333333333333', '4', '3'],
         'answer': 1,
         'explain': '總和 3 + 8 + 2 = 13，len(a) = 3，13 / 3 ≈ 4.33（/ 的結果是浮點數）。'},
        {'q': '想知道最低分是「第幾號」同學，用哪種 for 寫法比較方便？',
         'options': ['for s in score:', 'for i in range(len(score)):', 'while True:', '不需要迴圈'],
         'answer': 1,
         'explain': '用索引 i 走訪，找到最低分時記下 i，座號就是 i + 1。for s in score 只拿得到值，不知道位置。'},
    ]},
    'q4': {'title': '第四節 隨堂測驗', 'questions': [
        {'q': 'c = [[1, 2, 3], [4, 5, 6]]，c[1][0] 是？',
         'options': ['2', '4', '1', '5'],
         'answer': 1,
         'explain': '先列後行：c[1] 是第 2 列 [4, 5, 6]，再取索引 0，是 4。'},
        {'q': 'c = [[1, 2, 3], [4, 5, 6]]，len(c) 和 len(c[0]) 分別是？',
         'options': ['2 和 3', '3 和 2', '6 和 3', '2 和 6'],
         'answer': 0,
         'explain': 'len(c) 是列數（2 個子串列）；len(c[0]) 是第一列的長度（3 個元素）。'},
        {'q': '計算每位同學總分時，t = 0 應該放在哪裡？',
         'options': ['兩個迴圈外面', '外圈迴圈裡、內圈迴圈前', '內圈迴圈裡面', '程式最後'],
         'answer': 1,
         'explain': '每換一位同學（外圈每一輪）就要重新從 0 開始累加，所以放在外圈裡、內圈前。'},
    ]},
}

QUIZZES = safe_quizzes(QUIZZES)
