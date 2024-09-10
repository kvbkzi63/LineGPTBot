# LineGPTBot

LineGPTBot 是一個整合 LINE Bot 和 OpenAI ChatGPT 的聊天機器人，能夠讓用戶在 LINE 平台上與 AI 助手進行智能對話。這個專案提供了簡單的對話功能，無需記憶對話歷史。

## 目錄
- [專案介紹](#專案介紹)
- [功能特性](#功能特性)
- [安裝](#安裝)
- [環境變數](#環境變數)

## 專案介紹

LineGPTBot 是一個用於將 LINE Bot 串接到 OpenAI 的 GPT-4（或 GPT-3.5）模型的專案。用戶可以通過 LINE 機器人與 AI 進行自然對話，ChatGPT 將會根據用戶的訊息回應相應的內容。

## 功能特性
- 與 LINE Bot 進行實時對話
- 串接 OpenAI 的 GPT-4 模型進行智能回應
- 支援文字訊息交互

## 安裝

### 先決條件
在開始之前，請確保你已經安裝了以下所需元件：
- Python 3.7+
- [LINE Developers](https://developers.line.biz/) 帳號及 Messaging API 設置
- OpenAI API Key

### 步驟

1. clone此專案到本地：

   ```bash
   git clone https://github.com/your-username/LineGPTBot.git
   cd LineGPTBot

2. 建立虛擬環境並安裝依賴：

   ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    pip install -r requirements.txt

3. 啟動Flask伺服器：
   ```bash
   flask run --host=0.0.0.0 --port=5001
5. 使用 ngrok 或其他工具公開本地伺服器：
   ```bash
   ngrok http 5001

6. 在 LINE Developers 後台設定 Webhook URL，將 ngrok 提供的 URL 設置為 Webhook。


### 環境變數

專案需要以下環境變數設定：
  ```bash
    LINE_CHANNEL_SECRET=your_line_channel_secret
    LINE_CHANNEL_ACCESS_TOKEN=your_line_access_token
    OPENAI_API_KEY=your_openai_api_key



 
