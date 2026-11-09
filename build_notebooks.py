#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""產生 115 學年高一第二學期 Python 的 Colab 練習檔。

一份原始內容同時輸出兩種版本：
  notebooks/pyXX_*.ipynb              練習版（學生用，push 到 GitHub，網站上按「在 Colab 開啟」）
  notebooks_answers/pyXX_*_解答.ipynb  解答版（老師用，已列在 .gitignore，不會上傳）

儲存格寫法：
  md('文字')                 說明（Markdown）
  demo('程式')               示範程式：兩版都有完整程式碼
  ex('練習版提示', '解答')    練習題：練習版只有提示註解，解答版有完整程式碼
用法：python build_notebooks.py
"""
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = 'fhehshs/city-tech-115-2'
OJ = 'http://103.226.213.97/course/view.php?id=2109'


def md(t):
    return ('md', t.strip('\n'), None)


def demo(code):
    return ('demo', code.strip('\n'), None)


def ex(hint, ans):
    return ('ex', hint.strip('\n'), ans.strip('\n'))


def header(no, title, goals):
    g = '\n'.join(f'- {x}' for x in goals)
    return md(f"""# 城市科技 Python 第 {no} 課：{title}
臺北市芳和實驗中學 高一第二學期 ｜ 許惠淑老師

**本課目標**
{g}

> 📌 開始前：請先按「**檔案 → 在雲端硬碟中儲存副本**」，再在自己的副本上作答，否則關掉就不見了！
> 💻 線上練習（Online Judge）：[{OJ}]({OJ})""")


# ════════════════════════════════════════════════════════════
NB = {}

# ── 1. Colab 與輸出入 ──────────────────────────────────────
NB['py01_hello_colab'] = [
    header(1, '認識 Colab 與輸出入', ['會使用 Colab 的程式碼／文字儲存格', '會用 print() 輸出、input() 輸入', '會用 # 寫註解']),
    md("""## 一、認識 Colab 環境
1. 建議設定：**工具 → 設定 → 編輯器**，把「自動觸發程式碼完成功能」**取消勾選**，自己打字才記得住語法。
2. 儲存格有兩種：
   - **程式碼**：寫 Python，按左邊 ▶ 或 `Shift + Enter` 執行
   - **文字**：寫說明，支援 [Markdown 語法](https://markdown.tw/)，也可以寫數學式，例如 $f(x)=ax^2+bx+c$"""),
    md("""## 二、print()：讓電腦說話
語法：`print(資料1, 資料2, ..., sep=' ', end='\\n')`
- 多個資料用逗號 `,` 隔開，輸出時預設以**空格**分隔（`sep`）
- 每次輸出完預設會**換行**（`end`）"""),
    md("### 1. 輸出多個字串（逗號隔開，輸出會以空格分開）"),
    demo('print("Hello", "Python")'),
    md("### 2. 直接輸出數字或運算結果"),
    demo('print(1 + 2)\nprint(999 + 88888888 + 88888 + 777777)'),
    md("### 3. 結合字串與運算式"),
    demo('print("1+2=", 1 + 2)'),
    md("### 4. 字串可用 `+` 串接、`*` 重複"),
    demo('print("Hello" + "Python!")\nprint("Go! " * 5)'),
    md("### 5. 試試 sep 與 end"),
    demo('print("2026", "11", "04", sep="/")\nprint("不換行", end="")\nprint("…接在後面")'),
    md("""## 三、input()：讓使用者輸入
語法：`變數 = input("提示字串")`

⚠️ `input()` 拿到的一定是**字串**；要計算時必須先用 `int()` 或 `float()` 轉換。"""),
    demo('name = input("請輸入您的名字：")\nprint("你好，", name)'),
    md("""## 四、註解
`#` 後面到行尾都是註解，不會被執行。選取多行後按 `Ctrl + /` 可以一次加上或取消註解。"""),
    md("""## ✏️ 實作 1：說出你的身高
讓螢幕顯示「輸入你的身高」，使用者輸入後，顯示「您的身高是ＯＯ公分」。"""),
    ex('# 提示：用 input() 取得身高，再用 print() 把文字和身高一起輸出\n',
       'h = input("輸入你的身高：")\nprint("您的身高是", h, "公分")'),
    md("""## ✏️ 實作 2：自我介紹機
輸入「姓名」和「最喜歡的城市」，輸出：`我是ＯＯＯ，我最喜歡ＯＯ！`（提示：試著用 `sep=""` 讓文字不要有多餘空格）"""),
    ex('# 在這裡寫程式\n',
       'name = input("姓名：")\ncity = input("最喜歡的城市：")\nprint("我是", name, "，我最喜歡", city, "！", sep="")'),
    md("""## ✏️ 實作 3：f-string 小預告
Python 3.6 之後可以用 **f-string** 把變數直接放進字串：`f"你好，{name}"`。請改寫實作 2，用 f-string 輸出。"""),
    ex('# 提示：print(f"我是{name}，...")\n',
       'name = input("姓名：")\ncity = input("最喜歡的城市：")\nprint(f"我是{name}，我最喜歡{city}！")'),
    md(f"""## 🏁 完成後
到 [線上練習網站]({OJ}) 完成 **#301 輸出指令、#302 讓電腦說哈囉、#303 輸入指令、#304 讓電腦對您說 Hello**。"""),
]

