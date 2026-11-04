# -*- coding: utf-8 -*-
# 第 12 週：Pandas 資料分析與開放資料（Colab：py09_pandas）
from content._kit import *

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一節：認識 NumPy 與 Pandas', 'start': 2},
    {'name': '第二節：DataFrame 操作', 'start': 7},
    {'name': '第三節：畫圖與開放資料', 'start': 13},
    {'name': '第四節：機器學習入門', 'start': 19},
    {'name': '實作與總結', 'start': 24},
]

SCORES = py('import pandas as pd\ndf = pd.DataFrame({\n    "姓名": ["小安", "小柏", "小晴", "小哲", "小瑜"],\n    "國文": [65, 92, 78, 83, 70],\n    "英文": [90, 72, 76, 93, 56],\n    "數學": [81, 85, 91, 89, 77],\n    "社會": [79, 53, 47, 94, 80],\n})\ndf', '用「字典」建立 DataFrame：鍵是欄名，值是一欄的資料')

SLIDES = [
    {'id': 1, 'title': 'Pandas 資料分析與機器學習', 'chapter': '封面', 'bg': 'navy',
     'html': cover('🐼', 'Pandas 與機器學習', 'NumPy · Pandas · Open Data · Machine Learning',
                   ['📋 DataFrame', '📈 畫圖表', '🚲 YouBike 開放資料', '🤖 機器學習'], '第 12 週')},

    # ── 第一節 ──
    {'id': 2, 'title': '從串列到資料分析', 'chapter': '第一節：認識 NumPy 與 Pandas', 'bg': 'white',
     'html': title('🚀 從串列升級到資料分析工具')
     + table(['工具', '資料結構', '像什麼'],
             [['Python 內建', 'list、dict、tuple、set', '一個一個自己處理'],
              ['NumPy', 'ndarray（N 維陣列）', '高速計算的數字矩陣'],
              ['Pandas', 'Series（一維）、DataFrame（二維）', '有欄名的 Excel 表格，還能寫程式']], ['20%', '42%', '38%'])
     + note('🧠 第 6 章的二維串列要自己寫雙重迴圈算平均；用 Pandas 一行 ' + ic('df.mean()') + ' 就好。但懂原理，才知道 Pandas 在幫你做什麼。')},

    {'id': 3, 'title': 'NumPy', 'chapter': '第一節：認識 NumPy 與 Pandas', 'bg': 'white',
     'html': title('🔢 NumPy：Numerical Python')
     + two_col(py('import numpy as np\na = np.array([60, 70, 80, 90])\nprint(a + 5)       # 每個元素都加 5\nprint(a.mean(), a.max())', '', '[65 75 85 95]\n75.0 90'),
               card('blue', '為什麼比 list 快？', '① 元素型態都一樣<br>② 存在記憶體<strong>連續</strong>區塊<br>③ 運算用 C 語言實作<br><br>'
                    '資料科學、機器學習套件幾乎都建立在 NumPy 之上。', '⚡'), '1.2fr 1fr')
     + note('💡 ' + ic('a + 5') + ' 自動套用到每個元素，這叫<strong>廣播（broadcasting）</strong>；用 list 的話要自己寫迴圈。')},

    {'id': 4, 'title': 'Series', 'chapter': '第一節：認識 NumPy 與 Pandas', 'bg': 'white',
     'html': title('📏 Series：有標籤的一維資料')
     + two_col(py('import pandas as pd\nse = pd.Series([60, 70, 80, 90, 100],\n               index=["a", "b", "c", "d", "e"])\nprint(se.sum(), se.mean(), se.median())\nprint(se.iloc[0], se.loc["c"])', '',
                  '400 80.0 80.0\n60 80'),
               table(['寫法', '意思'], [['iloc[0]', '用<strong>位置</strong>取（integer location）'], ['loc["c"]', '用<strong>標籤</strong>取（location）'],
                                     ['describe()', '一次看完統計摘要']], ['40%', '60%']), '1.3fr 1fr')},

    {'id': 5, 'title': 'DataFrame', 'chapter': '第一節：認識 NumPy 與 Pandas', 'bg': 'white',
     'html': title('📋 DataFrame：有欄名的表格')
     + two_col(SCORES,
               table(['', '姓名', '國文', '英文', '數學', '社會'],
                     [['0', '小安', '65', '90', '81', '79'], ['1', '小柏', '92', '72', '85', '53'], ['2', '小晴', '78', '76', '91', '47'],
                      ['3', '小哲', '83', '93', '89', '94'], ['4', '小瑜', '70', '56', '77', '80']]), '1.1fr 1fr')
     + note('📌 左邊的 0～4 是<strong>索引（index）</strong>，上面的姓名、國文…是<strong>欄（columns）</strong>。在 Colab 最後一行寫 ' + ic('df') + ' 就會顯示漂亮的表格。')},

    {'id': 6, 'title': '第一節 隨堂測驗', 'chapter': '第一節：認識 NumPy 與 Pandas', 'bg': 'purple', 'quiz': 'q1',
     'html': quiz_cover('第一節 隨堂測驗', 'NumPy 與 Pandas ｜ 4 題')},

    # ── 第二節 ──
    {'id': 7, 'title': '取欄與取列', 'chapter': '第二節：DataFrame 操作', 'bg': 'white',
     'html': title('🎯 取出想要的欄和列')
     + table(['想做什麼', '寫法'],
             [['取一欄（得到 Series）', 'df["數學"]'], ['取多欄（得到 DataFrame）', 'df[["英文", "數學"]]'],
              ['取一列', 'df.loc[2]　或　df.iloc[2]'], ['取一格', 'df.loc[0, "國文"]　或　df.iloc[0, 1]'],
              ['前／後幾筆', 'df.head(3)、df.tail(2)'], ['欄名與筆數', 'df.columns、len(df)、df.shape']], ['42%', '58%'])
     + note('⚠️ 取多欄要用<strong>兩層中括號</strong>：外層是取欄，內層是「欄名的串列」。')},

    {'id': 8, 'title': '篩選', 'chapter': '第二節：DataFrame 操作', 'bg': 'white',
     'html': title('🔎 篩選：只留下符合條件的列')
     + two_col(py('print(df[df["英文"] > 80])\n\ncond = (df["國文"] > 70) & (df["英文"] > 70)\nprint(df[cond])', '',
                  '   姓名  國文  英文  數學  社會\n0  小安  65  90  81  79\n3  小哲  83  93  89  94\n\n   姓名  國文  英文  數學  社會\n1  小柏  92  72  85  53\n2  小晴  78  76  91  47\n3  小哲  83  93  89  94'),
               card('red', '和 if 不一樣！', 'Pandas 的「且」用 <strong>&amp;</strong>、「或」用 <strong>|</strong>、「非」用 <strong>~</strong>，'
                    '<br>而且<strong>每個條件都要加括號</strong>。<br><br>寫成 and / or 會出現 ValueError。', '⚠️'), '1.4fr 1fr')},

    {'id': 9, 'title': '排序與統計', 'chapter': '第二節：DataFrame 操作', 'bg': 'white',
     'html': title('📶 排序與統計')
     + two_col(py('df.sort_values("數學", ascending=False)\n\nprint(df["國文"].mean())\nprint(df["國文"].max(), df["國文"].min())\ndf.describe()', '',
                  '77.6\n92 65'),
               table(['函式', '意義'], [['sum()', '總和'], ['mean()', '平均'], ['median()', '中位數'], ['max() / min()', '最大／最小'],
                                     ['std()', '標準差'], ['describe()', '一次全部']], ['45%', '55%']), '1.3fr 1fr')
     + note('🔁 對照第 7 章：' + ic('sort_values()') + ' 就是幫你做好的排序演算法。')},

    {'id': 10, 'title': '新增欄位', 'chapter': '第二節：DataFrame 操作', 'bg': 'white',
     'html': title('➕ 新增欄位：總分與平均')
     + py('subjects = ["國文", "英文", "數學", "社會"]\ndf["總分"] = df[subjects].sum(axis=1)\ndf["平均"] = df[subjects].mean(axis=1).round(1)\ndf.sort_values("總分", ascending=False)', 'axis=1 代表「橫向」對每一列加總',
          '   姓名  國文  英文  數學  社會   總分    平均\n3  小哲  83  93  89  94  359  89.8\n0  小安  65  90  81  79  315  78.8\n1  小柏  92  72  85  53  302  75.5\n2  小晴  78  76  91  47  292  73.0\n4  小瑜  70  56  77  80  283  70.8')
     + note('🧠 對照第 6 章的成績單：雙重迴圈＋累加器，Pandas 一行完成。注意排序後索引（0～4）會跟著資料一起移動。')},

    {'id': 11, 'title': '分組統計', 'chapter': '第二節：DataFrame 操作', 'bg': 'white',
     'html': title('🗂️ groupby：分組統計')
     + two_col(py('df["組別"] = ["A", "B", "A", "B", "A"]\nprint(df.groupby("組別")["數學"].mean())', '',
                  '組別\nA    83.0\nB    87.0\nName: 數學, dtype: float64'),
               card('green', '像試算表的樞紐分析', '先依某一欄「分組」，再對每組做統計（count、sum、mean、max…）。<br><br>'
                    '例：各行政區有幾個 YouBike 站？各縣市 AQI 平均？', '📊'), '1.2fr 1fr')},

    {'id': 12, 'title': '第二節 隨堂測驗', 'chapter': '第二節：DataFrame 操作', 'bg': 'purple', 'quiz': 'q2',
     'html': quiz_cover('第二節 隨堂測驗', 'DataFrame 操作 ｜ 4 題')},

    # ── 第三節 ──
    {'id': 13, 'title': '畫圖', 'chapter': '第三節：畫圖與開放資料', 'bg': 'white',
     'html': title('📈 df.plot()：一行畫圖')
     + two_col(py('df.plot(kind="bar", x="姓名",\n        y=["國文", "英文", "數學", "社會"],\n        title="各科成績", figsize=(8, 4))', ''),
               table(['kind', '圖表', '適合'], [['line', '折線圖', '隨時間變化'], ['bar / barh', '長條圖', '比較大小'], ['pie', '圓餅圖', '占比'],
                                             ['hist', '直方圖', '分布'], ['scatter', '散佈圖', '兩變數關係']], ['26%', '30%', '44%']), '1.1fr 1fr')
     + note('🀄 Colab 預設字型不支援中文，圖上中文會變方塊。Colab 練習檔裡有一段「下載台北黑體並設定」的程式，先執行它。', 'yellow', '')},

    {'id': 14, 'title': '選對圖表', 'chapter': '第三節：畫圖與開放資料', 'bg': 'white',
     'html': title('🎨 選對圖表，資料才會說話')
     + grid(2,
            card('blue', '一週 AQI 變化', '→ <strong>折線圖</strong>：看趨勢', '📉'),
            card('green', '各區 YouBike 可借車數', '→ <strong>橫條圖</strong>（排序後）：比大小', '📊'),
            card('yellow', '班上通勤方式比例', '→ <strong>圓餅圖</strong>：看占比（類別不要太多）', '🥧'),
            card('purple', '讀書時數 vs 成績', '→ <strong>散佈圖</strong>：看有沒有關係（相關不等於因果！）', '⚬'))
     + note('✅ 好圖表檢查：有標題、有座標軸名稱與單位、註明資料來源與日期。')},

    {'id': 15, 'title': '讀取檔案', 'chapter': '第三節：畫圖與開放資料', 'bg': 'white',
     'html': title('📂 讀取各種資料')
     + table(['資料格式', '讀法', '例子'],
             [['CSV', 'pd.read_csv(網址或路徑)', '政府開放資料最常見的格式'], ['JSON', 'pd.read_json(網址)', 'YouBike、公車等即時資料 API'],
              ['Excel', 'pd.read_excel(路徑)', '學校成績、問卷匯出'], ['網頁表格', 'pd.read_html(網址)', '發票中獎號碼、股價表格']], ['18%', '40%', '42%'])
     + note('☁️ 讀 Google 雲端硬碟的檔案：先執行 ' + ic('from google.colab import drive') + '、' + ic('drive.mount("/content/drive")') + '，路徑以 /content/drive/MyDrive/ 開頭。')},

    {'id': 16, 'title': '政府開放資料', 'chapter': '第三節：畫圖與開放資料', 'bg': 'white',
     'html': title('🇹🇼 政府資料開放平臺 data.gov.tw')
     + grid(3,
            card('blue', '交通', 'YouBike 即時資訊、公車動態、停車場剩餘車位', '🚲', True),
            card('green', '環境', '空氣品質 AQI、雨量、地震（環境部、氣象署）', '🌏', True),
            card('yellow', '生活', '圖書館、公園、人口統計、餐廳衛生評核', '🏙️', True))
     + note('📜 使用開放資料要注意授權條款（多數採「政府資料開放授權條款」），使用時要<strong>註明來源</strong>；即時資料要記下<strong>取得時間</strong>。')},

    {'id': 17, 'title': 'YouBike 範例', 'chapter': '第三節：畫圖與開放資料', 'bg': 'white',
     'html': title('🚲 範例：YouBike 2.0 臺北市即時資訊')
     + py('url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"\nyb = pd.read_json(url)\nyb = yb[["sna", "sarea", "ar", "Quantity", "available_rent_bikes", "available_return_bikes"]]\nyb.columns = ["站名", "區域", "地址", "總車位", "可借", "可還"]\nprint(len(yb))\nprint(yb.groupby("區域")["站名"].count().sort_values(ascending=False).head(3))', '資料集：data.gov.tw 編號 137993')
     + note('🔧 真實資料會變：這份資料的「總車位」欄位名稱曾經從 total 改成 Quantity。讀進來先用 ' + ic('yb.columns') + ' 檢查欄位，程式出錯時第一個懷疑它。', 'yellow', '')},

    {'id': 18, 'title': '第三節 隨堂測驗', 'chapter': '第三節：畫圖與開放資料', 'bg': 'purple', 'quiz': 'q3',
     'html': quiz_cover('第三節 隨堂測驗', '畫圖與開放資料 ｜ 4 題')},

    # ── 第四節 ──
    {'id': 19, 'title': '什麼是機器學習', 'chapter': '第四節：機器學習入門', 'bg': 'white',
     'html': title('🤖 機器學習：讓電腦從資料中找規則')
     + two_col(card('blue', '傳統程式（前 8 章）', '<strong>人</strong>寫好規則 → 電腦照做<br><br>例：' + ic('if bmi < 18.5: print("過輕")')
                    + '<br>規則是我們依標準寫進去的。', '👩‍💻'),
               card('green', '機器學習', '給電腦<strong>大量資料＋答案</strong> → 電腦<strong>自己找出規則</strong>（模型）→ 用模型預測新資料<br><br>'
                    '例：看過上千張貓狗照片，學會分辨新照片是貓還是狗。', '🧠'), '1fr 1fr')
     + note('🧩 上學期第 8 章學過「巨量資料與資料科學」：資料越多、越乾淨，機器學到的規則通常越好。')},

    {'id': 20, 'title': '機器學習的步驟', 'chapter': '第四節：機器學習入門', 'bg': 'white',
     'html': title('🪜 機器學習的步驟')
     + steps([('收集資料', '例如花的尺寸、天氣紀錄、照片'), ('整理資料', '清理缺值、選欄位——本週前三節學的 Pandas'),
              ('切分資料', '大部分拿來<strong>訓練</strong>，留一部分<strong>測試</strong>（模型沒看過的考卷）'),
              ('訓練模型', '選一種演算法（例如決策樹），讓它從訓練資料學規則'),
              ('評估與預測', '用測試資料算準確率，再拿來預測新資料')], 'teal')
     + table(['類型', '說明', '例子'],
             [['監督式學習', '資料有標準答案', '垃圾郵件分類、房價預測'], ['非監督式學習', '沒有答案，讓電腦自己分群', '顧客分群'],
              ['強化學習', '做對給獎勵、做錯給懲罰', '下棋 AI、機器人走路']], ['22%', '40%', '38%'])},

    {'id': 21, 'title': '決策樹實作', 'chapter': '第四節：機器學習入門', 'bg': 'white',
     'html': title('🌳 實作：用決策樹分辨鳶尾花')
     + two_col(py('from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.tree import DecisionTreeClassifier\n\niris = load_iris()\nX, y = iris.data, iris.target          # 特徵、答案\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.3, random_state=42)\n\nmodel = DecisionTreeClassifier(max_depth=3)\nmodel.fit(X_train, y_train)            # 訓練\nprint("準確率", model.score(X_test, y_test))\nnew = [[5.1, 3.5, 1.4, 0.2]]           # 一朵新的花\nprint(iris.target_names[model.predict(new)])', 'scikit-learn 套件，Colab 已內建', "準確率 1.0\n['setosa']"),
               card('purple', '資料長什麼樣？', '150 朵鳶尾花，每朵有 4 個<strong>特徵</strong>：花萼長、花萼寬、花瓣長、花瓣寬（公分），'
                    '以及 1 個<strong>答案</strong>：3 個品種之一。<br><br>決策樹學到的規則像一連串 if-else：'
                    '「花瓣長 ≤ 2.45 → setosa；否則再看花瓣長、花瓣寬…」<br><br>⚠️ 測試資料只有 45 朵，準確率 1.0 不代表永遠不會錯。', '🌸'), '1.5fr 1fr')
     + note('🔗 決策樹其實就是電腦<strong>自動產生的 if-elif-else</strong>——和第 3 章自己寫的判斷結構一樣，只是規則從資料學來。')},

    {'id': 22, 'title': 'AI 的限制與責任', 'chapter': '第四節：機器學習入門', 'bg': 'white',
     'html': title('⚖️ 免寫程式體驗與 AI 的限制')
     + two_col(card('orange', 'Teachable Machine', 'Google 的免寫程式機器學習工具：用鏡頭拍幾十張「石頭、剪刀、布」，'
                    '幾分鐘就能訓練出辨識模型，並可匯出給程式使用。<br><br>teachablemachine.withgoogle.com', '📷'),
               card('red', '模型會出錯', '① <strong>資料偏差</strong>：訓練資料只有某些人，模型對其他人就不準<br>'
                    '② <strong>準確率不是 100%</strong>：重要決定（醫療、錄取）要有人把關<br>'
                    '③ <strong>隱私</strong>：拍照、收集資料前要經過同意', '⚠️'), '1fr 1.2fr')
     + note('🧠 「垃圾進、垃圾出」（Garbage in, garbage out）：資料品質決定模型品質。')},

    {'id': 23, 'title': '第四節 隨堂測驗', 'chapter': '第四節：機器學習入門', 'bg': 'purple', 'quiz': 'q4',
     'html': quiz_cover('第四節 隨堂測驗', '機器學習入門 ｜ 4 題')},

    # ── 實作與總結 ──
    {'id': 24, 'title': '本週實作', 'chapter': '實作與總結', 'bg': 'white',
     'html': title('✏️ 本週實作：YouBike 資料分析 ＋ 第一個 AI 模型')
     + colab('py09_pandas.ipynb', '第 9 課 Colab 練習（6 題）', 'DataFrame 篩選排序、總分平均、畫圖、YouBike 分組統計、決策樹分類鳶尾花')
     + grid(4,
            card('gray', '① 各區站數', 'groupby 計數'),
            card('gray', '② 各區可借車數', '加總後畫橫條圖'),
            card('gray', '③ 文山區前 5 站', '篩選＋排序'),
            card('gray', '④ 決策樹', '改 max_depth，比較準確率'))
     + rubric_box('4 題完成、圖表有標題，並用文字寫出 2 個發現（含資料取得時間）', '4 題完成且結果正確',
                  '完成 2–3 題', '完成 1 題以下')},

    {'id': 25, 'title': '本週總結', 'chapter': '實作與總結', 'bg': 'navy',
     'html': recap('本週重點',
                   [('NumPy / Pandas', '陣列與表格：取欄、篩選、排序、統計'),
                    ('畫圖與開放資料', 'df.plot()；read_csv / read_json；欄位會變先檢查'),
                    ('機器學習', '資料＋答案 → 模型自己找規則 → 預測'),
                    ('負責任的 AI', '資料偏差、準確率、隱私都要考慮')],
                   '「資料不會自己說話，要靠你問對問題。」',
                   '下週起：期末專題——用 API 與 Gradio 做與人互動的程式')},
]

