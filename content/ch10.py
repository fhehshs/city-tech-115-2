# -*- coding: utf-8 -*-
# 第 13–15 週：空氣品質 AQI 資料專題（Colab：py10_aqi_project）
from content._kit import *

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一節：API 與 JSON', 'start': 2},
    {'name': '第二節：AQI 資料分析', 'start': 8},
    {'name': '第三節：通知與互動網頁', 'start': 13},
    {'name': '期末專題', 'start': 18},
]

SLIDES = [
    {'id': 1, 'title': 'AQI 資料專題', 'chapter': '封面', 'bg': 'navy',
     'html': cover('🌫️', '空氣品質資料專題', 'API · JSON · AQI · Gradio · Final Project',
                   ['🔌 API', '🗂️ JSON', '📮 自動通知', '🖥️ Gradio 互動網頁'], '第 13–15 週')},

    # ── 第一節 ──
    {'id': 2, 'title': '專題情境', 'chapter': '第一節：API 與 JSON', 'bg': 'white',
     'html': title('🏃 情境：今天體育課要不要改在室內？')
     + lead('體育老師每天早上都要上網查空氣品質。能不能寫一支程式，<strong>自動抓資料、判斷、通知</strong>，甚至做成網頁讓全校查？')
     + steps([('取得資料', '呼叫環境部的 AQI API（本節）'), ('分析資料', '用 Pandas 找出學校附近測站（第二節）'),
              ('自動通知', '超過門檻就寄信（第三節）'), ('互動網頁', '用 Gradio 做「空氣品質查詢器」（第三節）')], 'teal')},

    {'id': 3, 'title': '什麼是 API', 'chapter': '第一節：API 與 JSON', 'bg': 'white',
     'html': title('🔌 API：程式和程式之間的點餐窗口')
     + two_col(card('blue', '比喻：速食店點餐', '你不用進廚房，只要在窗口<strong>照規定點餐</strong>（送出網址＋參數），'
                    '店員就把餐點<strong>照固定格式</strong>交給你（JSON 資料）。', '🍔'),
               table(['網址的部分', '意思'],
                     [['https://data.moenv.gov.tw/api/v2/aqx_p_432', '資料集：空氣品質指標(AQI)'],
                      ['?api_key=…', '你的通行證'], ['&limit=1000', '最多回傳幾筆'], ['&format=JSON', '回傳格式']], ['58%', '42%']), '1fr 1.3fr')
     + note('🇹🇼 環境部「環境資料開放平臺」提供 AQI 每小時更新的資料。使用前要先<strong>註冊會員取得 API Key</strong>。')},

    {'id': 4, 'title': '保護 API Key', 'chapter': '第一節：API 與 JSON', 'bg': 'white',
     'html': title('🔑 API Key 和密碼一樣，不能外流')
     + two_col(card('red', '❌ 危險寫法', ic('API_KEY = "a1b2c3…"') + '<br>寫在程式碼裡，分享 Colab 給別人時就被看光了。', '🙅'),
               card('green', '✅ 用 Colab Secrets', '左側 🔑 圖示 → 新增密鑰 ' + ic('MOENV_API_KEY') + ' → 開啟存取權<br>'
                    + ic('from google.colab import userdata') + '<br>' + ic('API_KEY = userdata.get("MOENV_API_KEY")'), '🔐'), '1fr 1.3fr')
     + note('🛡️ 資安習慣：金鑰、密碼、個資<strong>不寫進程式、不貼到群組、不上傳到公開的 GitHub</strong>。外流了就到平臺重新產生一組。', 'red', '')},

    {'id': 5, 'title': 'JSON 格式', 'chapter': '第一節：API 與 JSON', 'bg': 'white',
     'html': title('🗂️ JSON：字典和串列組成的資料')
     + two_col(py('{\n  "total": "84",\n  "records": [\n    {"sitename": "古亭", "county": "臺北市",\n     "aqi": "45", "status": "良好", "pm2.5": "9"},\n    {"sitename": "萬華", "county": "臺北市",\n     "aqi": "52", "status": "普通", "pm2.5": "14"}\n  ]\n}', 'API 回傳資料的樣子（示意，數字非實際資料）'),
               table(['符號', 'Python 對應'], [['{ "鍵": 值 }', '字典 dict'], ['[ … ]', '串列 list'], ['"文字"', '字串 str（注意 aqi 也是字串！）']], ['45%', '55%']), '1.3fr 1fr')
     + note('🧠 取值：' + ic('data["records"][0]["sitename"]') + ' → 先取字典的 records（一個串列），再取索引 0，再取 sitename。')},

    {'id': 6, 'title': '呼叫 API', 'chapter': '第一節：API 與 JSON', 'bg': 'white',
     'html': title('💻 用 requests 呼叫 API')
     + py('import requests\nfrom google.colab import userdata\n\nAPI_KEY = userdata.get("MOENV_API_KEY")\nurl = f"https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key={API_KEY}&limit=1000&format=JSON"\ndata = requests.get(url, timeout=30).json()\nrecords = data["records"]\nprint("測站數：", len(records))\nfor rec in records[:3]:\n    print(rec["county"], rec["sitename"], rec["aqi"], rec["status"])', '')
     + note('🧯 出錯時先 ' + ic('print(data)') + ' 看回傳了什麼：常見原因是 API Key 沒設定、網址打錯、平臺維護中。')},

    {'id': 7, 'title': '第一節 隨堂測驗', 'chapter': '第一節：API 與 JSON', 'bg': 'purple', 'quiz': 'q1',
     'html': quiz_cover('第一節 隨堂測驗', 'API 與 JSON ｜ 4 題')},

    # ── 第二節 ──
    {'id': 8, 'title': 'AQI 分級', 'chapter': '第二節：AQI 資料分析', 'bg': 'white',
     'html': title('🚦 空氣品質指標 AQI 分級')
     + table(['AQI', '狀態', '顏色', '活動建議（一般民眾）'],
             [['0–50', '良好', '🟢 綠', '正常戶外活動'], ['51–100', '普通', '🟡 黃', '極特殊敏感族群注意'],
              ['101–150', '對敏感族群不健康', '🟠 橘', '有症狀者減少體力消耗活動'], ['151–200', '對所有族群不健康', '🔴 紅', '減少戶外活動'],
              ['201–300', '非常不健康', '🟣 紫', '減少外出'], ['301–500', '危害', '🟤 褐紅', '避免外出']], ['14%', '26%', '14%', '46%'])
     + note('📚 AQI 依 O₃、PM2.5、PM10、CO、SO₂、NO₂ 等污染物濃度換算，取最大的那一項。分級依環境部空氣品質指標說明。')},

    {'id': 9, 'title': '轉成 DataFrame', 'chapter': '第二節：AQI 資料分析', 'bg': 'white',
     'html': title('📋 把 JSON 變成 DataFrame')
     + py('import pandas as pd\ndf = pd.DataFrame(records)\ndf["aqi"] = pd.to_numeric(df["aqi"], errors="coerce")\ndf = df.dropna(subset=["aqi"])\ndf[["county", "sitename", "aqi", "status", "pm2.5", "publishtime"]].head()', '')
     + grid(2,
            card('yellow', 'pd.to_numeric(…, errors="coerce")', 'API 給的 aqi 是<strong>字串</strong>，要轉成數字才能比大小、排序。轉不了的（例如測站維修沒資料）變成 NaN。', '🔢'),
            card('blue', 'dropna(subset=["aqi"])', '把 aqi 是 NaN 的列刪掉，這就是<strong>資料清理</strong>。', '🧹'))},

    {'id': 10, 'title': '找出學校附近', 'chapter': '第二節：AQI 資料分析', 'bg': 'white',
     'html': title('🏫 分析：臺北市、全臺最高、學校附近')
     + py('# 臺北市各測站 AQI 由高到低\ntpe = df[df["county"] == "臺北市"].sort_values("aqi", ascending=False)\nprint(tpe[["sitename", "aqi", "status"]])\n\n# 全臺 AQI 最高的 5 站\nprint(df.nlargest(5, "aqi")[["county", "sitename", "aqi"]])\n\n# 學校附近：古亭站\naqi = df[df["sitename"] == "古亭"]["aqi"].values[0]\nprint("古亭 AQI", aqi)', '')
     + note('🗺️ 芳和實中在臺北市大安區，較近的環境部測站有古亭、松山等；可以到「空氣品質監測網」地圖上確認距離最近的測站。')},

    {'id': 11, 'title': '校內空氣盒子', 'chapter': '第二節：AQI 資料分析', 'bg': 'white',
     'html': title('📦 校內空氣盒子：LASS 開源感測資料')
     + two_col(card('teal', '兩種資料比一比', '<strong>環境部測站</strong>：精密儀器、數量少、可信度高<br><br>'
                    '<strong>空氣盒子</strong>：低成本感測器、數量多、更貼近身邊，但有誤差、可能斷線', '⚖️'),
               card('orange', '資料的「健康檢查」', '① 有沒有資料？（盒子斷電就沒有）<br>② 時間對嗎？（API 給 UTC 時間，要 +8 小時）<br>'
                    '③ 數值合理嗎？（PM2.5 是負數或幾千就有問題）', '🩺'), '1fr 1fr')
     + note('🔬 比較同一時間「校內盒子」和「最近測站」的 PM2.5，差多少？為什麼會不同？——這就是資料素養。Colab 第 10 課有範例程式。')},

    {'id': 12, 'title': '第二節 隨堂測驗', 'chapter': '第二節：AQI 資料分析', 'bg': 'purple', 'quiz': 'q2',
     'html': quiz_cover('第二節 隨堂測驗', 'AQI 資料分析 ｜ 4 題')},

    # ── 第三節 ──
    {'id': 13, 'title': '自動通知', 'chapter': '第三節：通知與互動網頁', 'bg': 'white',
     'html': title('📮 超過門檻就自動寄信')
     + two_col(py('if aqi > 100:\n    send_email("AQI 警示",\n               f"古亭 AQI {aqi}，建議體育課改室內",\n               收件人)\nelse:\n    print("古亭 AQI", aqi, "空氣品質尚可")', '用到第 3 章的 if 和第 8 章的函式'),
               card('yellow', '通知管道的變化', '舊範例用 <strong>LINE Notify</strong>，但它已在 <strong>2025 年 3 月 31 日停止服務</strong>，程式就不能用了。<br><br>'
                    '這次改用 Gmail（需建立「應用程式密碼」，並存在 Colab Secrets）。', '📢'), '1.2fr 1fr')
     + note('🧠 學到的教訓：依賴外部服務的程式，<strong>服務會改版、會收掉</strong>。寫程式時把「寄通知」包成函式，要換管道只改一個地方。')},

    {'id': 14, 'title': 'Gradio 介紹', 'chapter': '第三節：通知與互動網頁', 'bg': 'white',
     'html': title('🖥️ Gradio：三行把函式變成網頁')
     + two_col(py('import gradio as gr\n\ndef bmi(h, w):\n    b = w / (h / 100) ** 2\n    return f"你的 BMI 是 {b:.2f}"\n\ngr.Interface(bmi,\n    inputs=[gr.Number(label="身高（公分）"),\n            gr.Number(label="體重（公斤）")],\n    outputs="text",\n    title="BMI 小幫手").launch()', '先執行 !pip -q install gradio'),
               steps([('寫一個函式', '參數 = 使用者輸入，return = 顯示的結果'), ('gr.Interface', '告訴 Gradio 有哪些輸入框、輸出什麼'),
                      ('.launch()', 'Colab 會顯示網頁，並給一個暫時的分享網址')], 'purple'), '1.3fr 1fr')
     + note('🔁 第 3 章的 BMI 程式，加上 Gradio 就變成同學可以用手機開的網頁——這就是「<strong>與人互動</strong>」的程式。')},

    {'id': 15, 'title': '空氣品質查詢器', 'chapter': '第三節：通知與互動網頁', 'bg': 'white',
     'html': title('🔍 實作：空氣品質查詢器')
     + py('def query(site):\n    row = df[df["sitename"] == site.strip()]\n    if row.empty:\n        return "查無此測站"\n    a = int(row["aqi"].values[0])\n    if a <= 50:\n        tip = "適合戶外活動"\n    elif a <= 100:\n        tip = "普通，敏感族群留意"\n    else:\n        tip = "建議減少戶外活動"\n    return f"{site} AQI {a}（{row[\'status\'].values[0]}）— {tip}"\n\ngr.Interface(query, inputs=gr.Textbox(label="測站名稱"),\n             outputs="text", title="空氣品質查詢器").launch()', '')
     + note('🧩 整學期的觀念全部用上：<strong>函式、if-elif、字串、Pandas 篩選、f-string</strong>。')},

    {'id': 16, 'title': '把資料用對', 'chapter': '第三節：通知與互動網頁', 'bg': 'white',
     'html': title('⚖️ 負責任地使用資料與程式')
     + grid(2,
            card('blue', '註明來源與時間', '「資料來源：環境部環境資料開放平臺，2026/11/4 10:00 取得」', '📝'),
            card('green', '說清楚限制', '空氣盒子有誤差、測站不在學校正上方、資料每小時才更新', '⚠️'),
            card('yellow', '不要造成恐慌', '寄通知的門檻和措辭要合理，不誇大', '🔕'),
            card('red', '保護金鑰與個資', '分享 Colab 前檢查有沒有 API Key、Email 密碼', '🔐'))},

    {'id': 17, 'title': '第三節 隨堂測驗', 'chapter': '第三節：通知與互動網頁', 'bg': 'purple', 'quiz': 'q3',
     'html': quiz_cover('第三節 隨堂測驗', '通知與互動網頁 ｜ 4 題')},

    # ── 期末專題 ──
    {'id': 18, 'title': '期末專題任務', 'chapter': '期末專題', 'bg': 'white',
     'html': title('🎯 期末專題：用 Python 做一個「與人互動」的資料小工具')
     + colab('py10_aqi_project.ipynb', '第 10 課 Colab：AQI 專題範例', 'API 呼叫、JSON 解析、Pandas 分析、空氣盒子、Gmail 通知、Gradio 查詢器')
     + grid(4,
            card('gray', '① 取得資料', 'API 或開放資料檔，註明來源與取得時間'),
            card('gray', '② 處理資料', '至少 1 個篩選或統計'),
            card('gray', '③ 呈現結果', '1 張圖表或 1 個 Gradio 介面'),
            card('gray', '④ 文字說明', '動機、做法、發現、困難'))
     + note('💡 主題自選：AQI、YouBike、天氣、公車、校內空氣盒子、圖書館…。2～3 人一組，繳交 Colab 共用連結（檢視者權限）＋ 1 分鐘展示。')},

    {'id': 19, 'title': '專題評分規準', 'chapter': '期末專題', 'bg': 'white',
     'html': title('📏 期末專題評分規準')
     + table(['向度', 'A', 'B', 'C', 'D'],
             [['資料取得（20%）', '使用 API 或即時資料，來源、時間完整', '使用開放資料檔，有註明來源', '有資料但來源不清楚', '沒有真實資料'],
              ['程式設計（35%）', '程式正確、有函式與註解、有處理錯誤情況', '程式正確可執行', '部分功能有誤', '無法執行'],
              ['呈現與互動（25%）', 'Gradio 介面或圖表清楚、易用', '有圖表或介面', '呈現不清楚', '沒有呈現'],
              ['說明與展示（20%）', '能說明發現與資料限制', '能說明做法', '說明不完整', '未說明']], ['20%', '20%', '20%', '20%', '20%'])},

    {'id': 20, 'title': '學期總結', 'chapter': '期末專題', 'bg': 'navy',
     'html': recap('這學期你學會了',
                   [('基礎語法', '輸出入、變數、運算、選擇、迴圈'),
                    ('資料結構與演算法', '串列、二維串列、排序、搜尋、遞迴'),
                    ('模組化', '函式：把問題拆小、包成工具'),
                    ('資料應用', 'Pandas、API、Gradio：用程式解決真實問題')],
                   'Stay Hungry, Stay Foolish ！',
                   '從 print("Hello") 到空氣品質查詢器——第 3 學期見：工程設計！')},
]