# ── 2. 變數與運算子 ────────────────────────────────────────
NB['py02_variables'] = [
    header(2, '變數、資料型態與運算子', ['知道變數命名規則與 4 種基本資料型態', '會用 int()、float()、str() 轉換型態', '會用算術、關係、邏輯運算子寫運算式']),
    md("""## 一、變數命名規則
1. 第 1 個字必須是**英文字母或底線 `_`**，不能是數字
2. 之後可以是英文字母、數字、底線
3. **大小寫不同**：`Score` 和 `score` 是兩個變數
4. 不能用保留字（如 `if`、`for`、`print` 雖不是保留字但也別拿來當變數名稱！）"""),
    md("""## 二、基本資料型態
| 型態 | 名稱 | 例子 |
|---|---|---|
| `int` | 整數 | `2`、`-15` |
| `float` | 浮點數 | `2.0`、`3.14` |
| `str` | 字串 | `"Hello"`、`'台北'` |
| `bool` | 布林值 | `True`、`False`（第一個字母大寫） |

用 `type()` 可以查型態："""),
    demo('print(type(2), type(2.0), type("2"), type(True))'),
    md("### 為什麼要轉換型態？試試看下面兩行的差別："),
    demo('a = input("輸入一個數字：")\nprint(a + a)            # 字串相加 → 接起來\nprint(int(a) + int(a))  # 轉成整數 → 真的相加'),
    md("""## ✏️ 實作 1：兩科成績
提示使用者輸入資訊和英文成績（可能有小數），以一行一科顯示，最後顯示總分。"""),
    ex('# 提示：成績可能有小數，用 float(input(...))\n',
       'a = float(input("請輸入資訊成績："))\nb = float(input("請輸入英文成績："))\nprint("資訊成績", a)\nprint("英文成績", b)\nprint("總分", a + b)'),
    md("""## 三、指定運算 `=`
`=` 是「把右邊的值存到左邊的變數」，不是數學的等於。

**小試身手**：(1) `sum = 0` 後執行 `sum = sum + 3`，sum = ?　(2) `x = 1, y = 0`，執行 `x = y` 和 `y = x` 後，x、y = ?"""),
    ex('# 先猜答案寫在註解，再執行驗證\n# (1) 我猜：\n# (2) 我猜：\n',
       'sum = 0\nsum = sum + 3\nprint(sum)        # 3\nx, y = 1, 0\nx = y\ny = x\nprint(x, y)       # 0 0（x 先被改成 0，y 再拿到 0）'),
    md("""## 四、算術運算子
| 運算子 | 意義 | 例子 | 結果 |
|---|---|---|---|
| `+ - *` | 加減乘 | `7 * 2` | `14` |
| `/` | 除（結果是 float） | `7 / 2` | `3.5` |
| `//` | 整數除法（商） | `7 // 2` | `3` |
| `%` | 取餘數 | `7 % 2` | `1` |
| `**` | 次方 | `16 ** 0.5` | `4.0` |

優先順序：`**` → `* / // %` → `+ -`，有括號先算括號。"""),
    ex('# 先猜再執行：\nprint(7 / 2)\nprint(3 * 5 % 2 - 1)\nprint(7 // 2)\nprint(16 ** 0.5)\n',
       'print(7 / 2)          # 3.5\nprint(3 * 5 % 2 - 1)  # 15 % 2 = 1，1 - 1 = 0\nprint(7 // 2)         # 3\nprint(16 ** 0.5)      # 4.0'),
    md("## ✏️ 實作 2：圓的面積與周長（圓周率用 3.14）"),
    ex('# 輸入半徑 r，輸出面積 pi*r*r 與周長 2*pi*r\n',
       'pi = 3.14\nr = float(input("請輸入半徑："))\nprint("面積", pi * r * r)\nprint("周長", 2 * pi * r)'),
    md("## ✏️ 實作 3：英呎英吋換公分（1 英呎 = 12 英吋，1 英吋 = 2.54 公分）"),
    ex('# 輸入幾英呎、幾英吋，輸出公分數\n',
       'f = int(input("輸入英呎："))\ni = int(input("輸入英吋："))\nprint((f * 12 + i) * 2.54, "公分")'),
    md("## ✏️ 實作 4：幾打又幾支（一打 12 支）"),
    ex('# 提示：// 求打數，% 求剩下幾支\n',
       'n = int(input("輸入支數："))\nprint("共", n // 12, "打又", n % 12, "支")'),
    md("## ✏️ 實作 5：滿千折百（每滿 1000 元折 100 元），輸入消費金額，輸出應付金額"),
    ex('# 提示：先算出「滿了幾個 1000」\n',
       'm = int(input("消費金額："))\nprint("應付金額", m - (m // 1000) * 100)'),
    md("""## 五、關係運算子：結果是 True 或 False
`>`、`>=`、`<`、`<=`、`==`（等於）、`!=`（不等於）

⚠️ `=` 是指定，`==` 才是比較！

**小試身手**：`a, b, c = 3, 5, 3`，判斷 (1) a 是否等於 b　(2) b 是否不等於 c　(3) a+b 是否小於 c"""),
    ex('a, b, c = 3, 5, 3\n# (1)\n# (2)\n# (3)\n',
       'a, b, c = 3, 5, 3\nprint(a == b)      # False\nprint(b != c)      # True\nprint(a + b < c)   # False'),
    md("""## 六、邏輯運算子 `and`、`or`、`not`
數學的 `80 ≤ s ≤ 89` 要寫成 `s >= 80 and s <= 89`（Python 也接受 `80 <= s <= 89`）。

**小試身手**：寫出條件式 (1) n 可被 2 整除　(2) n 不能被 3 整除　(3) n 可被 2 整除但不能被 3 整除　(4) a、b、c 能構成三角形（任兩邊和大於第三邊）"""),
    ex('n = 10\na, b, c = 3, 4, 5\n# (1)\n# (2)\n# (3)\n# (4)\n',
       'n = 10\na, b, c = 3, 4, 5\nprint(n % 2 == 0)\nprint(n % 3 != 0)\nprint(n % 2 == 0 and n % 3 != 0)\nprint(a + b > c and b + c > a and a + c > b)'),
    md(f"""## 🏁 完成後
到 [線上練習網站]({OJ}) 完成 **#305～#313**（重點：#307 計算兩銷量之和、#310 滿千折百、#311 銷量總和與平均）。"""),
]

# ── 3. 選擇結構 ────────────────────────────────────────────
NB['py03_if'] = [
    header(3, '循序與選擇結構', ['理解結構化程式設計的三種結構', '會寫兩數交換', '會用 if、if-else、if-elif-else 做判斷']),
    md("""## 一、循序結構：兩數交換
`x = 1, y = 0`，想交換成 `x = 0, y = 1`。下面的寫法對嗎？為什麼？
```python
x = y
y = x
```"""),
    ex('# 寫一程式，輸入兩整數 x、y，交換後輸出\n# 提示：需要一個暫存變數 t\n',
       'x = int(input("x="))\ny = int(input("y="))\nt = x\nx = y\ny = t\nprint(x, y)'),
    md("Python 還有一行交換的寫法："),
    demo('x, y = 1, 0\nx, y = y, x\nprint(x, y)'),
    md("""## 二、if：條件成立才執行
```python
if 條件式:
    敘述（要縮排！）
```
- 條件式後面一定要有冒號 `:`
- 區塊內要**縮排**（Colab 預設 2 格，常見 4 格，同一區塊要一致）"""),
    demo('age = 20\nif age >= 18:\n    print("你的年齡", age)\n    print("成年")'),
    md("""## 三、if - else：二選一"""),
    md("## ✏️ 實作 1：判斷奇數或偶數"),
    ex('# 輸入整數 n，輸出「奇數」或「偶數」\n',
       'n = int(input("n="))\nif n % 2 == 0:\n    print("偶數")\nelse:\n    print("奇數")'),
    md("## ✏️ 實作 2：59 分自動加 1 分（輸入成績，如果是 59 分就變 60 分，輸出最後成績）"),
    ex('# 在這裡寫程式\n',
       's = int(input("成績："))\nif s == 59:\n    s = s + 1\nprint(s)'),
    md("""## ✏️ 實作 3：三數中的最大數
一次輸入三個數（用空白隔開），可以用：`a, b, c = map(int, input().split())`"""),
    ex('a, b, c = map(int, input("輸入三個整數（空白隔開）：").split())\n# 找出最大的數 max_n\n',
       'a, b, c = map(int, input("輸入三個整數（空白隔開）：").split())\nmax_n = a\nif b > max_n:\n    max_n = b\nif c > max_n:\n    max_n = c\nprint("最大數", max_n)'),
    md("""## 四、if - elif - else：多選一
依序檢查，**第一個成立**的區塊會被執行，其他就跳過。"""),
    md("""## ✏️ 實作 4：成績等第
優：90～100　甲：80～89　乙：70～79　丙：60～69　丁：未滿 60"""),
    ex('# 輸入成績，輸出等第\n',
       's = int(input("成績："))\nif s >= 90:\n    print("優")\nelif s >= 80:\n    print("甲")\nelif s >= 70:\n    print("乙")\nelif s >= 60:\n    print("丙")\nelse:\n    print("丁")'),
    md("""## ✏️ 實作 5：購物節折扣
1000（含）以上 95 折、2000 以上 9 折、3000 以上 85 折、4000 以上 8 折。輸入購物金額，輸出實付金額。

💡 想一想：條件要從大的金額先判斷，還是從小的先判斷？為什麼？"""),
    ex('# 在這裡寫程式\n',
       'm = int(input("購物金額："))\nif m >= 4000:\n    m = m * 0.8\nelif m >= 3000:\n    m = m * 0.85\nelif m >= 2000:\n    m = m * 0.9\nelif m >= 1000:\n    m = m * 0.95\nprint("實付金額", int(m))'),
    md("""## ✏️ 實作 6：BMI 判斷（BMI = 體重(kg) / 身高(m)²）
| BMI | 判定 |
|---|---|
| 未滿 18.5 | 過輕 |
| 18.5～未滿 24 | 正常範圍 |
| 24～未滿 27 | 過重 |
| 27 以上 | 肥胖 |

（標準依衛福部國民健康署成人 BMI 分級）"""),
    ex('# 輸入身高(cm)、體重(kg)，輸出 BMI（小數 2 位）與判定\n# 提示：f"{bmi:.2f}" 可以只顯示 2 位小數\n',
       'h = float(input("身高(cm)：")) / 100\nw = float(input("體重(kg)："))\nbmi = w / (h * h)\nprint(f"BMI = {bmi:.2f}")\nif bmi < 18.5:\n    print("過輕")\nelif bmi < 24:\n    print("正常範圍")\nelif bmi < 27:\n    print("過重")\nelse:\n    print("肥胖")'),
    md(f"""## 🏁 完成後
到 [線上練習網站]({OJ}) 完成 **#314～#319**（#315 兩數交換、#317 自動加 1 元、#318 計算最高銷量、#319 購物折扣計算）。"""),
]

