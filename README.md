# 城市科技 Python 高一第二學期 課程網站（115 學年度）

3 學期制的高一第 2 學期：15 週、每週 2 節，對應課程計畫第 15–29 週
（`C:\hs\課程\classroom\課程計畫\高中\115高中部一年級各探索課程計畫自導性撰寫表格 (城市科技)_加大概念.docx`）。

| 章 | 學期週次 | 計畫週次 | 單元 |
|---|---|---|---|
| 1–5 | W1–5 | 15–19 | Colab 與輸出入、變數與運算子、選擇結構、迴圈、學習挑戰 |
| 6 | W6–8 | 20–22 | 串列與二維串列（陣列資料結構） |
| 7 | W9–10 | 23–24 | 排序與搜尋演算法、效能分析 |
| 8 | W11 | 25 | 函式與遞迴 |
| 9 | W12 | 26 | Pandas 資料分析與機器學習 |
| 10 | W13–15 | 27–29 | 期末專題：與人互動的 Python 程式（AQI、Gradio） |

評分依課程計畫：一般作業評量 80%、課堂學習態度 20%（見 `templates/rubric.html`）。
架構與第一學期（city-tech-115-1）、七年級網站（it-g7-115-2）相同。

教材來源：Classroom「Hello Python !」的 113 學年 Colab（Python programming 1–5），
內容已改寫成 115 版；線上練習對應 Moodle「115芳和高中資訊科技Py」(http://103.226.213.97/course/view.php?id=2109)。

## 本機預覽（互動版）

```
pip install flask
python app.py
```
瀏覽器開 http://localhost:5000

## 檔案說明

| 要改什麼 | 檔案 |
|---|---|
| 各章投影片與隨堂測驗 | `content/ch01.py` ～ `content/ch10.py` |
| 共用版型（卡片、程式碼區塊 `py()`、Colab 按鈕 `colab()`、線上練習 `oj()`） | `content/_kit.py` |
| 首頁章節卡片、開放章數（`PUBLISHED`） | `templates/home.html` |
| 評量規準 | `templates/rubric.html` |
| 補充影片 | `content/enhancements.py` |
| **Colab 練習檔內容** | `build_notebooks.py` |

改完先跑 `python validate_site.py .`，顯示「通過 ✅」再匯出。

## Colab 練習檔

```
python build_notebooks.py
```
會產生兩種版本：

| 資料夾 | 內容 | 是否上傳 GitHub |
|---|---|---|
| `notebooks/py01_hello_colab.ipynb` … `py10_aqi_project.ipynb` | 練習版（只有提示） | ✅ 上傳，學生從網站按「在 Colab 開啟」 |
| `notebooks_answers/*_解答.ipynb` | 解答版 | ❌ 已列在 `.gitignore`，只留在老師電腦 |

網站上的「在 Colab 開啟」連結格式是
`https://colab.research.google.com/github/fhehshs/city-tech-115-2/blob/main/notebooks/檔名.ipynb`，
**repo 必須是 Public 且已 push，連結才會有效**。學生開啟後要先「檔案 → 在雲端硬碟中儲存副本」。
解答版可以直接上傳到自己的 Google 雲端硬碟，用 Colab 開啟示範。

第 10 課需要的帳號設定（請學生在 Colab 左側 🔑 Secrets 設定，不要寫在程式裡）：
- `MOENV_API_KEY`：環境部環境資料開放平臺（data.moenv.gov.tw）註冊會員後取得
- `GMAIL_ADDRESS`、`GMAIL_APP_PASSWORD`：寄通知用（Google 帳戶需開兩步驟驗證才能建立應用程式密碼）

## 發布給學生（GitHub Pages）

1. `python build_notebooks.py`（產生 notebooks/）
2. `python make_static.py` → 產生 `docs/`（資料已內嵌，直接雙擊 `docs/index.html` 也能離線看）
3. 第一次上架：GitHub 新增 repo `city-tech-115-2`（**Public**），在此資料夾執行
   ```
   git init
   git add .
   git commit -m "城市科技 Python 115-2 課程網站"
   git branch -M main
   git remote add origin https://github.com/fhehshs/city-tech-115-2.git
   git push -u origin main
   ```
4. GitHub → Settings → Pages → Deploy from a branch → `main` / `/docs` → Save
5. 學生網址：`https://fhehshs.github.io/city-tech-115-2/`

之後更新：改內容 → `python build_notebooks.py` → `python make_static.py` → `git add . && git commit -m "更新" && git push`

## 逐週開放章節
`templates/home.html` 裡的 `const PUBLISHED = 10;` 改成目前要開放的章數，重跑 `make_static.py` 再 push。