QUIZZES = {
    'q1': {'title': '第一節 隨堂測驗', 'questions': [
        {'q': 'Pandas 中「二維、有欄名的表格」資料結構叫做？',
         'options': ['Series', 'DataFrame', 'list', 'ndarray'],
         'answer': 1,
         'explain': 'DataFrame 是二維表格，每一欄有名稱；Series 是一維、有標籤的資料。'},
        {'q': 'NumPy 陣列 a = np.array([1, 2, 3])，a * 2 的結果是？',
         'options': ['[1, 2, 3, 1, 2, 3]', '[2 4 6]', '錯誤', '12'],
         'answer': 1,
         'explain': 'NumPy 的運算會套用到每個元素（廣播），得到 [2 4 6]。如果是 Python list，[1, 2, 3] * 2 才會變成重複兩次。'},
        {'q': 'se = pd.Series([60, 70, 80], index=["a", "b", "c"])，se.loc["b"] 是？',
         'options': ['60', '70', '80', '"b"'],
         'answer': 1,
         'explain': 'loc 用標籤取值，標籤 "b" 對應的是 70。用位置取則寫 se.iloc[1]。'},
        {'q': 'NumPy 處理大量資料比 list 快的原因，下列何者「錯誤」？',
         'options': ['元素型態都相同', '資料存在連續的記憶體區塊', '核心運算用 C 實作', '它會自動刪除不需要的資料'],
         'answer': 3,
         'explain': 'NumPy 快是因為型態一致、記憶體連續、底層用 C 實作，並不會自動刪除資料。'},
    ]},
    'q2': {'title': '第二節 隨堂測驗', 'questions': [
        {'q': '要取出 df 的「英文」和「數學」兩欄，正確寫法是？',
         'options': ['df["英文", "數學"]', 'df[["英文", "數學"]]', 'df.英文.數學', 'df("英文", "數學")'],
         'answer': 1,
         'explain': '取多欄要用兩層中括號，內層是欄名的串列。'},
        {'q': '篩選「國文 > 80 且 英文 > 80」，正確寫法是？',
         'options': ['df[df["國文"] > 80 and df["英文"] > 80]', 'df[(df["國文"] > 80) & (df["英文"] > 80)]',
                     'df[df["國文"] > 80 & df["英文"] > 80]', 'df.filter(國文 > 80, 英文 > 80)'],
         'answer': 1,
         'explain': 'Pandas 的「且」用 &，而且每個條件要加括號；用 and 會出現 ValueError，不加括號則運算順序會出錯。'},
        {'q': 'df.sort_values("數學", ascending=False) 的作用是？',
         'options': ['數學由小到大排序', '數學由大到小排序', '刪除數學欄', '計算數學平均'],
         'answer': 1,
         'explain': 'ascending 是「遞增」，設為 False 就是遞減，也就是由大到小。'},
        {'q': 'df[subjects].sum(axis=1) 是在算什麼？',
         'options': ['每一科的全班總分', '每位同學各科加起來的總分', '全部成績的總和', '每一科的平均'],
         'answer': 1,
         'explain': 'axis=1 代表橫向，對每一列（每位同學）把各科加起來。axis=0（預設）才是每一欄（每一科）往下加總。'},
    ]},
    'q3': {'title': '第三節 隨堂測驗', 'questions': [
        {'q': '想呈現「過去 7 天 AQI 的變化趨勢」，最適合哪種圖？',
         'options': ['圓餅圖', '折線圖', '散佈圖', '直方圖'],
         'answer': 1,
         'explain': '隨時間變化的資料用折線圖最能看出上升、下降的趨勢。'},
        {'q': 'YouBike 即時資料是 JSON 格式，用 Pandas 讀取應該用？',
         'options': ['pd.read_csv()', 'pd.read_json()', 'pd.read_excel()', 'open()'],
         'answer': 1,
         'explain': 'JSON 格式用 read_json()；CSV 才用 read_csv()。'},
        {'q': 'Colab 畫出來的圖，中文字都變成方塊，原因是？',
         'options': ['資料錯了', '預設字型不支援中文，需要另外設定中文字型', 'Pandas 不能處理中文', '網路斷線'],
         'answer': 1,
         'explain': 'matplotlib 預設字型沒有中文字，下載並設定中文字型（例如台北黑體）就能正常顯示。'},
        {'q': '程式昨天還能跑，今天讀開放資料卻出現 KeyError: \'total\'，最可能的原因是？',
         'options': ['電腦中毒', '資料提供者改了欄位名稱', 'Python 版本太舊', 'Colab 壞了'],
         'answer': 1,
         'explain': 'KeyError 代表找不到這個欄位。真實的開放資料欄位可能被改名，先用 df.columns 看目前的欄位名稱再修改程式。'},
    ]},
    'q4': {'title': '第四節 隨堂測驗', 'questions': [
        {'q': '機器學習和傳統程式設計最大的不同是？',
         'options': ['機器學習不需要電腦', '傳統程式由人寫規則；機器學習由電腦從資料中找出規則', '機器學習一定 100% 正確', '傳統程式不能做判斷'],
         'answer': 1,
         'explain': '傳統程式是人把規則寫成 if-else；機器學習是給電腦資料與答案，讓它自己歸納出規則（模型）。'},
        {'q': '為什麼要把資料切成「訓練資料」和「測試資料」？',
         'options': ['讓檔案變小', '用模型沒看過的資料檢驗它學得好不好', '因為電腦記憶體不夠', '測試資料是給老師看的'],
         'answer': 1,
         'explain': '用訓練過的資料考試，就像拿寫過的考卷再考一次，分數會太好看。測試資料才能看出模型對新資料的表現。'},
        {'q': '「給電腦大量已標記『垃圾郵件／正常郵件』的信件來學習分類」屬於哪一類？',
         'options': ['監督式學習', '非監督式學習', '強化學習', '不是機器學習'],
         'answer': 0,
         'explain': '資料附有標準答案（標記），讓模型學會對應關係，就是監督式學習。'},
        {'q': '一個人臉辨識模型的訓練照片幾乎都是同一族群，最可能發生什麼問題？',
         'options': ['模型會跑得比較快', '對其他族群的辨識準確率較差（資料偏差）', '完全不會有影響', '模型會自動補足資料'],
         'answer': 1,
         'explain': '模型只能學到資料裡有的東西。訓練資料不夠多元，就會對沒看過的族群判斷較差，這是 AI 公平性的重要議題。'},
    ]},
}

QUIZZES = safe_quizzes(QUIZZES)