# ── 4. 迴圈 ────────────────────────────────────────────────
NB['py04_loops'] = [
    header(4, '重複結構：for 與 while', ['會用 for 搭配 range()', '會用雙重迴圈印圖形', '會用 while 與 break']),
    md("""## 一、for 迴圈與 range()
| 寫法 | 產生的數 |
|---|---|
| `range(6)` | 0, 1, 2, 3, 4, 5 |
| `range(2, 6)` | 2, 3, 4, 5（不含 6） |
| `range(2, 15, 3)` | 2, 5, 8, 11, 14 |
| `range(10, 0, -2)` | 10, 8, 6, 4, 2 |"""),
    demo('for i in range(2, 15, 3):\n    print(i, end=" ")'),
    md("## ✏️ 實作 1：輸出 50 行 Hello Python!"),
    ex('# 在這裡寫程式\n',
       'for i in range(50):\n    print("Hello Python!")'),
    md("## ✏️ 實作 2：計算 1 + 2 + … + n"),
    ex('n = int(input("n="))\ntotal = 0\n# 用 for 迴圈把 1 到 n 加進 total\n\nprint("1 加到", n, "的和", total)\n',
       'n = int(input("n="))\ntotal = 0\nfor i in range(1, n + 1):\n    total = total + i\nprint("1 加到", n, "的和", total)'),
    md("💡 變數不要命名成 `sum`，因為 `sum()` 是 Python 內建函式，蓋掉後就不能用了。"),
    md("""## ✏️ 延伸活動（任選 3 題）
(1) 3 + 6 + 9 + … + 150　(2) 1 ~ n 所有偶數和　(3) 1 ~ n 中「7 的倍數或個位數是 7」的和　(4) 1 × 2 × 3 × … × n"""),
    ex('# (1)\n\n# (2)\n\n# (3)\n\n# (4)\n',
       't = 0\nfor i in range(3, 151, 3):\n    t += i\nprint(t)\n\nn = int(input("n="))\nt = 0\nfor i in range(2, n + 1, 2):\n    t += i\nprint(t)\n\nt = 0\nfor i in range(1, n + 1):\n    if i % 7 == 0 or i % 10 == 7:\n        t += i\nprint(t)\n\np = 1\nfor i in range(1, n + 1):\n    p *= i\nprint(p)'),
    md("""## 二、雙重迴圈
外迴圈控制「列」，內迴圈控制「每列印幾個」。`print(..., end="")` 讓輸出不換行。"""),
    demo('for i in range(4):\n    for j in range(6):\n        print("*", end="")\n    print()'),
    md("## ✏️ 實作 3：印出星號三角形（輸入 n，第 i 列印 i 個 *）"),
    ex('n = int(input("n="))\n# 提示：內迴圈的次數跟著 i 改變\n',
       'n = int(input("n="))\nfor i in range(1, n + 1):\n    for j in range(i):\n        print("*", end="")\n    print()'),
    md("## ✏️ 實作 4：九九乘法表"),
    ex('# 輸出 1x1=1 到 9x9=81\n',
       'for i in range(1, 10):\n    for j in range(1, 10):\n        print(f"{i}x{j}={i*j:2d}", end="  ")\n    print()'),
    md("""## 三、while 迴圈
條件成立就一直做，**一定要讓條件有機會變成 False**，否則會變無窮迴圈（按儲存格左邊的 ■ 可以停止）。"""),
    demo('i = 1\nwhile i < 6:\n    print(i)\n    i = i + 1'),
    md("""## ✏️ 實作 5：成績加分
每多寫一個作業成績乘 1.05（去除小數），例如 70 → 73 → 76…。輸入起始成績和期望成績，輸出至少要多寫幾個作業。"""),
    ex('# 在這裡寫程式\n',
       's = int(input("起始成績："))\ngoal = int(input("期望成績："))\ncount = 0\nwhile s < goal:\n    s = int(s * 1.05)\n    count += 1\nprint("至少要多完成", count, "個作業")'),
    md("""## ✏️ 實作 6：密碼驗證（break）
密碼是 `fhehs2027`，打錯 3 次就拒絕；只按 Enter（空白）不算打錯。"""),
    ex('# 提示：while True 搭配 break\n',
       'wrong = 0\nwhile True:\n    pw = input("請輸入密碼：")\n    if pw == "":\n        continue\n    if pw == "fhehs2027":\n        print("登入成功")\n        break\n    wrong += 1\n    print("密碼錯誤", wrong, "次")\n    if wrong == 3:\n        print("拒絕存取")\n        break'),
    md(f"""## 🏁 完成後
到 [線上練習網站]({OJ}) 完成 **#320～#328**（#321、#323、#325 星號三角形、#326、#327、#328 業績計算）。"""),
]