QUIZZES = {
    'q1': {'title': '第一節 隨堂測驗', 'questions': [
        {'q': '關於 API 的敘述，何者正確？',
         'options': ['API 是一種程式語言', 'API 讓程式可以照規定的格式向服務要資料', 'API 只能在手機上用', 'API 不需要網路'],
         'answer': 1,
         'explain': 'API（應用程式介面）是程式之間溝通的約定：照規定送出請求，就會收到固定格式的資料。'},
        {'q': '要讓 Colab 安全地使用 API Key，最好的做法是？',
         'options': ['直接寫在程式碼第一行', '貼在班級群組方便大家用', '存在 Colab Secrets，用 userdata.get() 讀取', '寫在檔名裡'],
         'answer': 2,
         'explain': '金鑰寫在程式碼裡，分享筆記本時就會外流。存在 Colab Secrets 只有你自己的執行環境讀得到。'},
        {'q': 'JSON 中 { } 和 [ ] 分別對應 Python 的？',
         'options': ['串列、字典', '字典、串列', '字串、數字', '函式、迴圈'],
         'answer': 1,
         'explain': '大括號 { } 是「鍵: 值」的字典，中括號 [ ] 是有順序的串列。'},
        {'q': 'data = {"records": [{"sitename": "古亭"}]}，要取出 "古亭" 應寫？',
         'options': ['data["sitename"]', 'data["records"]["sitename"]', 'data["records"][0]["sitename"]', 'data[0]["sitename"]'],
         'answer': 2,
         'explain': '先取字典的 records（是串列），再取索引 0（第一個字典），最後取 sitename。'},
    ]},
    'q2': {'title': '第二節 隨堂測驗', 'questions': [
        {'q': 'AQI = 120，狀態是？',
         'options': ['良好', '普通', '對敏感族群不健康', '危害'],
         'answer': 2,
         'explain': 'AQI 101～150 為「對敏感族群不健康」（橘色），有症狀的人應減少體力消耗的活動。'},
        {'q': 'API 回傳的 aqi 欄位是字串，為什麼要先用 pd.to_numeric() 轉換？',
         'options': ['讓字變漂亮', '字串不能正確地比大小和排序', '因為 Pandas 不支援中文', '為了刪除資料'],
         'answer': 1,
         'explain': '字串比大小是一個字一個字比，"9" 會大於 "100"。轉成數字後比較、排序、計算才正確。'},
        {'q': 'df.dropna(subset=["aqi"]) 的作用是？',
         'options': ['刪除 aqi 欄', '刪除 aqi 沒有值（NaN）的列', '把 aqi 補成 0', '排序 aqi'],
         'answer': 1,
         'explain': 'dropna 刪除缺值的資料列，subset 指定只看 aqi 欄。這是資料清理的常見步驟。'},
        {'q': '校內空氣盒子的 PM2.5 和環境部測站不一樣，下列解釋何者「最不合理」？',
         'options': ['感測器種類與精度不同', '兩者位置不同', '量測時間可能不同', '程式語言不同造成的'],
         'answer': 3,
         'explain': '數值差異來自儀器、位置、時間等真實因素，和用哪種程式語言讀取資料無關。'},
    ]},
    'q3': {'title': '第三節 隨堂測驗', 'questions': [
        {'q': '舊範例使用 LINE Notify 傳通知，現在無法使用的原因是？',
         'options': ['Python 不支援', 'LINE Notify 已於 2025 年 3 月 31 日停止服務', '學校網路擋住', 'API Key 過期'],
         'answer': 1,
         'explain': 'LINE Notify 已結束服務。依賴外部服務的程式要能隨時更換，所以把「寄通知」包成函式比較好維護。'},
        {'q': 'gr.Interface(fn, inputs=…, outputs=…) 中的 fn 是？',
         'options': ['網頁的顏色', '使用者輸入後要執行的函式', '網址', '圖片'],
         'answer': 1,
         'explain': 'Gradio 會把使用者在輸入框填的值當成參數傳給 fn，再把 fn 的回傳值顯示在輸出區。'},
        {'q': '查詢器函式中，if row.empty: return "查無此測站" 是為了？',
         'options': ['讓程式更快', '處理使用者輸入不存在的測站，避免程式出錯', '刪除資料', '寄送通知'],
         'answer': 1,
         'explain': '使用者可能打錯字。先檢查篩選結果是否為空，否則取 values[0] 會出現 IndexError。'},
        {'q': '分享專題 Colab 給老師前，最重要的檢查是？',
         'options': ['字型大小', '程式碼裡有沒有 API Key、密碼等機密資訊', '有沒有用到 for 迴圈', '檔案大小'],
         'answer': 1,
         'explain': '分享的筆記本別人都看得到程式碼，機密資訊要用 Colab Secrets 存放，分享前務必檢查。'},
    ]},
}

QUIZZES = safe_quizzes(QUIZZES)