# ── 5. 學習挑戰 ────────────────────────────────────────────
NB['py05_challenge'] = [
    header(5, '學習挑戰：綜合應用題', ['綜合運用輸入輸出、選擇與重複結構', '練習把題目拆解成「輸入 → 處理 → 輸出」', '在練習網站完成「學習挑戰」挑戰 1～9']),
    md("""## 解題四步驟
1. **讀題**：輸入是什麼？輸出長什麼樣？
2. **舉例**：自己用 2～3 組數字手算一次
3. **寫程式**：先求對，再求快
4. **測試**：包含邊界值（0、最大值、剛好等於條件的值）

> ⚠️ 這 9 題和練習網站「學習挑戰」的**挑戰 1～9** 格式相同：`input()` 括號內**不要寫提示字**，輸出要和範例**一字不差**。
> 在這裡用範例測過，再貼到練習網站按「評估」。"""),
    md("""### 挑戰 1：梯形面積
輸入梯形的上底、下底、高（**3 行**，每行一個正整數），輸出面積，**小數點後 1 位**。

範例輸入：`3`、`5`、`4`（分 3 行）→ 範例輸出：`16.0`

💡 固定小數位數：`f"{x:.1f}"`；只輸出數字，不要加「面積 =」"""),
    ex('# 在這裡寫程式\n', 'a = int(input())\nb = int(input())\nh = int(input())\nprint(f"{(a + b) * h / 2:.1f}")'),
    md("""### 挑戰 2：絕對值
輸入一個整數（可能是負數或 0），輸出它的絕對值。**不可以使用 abs()**。

範例輸入：`-7` → 範例輸出：`7`"""),
    ex('# 在這裡寫程式\n', 'a = int(input())\nif a < 0:\n    a = -a\nprint(a)'),
    md("""### 挑戰 3：三角形周長與面積
輸入三邊長（**1 行**，3 個正整數以空格隔開）。能構成三角形：第 1 行輸出周長，第 2 行輸出面積（**小數點後 2 位**）；不能構成就輸出「無法構成三角形」。

| 範例輸入 | 範例輸出 |
|---|---|
| `3 4 5` | `12`<br>`6.00` |
| `1 2 3` | `無法構成三角形` |

💡 任兩邊之和要**大於**第三邊；海龍公式 $s=(a+b+c)/2$，面積 $=\\sqrt{s(s-a)(s-b)(s-c)}$，開根號用 `** 0.5`"""),
    ex('# 在這裡寫程式\n', 'a, b, c = map(int, input().split())\nif a + b > c and a + c > b and b + c > a:\n    s = (a + b + c) / 2\n    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5\n    print(a + b + c)\n    print(f"{area:.2f}")\nelse:\n    print("無法構成三角形")'),
    md("""### 挑戰 4：糖果分裝
糖果最多 N 個（輸入 N）。7 個一數餘 5、11 個一數餘 5、17 個一數餘 5，由小到大每行輸出一個可能的數量；**一個都沒有就輸出「無」**。

| 範例輸入 | 範例輸出 |
|---|---|
| `3000` | `5`<br>`1314`<br>`2623` |
| `4` | `無` |

💡 窮舉法：一個一個試；可以用一個變數記錄有沒有找到過"""),
    ex('# 在這裡寫程式\n', 'n = int(input())\nfound = False\nfor i in range(1, n + 1):\n    if i % 7 == 5 and i % 11 == 5 and i % 17 == 5:\n        print(i)\n        found = True\nif not found:\n    print("無")'),
    md("""### 挑戰 5：儲蓄計畫
輸入第 1 個月存的金額 m 和目標金額 g（**1 行**，以空格隔開）。之後每個月比前一個月多存 10%（去除小數，用 `int(m * 1.1)`）。每個月輸出一行，直到累計金額**超過** g 為止（第 1 個月一定要輸出）。

| 範例輸入 | 範例輸出 |
|---|---|
| `500 1000` | `第1個月存500元，共500元`<br>`第2個月存550元，共1050元` |

💡 逗號是**全形**「，」，文字和數字之間沒有空格"""),
    ex('# 在這裡寫程式\n', 'm, g = map(int, input().split())\ntotal = m\ni = 1\nprint(f"第{i}個月存{m}元，共{total}元")\nwhile total <= g:\n    m = int(m * 1.1)\n    total += m\n    i += 1\n    print(f"第{i}個月存{m}元，共{total}元")'),
    md("""### 挑戰 6：Sagit 計分程式（ZeroJudge a053）
輸入答對題數 n：0～10 題每題 6 分；11～20 題的部分每題 2 分；21～40 題的部分每題 1 分；40 題以上一律 100 分。輸出分數。

範例輸入：`25` → 範例輸出：`85`

💡 先手算 10、11、20、21、40、41 題各幾分，測資會考邊界值"""),
    ex('# 在這裡寫程式\n', 'n = int(input())\nif n <= 10:\n    s = n * 6\nelif n <= 20:\n    s = 60 + (n - 10) * 2\nelif n <= 40:\n    s = 80 + (n - 20)\nelse:\n    s = 100\nprint(s)'),
    md("""### 挑戰 7：兩光法師占卜術（ZeroJudge a003）
輸入生日的月 M、日 D（**1 行**，以空格隔開），S = (M×2 + D) % 3；S 為 0、1、2 分別輸出「普通」「吉」「大吉」。

範例輸入：`3 5` → 範例輸出：`大吉`"""),
    ex('# 在這裡寫程式\n', 'm, d = map(int, input().split())\ns = (m * 2 + d) % 3\nif s == 0:\n    print("普通")\nelif s == 1:\n    print("吉")\nelse:\n    print("大吉")'),
    md("""### 挑戰 8：盈數、虧數和完全數（ZeroJudge d010）
輸入正整數 n，n 除了自己以外的所有因數加起來是 s：s > n 輸出「盈數」，s < n 輸出「虧數」，s = n 輸出「完全數」。

範例輸入：`28` → 範例輸出：`完全數`

💡 1 沒有真因數，s = 0，所以是虧數"""),
    ex('# 在這裡寫程式\n', 'n = int(input())\ns = 0\nfor i in range(1, n):\n    if n % i == 0:\n        s += i\nif s > n:\n    print("盈數")\nelif s < n:\n    print("虧數")\nelse:\n    print("完全數")'),
    md("""### 挑戰 9：印出長方形
輸入 x 和 y（**1 行**，以空格隔開），用 `*` 印出 x 列、每列 y 個的長方形（星號之間沒有空格）。

| 範例輸入 | 範例輸出 |
|---|---|
| `3 5` | `*****`<br>`*****`<br>`*****` |"""),
    ex('# 在這裡寫程式\n', 'x, y = map(int, input().split())\nfor i in range(x):\n    print("*" * y)'),
    md(f"""## 🏁 完成後
到 [線上練習網站]({OJ}) 的「**學習挑戰（第 5 章綜合應用題）**」，把挑戰 1～9 貼上並按「評估」，每題 100 分。"""),
]

# ── 6. 串列 ────────────────────────────────────────────────
NB['py06_list'] = [
    header(6, '串列與二維串列', ['理解串列與索引（從 0 開始）', '會用迴圈處理串列：最大、最小、總和、平均', '會用二維串列做成績單']),
    md("""## 一、為什麼需要串列？
1000 位學生的成績，不可能開 1000 個變數。用串列 `score = [81, 82, 83, 84, 85]` 一個名字就能存全部。

- 索引從 **0** 開始：`score[0]` 是第 1 個，`score[4]` 是第 5 個
- `score[-1]` 是最後一個
- 超出範圍（例如 `score[5]`）會出現 `IndexError`"""),
    md("**小試身手**：`b = [1, 2, 3, 4, 5, 6]`，先猜 `b[0]`、`b[5]`、`b[-1]`、`b[-6]`，再執行驗證。`b[6]` 會怎樣？"),
    ex('b = [1, 2, 3, 4, 5, 6]\n', 'b = [1, 2, 3, 4, 5, 6]\nprint(b[0], b[5], b[-1], b[-6])\n# print(b[6])  # IndexError: list index out of range'),
    md("## 二、串列常用操作"),
    demo('n = [10, 20, 30, 40]\nprint(n, len(n))          # 輸出、長度\nfor x in n:               # 逐一取出元素\n    print(x, end=" ")\nprint()\nfor i in range(len(n)):   # 用索引取出\n    print(i, n[i])\nprint(30 in n, 50 not in n)\nprint(n + [50, 60], [0] * 4)\nprint(n[1:3], n[:2], n[2:])  # 切片\nn[0] = 99\nn.append(70)              # 加在最後\nprint(n)'),
    md("## ✏️ 實作 1：找出最高分（不要用 max()）\n成績：88, 51, 84, 58, 91, 86, 75, 92, 66, 82"),
    ex('score = [88, 51, 84, 58, 91, 86, 75, 92, 66, 82]\n# 提示：先假設第一個最大，再一個一個比\n',
       'score = [88, 51, 84, 58, 91, 86, 75, 92, 66, 82]\nmx = score[0]\nfor s in score:\n    if s > mx:\n        mx = s\nprint("最高分", mx)'),
    md("## ✏️ 實作 2：找出最低分"),
    ex('score = [88, 51, 84, 58, 91, 86, 75, 92, 66, 82]\n',
       'score = [88, 51, 84, 58, 91, 86, 75, 92, 66, 82]\nmn = score[0]\nfor s in score:\n    if s < mn:\n        mn = s\nprint("最低分", mn)'),
    md("## ✏️ 實作 3：計算總分與平均（寫完後用內建的 sum()、len() 驗算）"),
    ex('score = [88, 51, 84, 58, 91, 86, 75, 92, 66, 82]\n',
       'score = [88, 51, 84, 58, 91, 86, 75, 92, 66, 82]\ntotal = 0\nfor s in score:\n    total += s\nprint("總分", total, "平均", total / len(score))\nprint(sum(score), sum(score) / len(score))'),
    md("""## 三、二維串列：先列後行
5 位同學 3 科成績 → 5 × 3 的二維串列，`c[i][j]` 是第 i 列第 j 行（都從 0 開始）。"""),
    demo('c = [[85, 90, 78],\n     [72, 65, 80],\n     [95, 88, 92],\n     [60, 75, 70],\n     [88, 94, 85]]\nprint(c[2])       # 第 3 位同學的成績\nprint(c[2][1])    # 第 3 位同學的第 2 科\nfor i in range(len(c)):\n    for j in range(len(c[i])):\n        print(c[i][j], end=" ")\n    print()'),
    md("## ✏️ 實作 4：成績單\n用上面的串列 c，輸出每位同學的座號、總分、平均（小數 1 位），最後輸出每一科的平均。"),
    ex('c = [[85, 90, 78], [72, 65, 80], [95, 88, 92], [60, 75, 70], [88, 94, 85]]\n',
       'c = [[85, 90, 78], [72, 65, 80], [95, 88, 92], [60, 75, 70], [88, 94, 85]]\nfor i in range(len(c)):\n    t = 0\n    for j in range(len(c[i])):\n        t += c[i][j]\n    print(f"{i+1}號 總分 {t} 平均 {t/len(c[i]):.1f}")\nfor j in range(3):\n    t = 0\n    for i in range(len(c)):\n        t += c[i][j]\n    print(f"第{j+1}科平均 {t/len(c):.1f}")'),
    md("""## ✏️ 實作 5：等差數列
建立 3 個從 0 開始、長度為 4 的等差數列，公差分別是 1、2、3。輸出 `[[0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9]]`"""),
    ex('# 提示：外迴圈跑公差，內迴圈產生 4 個數\n',
       'result = []\nfor d in range(1, 4):\n    row = []\n    for k in range(4):\n        row.append(k * d)\n    result.append(row)\nprint(result)'),
    md(f"""## 🏁 完成後
到 [線上練習網站]({OJ}) 完成 **#401～#409**（#403、#404、#405、#408 計算銷售總和）。"""),
]

# ── 7. 排序與搜尋 ──────────────────────────────────────────
NB['py07_sort_search'] = [
    header(7, '排序與搜尋演算法', ['理解氣泡排序的原理並實作', '會寫循序搜尋', '理解二分搜尋為什麼比較快']),
    md("""## 一、氣泡排序（Bubble Sort）
反覆比較**相鄰**兩個數，前面比後面大就交換。每做完一輪，最大的數會「浮」到最後面。
- n 筆資料最多做 n-1 輪
- 第 i 輪只要比較 n-i 次"""),
    md("## ✏️ 實作 1：把 [4, 3, 5, 1, 2] 由小到大排好，並輸出每一輪的結果"),
    ex('a = [4, 3, 5, 1, 2]\nn = len(a)\n# 外迴圈：第 i 輪；內迴圈：比較 a[j] 和 a[j+1]\n',
       'a = [4, 3, 5, 1, 2]\nn = len(a)\nfor i in range(1, n):\n    for j in range(n - i):\n        if a[j] > a[j + 1]:\n            a[j], a[j + 1] = a[j + 1], a[j]\n    print(f"第{i}輪：", a)'),
    md("💡 Python 內建 `sorted(a)` 和 `a.sort()` 可以直接排序，但理解演算法才知道電腦在做什麼。"),
    md("""## 二、循序搜尋（Sequential Search）
從頭到尾一個一個比，找到就停。資料**不用先排序**，但資料很多時會很慢。"""),
    md("## ✏️ 實作 2：在 [3, 8, 2, 9, 1, 6, 5, 4, 7] 中搜尋使用者輸入的鍵值，找到輸出索引，找不到輸出「沒搜尋到資料」"),
    ex('a = [3, 8, 2, 9, 1, 6, 5, 4, 7]\nkey = int(input("搜尋："))\n',
       'a = [3, 8, 2, 9, 1, 6, 5, 4, 7]\nkey = int(input("搜尋："))\ni = 0\nwhile i < len(a):\n    if a[i] == key:\n        print("在索引", i)\n        break\n    i += 1\nif i == len(a):\n    print("沒搜尋到資料")'),
    md("""## 三、二分搜尋（Binary Search）
資料**必須先排序**。每次看中間那個：比鍵值大就往左半找，比鍵值小就往右半找。每次砍掉一半！

1000 筆資料：循序搜尋最多比 1000 次，二分搜尋最多約 10 次（$2^{10}=1024$）。"""),
    md("## ✏️ 實作 3：在排序好的商品編號中二分搜尋，並輸出比較了幾次"),
    ex('a = [101, 103, 107, 112, 118, 125, 131, 140, 152, 160]\nkey = int(input("商品編號："))\nleft, right = 0, len(a) - 1\n# 提示：mid = (left + right) // 2\n',
       'a = [101, 103, 107, 112, 118, 125, 131, 140, 152, 160]\nkey = int(input("商品編號："))\nleft, right = 0, len(a) - 1\ncount = 0\nfound = -1\nwhile left <= right:\n    mid = (left + right) // 2\n    count += 1\n    if a[mid] == key:\n        found = mid\n        break\n    elif a[mid] > key:\n        right = mid - 1\n    else:\n        left = mid + 1\nprint("索引", found, "比較次數", count)'),
    md("""## 四、APCS 實作題挑戰（選做）
大學程式設計先修檢測（APCS）歷屆第 1 題通常只需要本學期學到的語法：
- [105年3月 第1題 成績指標](https://apcs.csie.ntnu.edu.tw/wp-content/uploads/2018/12/1050305APCSImplementation.pdf)（排序＋找最高不及格與最低及格分數）
- [105年10月 第1題 三角形辨別](https://apcs.csie.ntnu.edu.tw/wp-content/uploads/2018/12/1051029APCSImplementation.pdf)（排序＋判斷）
- [106年3月 第1題 秘密差](https://apcs.csie.ntnu.edu.tw/wp-content/uploads/2018/12/1060304APCSImplementation.pdf)（字串與奇偶位數）"""),
    md("### 成績指標：輸入 n 和 n 個成績，第一行輸出由小到大排序結果；第二行輸出最高的不及格分數（沒有則輸出 best case）；第三行輸出最低的及格分數（沒有則輸出 worst case）"),
    ex('# 在這裡寫程式\n',
       'n = int(input())\na = sorted(map(int, input().split()))\nprint(*a)\nfail = [x for x in a if x < 60]\npas = [x for x in a if x >= 60]\nprint(fail[-1] if fail else "best case")\nprint(pas[0] if pas else "worst case")'),
    md(f"""## 🏁 完成後
到 [線上練習網站]({OJ}) 完成 **#501～#507**（#502 排序商品編號、#504 循序搜尋、#507 二分搜尋商品編號）。"""),
]

# ── 8. 函式與遞迴 ──────────────────────────────────────────
NB['py08_function'] = [
    header(8, '函式與遞迴', ['會定義與呼叫函式、使用參數與回傳值', '理解遞迴的「關係式＋終止條件」', '會用遞迴寫 1+…+n、n!、費氏數列']),
    md("""## 一、函式
`print()`、`input()`、`len()` 都是內建函式。也可以用 `def` 自己定義：
```python
def 函式名稱(參數1, 參數2):
    函式主體
    return 回傳值   # 沒有回傳值可以省略
```"""),
    demo('def sayhello():\n    print("Hello Python!")\n\ndef add(a, b):\n    return a + b\n\nsayhello()\nsayhello()\ns = add(6, 10)\nprint(s)'),
    md("## ✏️ 實作 1：自訂函式 power(a, b) 回傳 a 的 b 次方（用迴圈，不要用 **）"),
    ex('def power(a, b):\n    # 在這裡寫\n    pass\n\nprint(power(2, 10))   # 應該是 1024\n',
       'def power(a, b):\n    p = 1\n    for i in range(b):\n        p *= a\n    return p\n\nprint(power(2, 10))'),
    md("## ✏️ 實作 2：用函式計算半徑 2.1、3.4、5.7、-9.1 的圓面積（半徑是負數要回傳 0 並提示）"),
    ex('def area(r):\n    pass\n\nfor r in [2.1, 3.4, 5.7, -9.1]:\n    print(r, area(r))\n',
       'def area(r):\n    if r < 0:\n        print("半徑不可為負數")\n        return 0\n    return 3.14 * r * r\n\nfor r in [2.1, 3.4, 5.7, -9.1]:\n    print(r, area(r))'),
    md("""## ✏️ 實作 3：最大公因數與最小公倍數
輾轉相除法：`gcd(a, b)`，當 b 為 0 時答案是 a；否則答案等於 `gcd(b, a % b)`。最小公倍數 = a × b ÷ 最大公因數。"""),
    ex('def gcd(a, b):\n    pass\n\na, b = map(int, input("輸入兩數：").split())\n',
       'def gcd(a, b):\n    while b != 0:\n        a, b = b, a % b\n    return a\n\na, b = map(int, input("輸入兩數：").split())\ng = gcd(a, b)\nprint("最大公因數", g, "最小公倍數", a * b // g)'),
    md("""## 二、遞迴：函式呼叫自己
解遞迴問題的兩件事：
1. **遞迴關係式**：大問題怎麼用小問題表示，例如 $f(n) = f(n-1) + n$
2. **終止條件**：最小的問題答案是什麼，例如 $f(1) = 1$（沒有終止條件會無限呼叫，出現 `RecursionError`）"""),
    md("## ✏️ 實作 4：用遞迴計算 1 + 2 + … + n"),
    ex('def f(n):\n    pass\n\nprint(f(100))   # 5050\n', 'def f(n):\n    if n == 1:\n        return 1\n    return f(n - 1) + n\n\nprint(f(100))'),
    md("## ✏️ 實作 5：用遞迴計算 n!（n! = n × (n-1)!，0! = 1）並輸出 10!"),
    ex('def fact(n):\n    pass\n\nprint(fact(10))   # 3628800\n', 'def fact(n):\n    if n <= 1:\n        return 1\n    return n * fact(n - 1)\n\nprint(fact(10))'),
    md("""## ✏️ 實作 6：費氏數列
1, 1, 2, 3, 5, 8, 13…，f(1) = f(2) = 1，f(n) = f(n-1) + f(n-2)。輸出前 15 項。

💡 試試 `f(35)`，是不是要等很久？想想看為什麼（提示：f(3) 被重複算了幾次？）"""),
    ex('def fib(n):\n    pass\n\nfor i in range(1, 16):\n    print(fib(i), end=" ")\n',
       'def fib(n):\n    if n <= 2:\n        return 1\n    return fib(n - 1) + fib(n - 2)\n\nfor i in range(1, 16):\n    print(fib(i), end=" ")'),
    md("## ✏️ 實作 7（挑戰）：把二分搜尋改寫成遞迴函式 bsearch(a, key, left, right)"),
    ex('def bsearch(a, key, left, right):\n    pass\n\na = [101, 103, 107, 112, 118, 125, 131, 140, 152, 160]\nprint(bsearch(a, 131, 0, len(a) - 1))   # 6\n',
       'def bsearch(a, key, left, right):\n    if left > right:\n        return -1\n    mid = (left + right) // 2\n    if a[mid] == key:\n        return mid\n    if a[mid] > key:\n        return bsearch(a, key, left, mid - 1)\n    return bsearch(a, key, mid + 1, right)\n\na = [101, 103, 107, 112, 118, 125, 131, 140, 152, 160]\nprint(bsearch(a, 131, 0, len(a) - 1))'),
    md(f"""## 🏁 完成後
到 [線上練習網站]({OJ}) 完成 **#329 函式、#508～#513**（遞迴 1 加到 n、費氏數列、二分搜尋遞迴、n!）。"""),
]

# ── 9. Pandas ──────────────────────────────────────────────
NB['py09_pandas'] = [
    header(9, 'Pandas 資料分析與機器學習入門', ['認識 NumPy、Pandas 的用途', '會建立 Series、DataFrame 並篩選、排序、統計', '會讀取政府開放資料並畫圖', '會用決策樹訓練第一個機器學習模型']),
    md("""## 一、為什麼用 Pandas？
- **NumPy**：高速的多維陣列運算，是資料科學套件的基礎
- **Pandas**：建立在 NumPy 上，提供像 Excel 表格一樣的 **DataFrame**，可以讀 CSV、JSON、網頁表格
- 參考：[NumPy 官方說明](https://numpy.org/doc/stable/user/whatisnumpy.html)、[Pandas 入門](https://pandas.pydata.org/docs/getting_started/index.html)"""),
    md("## 二、Series：一維資料"),
    demo('import pandas as pd\nse = pd.Series([60, 70, 80, 90, 100], index=["a", "b", "c", "d", "e"])\nprint(se)\nprint(se.sum(), se.mean(), se.max(), se.median())\nprint(se.iloc[0], se.loc["c"])'),
    md("## 三、DataFrame：二維表格"),
    demo('df = pd.DataFrame({\n    "姓名": ["小安", "小柏", "小晴", "小哲", "小瑜"],\n    "國文": [65, 92, 78, 83, 70],\n    "英文": [90, 72, 76, 93, 56],\n    "數學": [81, 85, 91, 89, 77],\n    "社會": [79, 53, 47, 94, 80],\n})\ndf'),
    md("""| 想做什麼 | 寫法 |
|---|---|
| 取一欄 | `df["數學"]` |
| 取多欄 | `df[["英文", "數學"]]` |
| 取一列 | `df.loc[2]` 或 `df.iloc[2]` |
| 前／後幾筆 | `df.head(2)`、`df.tail(2)` |
| 篩選 | `df[df["英文"] > 80]`；且用 `&`、或用 `|`，每個條件要加括號 |
| 排序 | `df.sort_values("英文", ascending=False)` |
| 統計 | `df.describe()`、`df["國文"].mean()` |"""),
    md("## ✏️ 實作 1：(1) 英文超過 80 分的人　(2) 國文和英文都超過 70 分的人　(3) 依數學成績由高到低排序"),
    ex('# (1)\n\n# (2)\n\n# (3)\n',
       'print(df[df["英文"] > 80])\nprint(df[(df["國文"] > 70) & (df["英文"] > 70)])\ndf.sort_values("數學", ascending=False)'),
    md("## ✏️ 實作 2：新增「總分」與「平均」欄位，並找出總分最高的人"),
    ex('# 提示：df[["國文","英文","數學","社會"]].sum(axis=1)，axis=1 代表橫向加總\n',
       'subjects = ["國文", "英文", "數學", "社會"]\ndf["總分"] = df[subjects].sum(axis=1)\ndf["平均"] = df[subjects].mean(axis=1).round(1)\nprint(df.sort_values("總分", ascending=False).head(1))\ndf'),
    md("""## 四、畫圖（中文字型設定）
Colab 預設字型不支援中文，先下載台北黑體並設定："""),
    demo('!wget -q -O taipei_sans_tc_beta.ttf "https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download"\nimport matplotlib\nimport matplotlib.pyplot as plt\nmatplotlib.font_manager.fontManager.addfont("taipei_sans_tc_beta.ttf")\nplt.rcParams["font.sans-serif"] = "Taipei Sans TC Beta"\nplt.rcParams["axes.unicode_minus"] = False'),
    demo('df.plot(kind="bar", x="姓名", y=["國文", "英文", "數學", "社會"], title="各科成績", figsize=(8, 4))\nplt.show()'),
    md("""`kind` 可以是：`line` 折線、`bar` 長條、`barh` 橫條、`hist` 直方圖、`box` 箱型圖、`scatter` 散佈圖（要給 x、y）、`pie` 圓餅圖。

## ✏️ 實作 3：畫出每位同學「總分」的折線圖，加上標記點 marker="o" 與格線 grid=True"""),
    ex('# 在這裡寫程式\n', 'df.plot(kind="line", x="姓名", y="總分", marker="o", grid=True, title="學生總分", figsize=(8, 4))\nplt.show()'),
    md("""## 五、讀取開放資料：YouBike 2.0 臺北市即時資訊
- 資料集：[政府資料開放平臺 137993](https://data.gov.tw/dataset/137993)
- 欄位：`sna` 站名、`sarea` 行政區、`ar` 地址、`Quantity` 總車位（欄位名稱偶爾會改，讀進來先用 `yb.columns` 檢查）、`available_rent_bikes` 可借車數、`available_return_bikes` 可還空位"""),
    demo('url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"\nyb = pd.read_json(url)\nyb = yb[["sna", "sarea", "ar", "Quantity", "available_rent_bikes", "available_return_bikes"]]\nyb.columns = ["站名", "區域", "地址", "總車位", "可借", "可還"]\nyb.head()'),
    md("## ✏️ 實作 4：(1) 每個行政區有幾個站　(2) 每個行政區可借車數總和，畫成橫條圖　(3) 找出文山區可借車數最多的 5 站"),
    ex('# (1) 提示：yb.groupby("區域")["站名"].count()\n\n# (2)\n\n# (3)\n',
       'print(yb.groupby("區域")["站名"].count())\nyb.groupby("區域")["可借"].sum().sort_values().plot(kind="barh", figsize=(6, 6), title="各區可借車數")\nplt.show()\nyb[yb["區域"] == "文山區"].sort_values("可借", ascending=False).head(5)'),
    md("""## ✏️ 實作 5（選做）：自己找一份開放資料
到 [政府資料開放平臺](https://data.gov.tw/) 找一份 CSV 或 JSON 資料，用 `pd.read_csv(網址)` 或 `pd.read_json(網址)` 讀進來，做一個篩選和一張圖，並用文字儲存格寫下你發現了什麼。"""),
    ex('# 資料集名稱：\n# 網址：\n', '# 範例：臺北市立圖書館各分館 https://data.gov.tw/dataset/121431\n# 讀進來後觀察欄位，再做篩選與統計'),
    md("""## 六、機器學習入門：決策樹分辨鳶尾花
傳統程式是「人寫規則」；機器學習是「給電腦資料＋答案，讓它自己找規則」。

步驟：收集資料 → 整理資料 → 切分訓練／測試 → 訓練模型 → 評估與預測

鳶尾花資料集有 150 朵花，每朵 4 個特徵（花萼長、花萼寬、花瓣長、花瓣寬，單位公分）與 1 個答案（3 個品種之一）。"""),
    demo('from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.tree import DecisionTreeClassifier\n\niris = load_iris()\nflowers = pd.DataFrame(iris.data, columns=["花萼長", "花萼寬", "花瓣長", "花瓣寬"])\nflowers["品種"] = [iris.target_names[t] for t in iris.target]\nflowers.sample(5)'),
    demo('X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)\nmodel = DecisionTreeClassifier(max_depth=3, random_state=42)\nmodel.fit(X_train, y_train)                 # 訓練\nprint("測試資料準確率：", model.score(X_test, y_test))'),
    md("看看模型學到的規則（就是一連串的 if-else）："),
    demo('from sklearn.tree import export_text\nprint(export_text(model, feature_names=["花萼長", "花萼寬", "花瓣長", "花瓣寬"]))'),
    md("""## ✏️ 實作 6：
(1) 把 `max_depth` 改成 1、2、5，各自的準確率是多少？用文字儲存格寫下你的觀察。
(2) 預測一朵新花：花萼長 6.5、花萼寬 3.0、花瓣長 5.5、花瓣寬 2.0，模型認為是哪個品種？"""),
    ex('# (1)\n\n# (2) 提示：model.predict([[6.5, 3.0, 5.5, 2.0]])，再用 iris.target_names[...] 轉成品種名稱\n',
       'for d in [1, 2, 3, 5]:\n    m = DecisionTreeClassifier(max_depth=d, random_state=42).fit(X_train, y_train)\n    print("max_depth", d, "準確率", round(m.score(X_test, y_test), 3))\n\npred = model.predict([[6.5, 3.0, 5.5, 2.0]])\nprint(iris.target_names[pred])'),
    md("""> 🤔 想一想：準確率很高，是不是就可以完全相信模型？如果訓練資料只來自某一個地區的花，拿去判斷別的地區的花還會準嗎？

> 📷 免寫程式體驗：[Teachable Machine](https://teachablemachine.withgoogle.com/) 可以用鏡頭拍照，幾分鐘訓練出影像辨識模型。"""),
]

# ── 10. AQI 專題 ───────────────────────────────────────────
NB['py10_aqi_project'] = [
    header(10, '空氣品質 AQI 資料專題', ['會用 requests 呼叫 API、解析 JSON', '會用 Pandas 篩選測站資料', '會把程式包成互動網頁（Gradio）並完成專題']),
    md("""## 一、什麼是 API？
API 就像餐廳的點餐窗口：你照規定的格式「點餐」（送出網址），伺服器就把資料（通常是 JSON）送回來。

本課使用 **環境部環境資料開放平臺** 的「空氣品質指標(AQI)」資料集 `aqx_p_432`。
1. 到 [環境資料開放平臺](https://data.moenv.gov.tw/) 註冊會員，取得自己的 **API Key**
2. 在 Colab 左側 🔑「Secrets（密鑰）」新增名稱 `MOENV_API_KEY`，值貼上 API Key，並開啟「筆記本存取權」

> ⚠️ 不要把 API Key、密碼直接寫在程式碼裡再分享出去！"""),
    demo('import requests\nimport pandas as pd\nfrom google.colab import userdata\n\nAPI_KEY = userdata.get("MOENV_API_KEY")\nurl = f"https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key={API_KEY}&limit=1000&format=JSON"\nr = requests.get(url, timeout=30)\ndata = r.json()\nrecords = data["records"] if isinstance(data, dict) else data\nprint("測站數：", len(records))\nrecords[0]'),
    md("## ✏️ 實作 1：用迴圈輸出每個測站的 縣市、站名、AQI、狀態"),
    ex('# 提示：每一筆 rec 是字典，用 rec["county"]、rec["sitename"]、rec["aqi"]、rec["status"]\n',
       'for rec in records:\n    print(rec["county"], rec["sitename"], rec["aqi"], rec["status"], sep=",")'),
    md("## 二、轉成 DataFrame"),
    demo('df = pd.DataFrame(records)\ndf["aqi"] = pd.to_numeric(df["aqi"], errors="coerce")   # 轉數字，無法轉的變 NaN\ndf = df.dropna(subset=["aqi"])\ndf[["county", "sitename", "aqi", "status", "pm2.5", "publishtime"]].head()'),
    md("## ✏️ 實作 2：(1) 臺北市所有測站 AQI 由高到低　(2) 全臺 AQI 最高的 5 個測站　(3) 古亭站目前的 AQI"),
    ex('# (1)\n\n# (2)\n\n# (3)\n',
       'print(df[df["county"] == "臺北市"].sort_values("aqi", ascending=False)[["sitename", "aqi", "status"]])\nprint(df.sort_values("aqi", ascending=False).head(5)[["county", "sitename", "aqi"]])\naqi = df[df["sitename"] == "古亭"]["aqi"].values[0]\nprint("古亭 AQI", aqi)'),
    md("""## 三、校內空氣盒子（LASS 開源感測資料）
學校的空氣盒子 ID：`B827EB63D1C8`（[網頁版](https://pm25.lass-net.org/data/show.php?device_id=B827EB63D1C8)）。資料時間是 UTC，要 +8 小時才是台灣時間。

若盒子斷電或斷網就會沒有資料，可到 [LASS 地圖](https://pm25.lass-net.org/) 找附近其他盒子的 ID。"""),
    demo('from datetime import datetime, timedelta\nDEVICE = "B827EB63D1C8"\nurl = f"https://pm25.lass-net.org/API-1.0.0/device/{DEVICE}/latest/?format=JSON"\nfeeds = requests.get(url, timeout=30).json()["feeds"]\nbox = None\nif not feeds:\n    print("空氣盒子目前沒有上傳資料，請換一個附近的盒子 ID")\nelse:\n    box = list(feeds[0].values())[0]\n    t = datetime.strptime(f\'{box["date"]} {box["time"]}\', "%Y-%m-%d %H:%M:%S") + timedelta(hours=8)\n    print("時間", t)\n    print("PM2.5", box.get("s_d0"), "溫度", box.get("s_t0"), "濕度", box.get("s_h0"))'),
    md("""## ✏️ 實作 3：比較校內空氣盒子 PM2.5 和最近的官方測站（古亭）pm2.5，誰比較高？差多少？
（空氣盒子是低成本感測器，數值會有誤差，這也是資料分析要注意的地方。）"""),
    ex('# 在這裡寫程式\n',
       'if box is None:\n    print("沒有空氣盒子資料，無法比較")\nelse:\n    school = float(box.get("s_d0"))\n    guting = float(df[df["sitename"] == "古亭"]["pm2.5"].values[0])\n    print("校內", school, "古亭", guting, "差", round(school - guting, 1))'),
    md("""## 四、超過門檻就寄信通知
> 📢 LINE Notify 已於 2025 年 3 月 31 日停止服務，舊範例不能再用。這裡改用 Gmail 寄信。

1. Google 帳戶要開啟兩步驟驗證，再建立「[應用程式密碼](https://support.google.com/accounts/answer/185833)」（學校帳號若無法建立，請用個人帳號）
2. 在 Colab Secrets 新增 `GMAIL_ADDRESS`、`GMAIL_APP_PASSWORD`"""),
    demo('import smtplib\nfrom email.mime.text import MIMEText\n\ndef send_email(subject, body, to):\n    sender = userdata.get("GMAIL_ADDRESS")\n    msg = MIMEText(body, "plain", "utf-8")\n    msg["Subject"], msg["From"], msg["To"] = subject, sender, to\n    with smtplib.SMTP("smtp.gmail.com", 587) as s:\n        s.starttls()\n        s.login(sender, userdata.get("GMAIL_APP_PASSWORD"))\n        s.send_message(msg)'),
    ex('# 實作 4：古亭 AQI 超過 100（對敏感族群不健康）就寄信給自己，否則輸出目前 AQI\n',
       'if aqi > 100:\n    send_email("AQI 警示", f"古亭 AQI {aqi}，請減少戶外活動", userdata.get("GMAIL_ADDRESS"))\n    print("已寄出通知")\nelse:\n    print("古亭 AQI", aqi, "空氣品質尚可")'),
    md("""## 五、Gradio：把程式變成互動網頁
Gradio 可以把一個函式變成有輸入框、按鈕的網頁，執行後會出現一個暫時的分享網址；有效期限有限，Colab 停止執行後就會失效。"""),
    demo('!pip -q install gradio'),
    demo('import gradio as gr\n\ndef bmi(h, w):\n    b = w / (h / 100) ** 2\n    level = "過輕" if b < 18.5 else "正常範圍" if b < 24 else "過重" if b < 27 else "肥胖"\n    return f"你的 BMI 是 {b:.2f}，{level}"\n\ngr.Interface(bmi,\n             inputs=[gr.Number(label="身高（公分）"), gr.Number(label="體重（公斤）")],\n             outputs="text",\n             title="BMI 小幫手").launch()'),
    md("## ✏️ 實作 5：空氣品質查詢器——輸入測站名稱，回傳該站 AQI、狀態與一句建議"),
    ex('def query(site):\n    # 用 df 找出該站資料；找不到要回傳「查無此測站」\n    pass\n\n# gr.Interface(query, inputs=gr.Textbox(label="測站名稱"), outputs="text", title="空氣品質查詢器").launch()\n',
       'def query(site):\n    row = df[df["sitename"] == site.strip()]\n    if row.empty:\n        return "查無此測站"\n    a = int(row["aqi"].values[0])\n    tip = "適合戶外活動" if a <= 50 else "普通，敏感族群留意" if a <= 100 else "建議減少戶外活動"\n    return f"{site} AQI {a}（{row[\'status\'].values[0]}）— {tip}"\n\ngr.Interface(query, inputs=gr.Textbox(label="測站名稱"), outputs="text", title="空氣品質查詢器").launch()'),
    md("""## 🎯 期末專題：用 Python 做一個「與人互動」的資料小工具
**主題自選**（AQI、YouBike、天氣、校內空氣盒子、自己的資料…），必須包含：
1. 取得資料：API 或開放資料檔（註明來源與取得日期）
2. 處理資料：至少 1 個篩選或統計
3. 呈現：1 張圖表 **或** 1 個 Gradio 互動介面
4. 文字說明：動機、做法、發現、遇到的困難

繳交：Colab 共用連結（檢視者權限）＋ 1 分鐘展示。"""),
]


# ════════════════════════════════════════════════════════════
def build(cells, answer):
    nb_cells = []
    for kind, a, b in cells:
        if kind == 'md':
            nb_cells.append({'cell_type': 'markdown', 'metadata': {}, 'source': a})
        else:
            src = b if (kind == 'ex' and answer) else a
            if kind == 'ex':
                src = ('# ✏️ 解答\n' if answer else '# ✏️ 練習\n') + src
            nb_cells.append({'cell_type': 'code', 'metadata': {}, 'execution_count': None,
                             'outputs': [], 'source': src})
    return {'nbformat': 4, 'nbformat_minor': 0,
            'metadata': {'colab': {'provenance': []}, 'language_info': {'name': 'python'},
                         'kernelspec': {'name': 'python3', 'display_name': 'Python 3'}},
            'cells': nb_cells}


def main():
    out_p = os.path.join(ROOT, 'notebooks')
    out_a = os.path.join(ROOT, 'notebooks_answers')
    os.makedirs(out_p, exist_ok=True)
    os.makedirs(out_a, exist_ok=True)
    for name, cells in NB.items():
        for answer, d, fn in [(False, out_p, f'{name}.ipynb'), (True, out_a, f'{name}_解答.ipynb')]:
            with open(os.path.join(d, fn), 'w', encoding='utf-8') as f:
                json.dump(build(cells, answer), f, ensure_ascii=False, indent=1)
        n_ex = sum(1 for c in cells if c[0] == 'ex')
        print(f'✔ {name}: {len(cells)} 格，{n_ex} 題練習')
    print('✅ 練習版 → notebooks/　解答版 → notebooks_answers/（不會上傳）')


if __name__ == '__main__':
    main()
