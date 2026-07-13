# 🇻🇳🇨🇳 AI Translator Pro

Bot Telegram dịch tự động Việt ⇄ Trung sử dụng OpenAI GPT.

## Chức năng

- Dịch tự động Việt ⇄ Trung
- Tự nhận diện ngôn ngữ
- Prompt tối ưu cho thương mại
- Hỗ trợ Dictionary riêng
- Bật/Tắt dịch theo từng nhóm
- Tiết kiệm chi phí API
- Dịch tự nhiên theo ngữ cảnh

---

## Cấu trúc Project

```
app/
data/
requirements.txt
Procfile
runtime.txt
README.md
```

---

## Biến môi trường Railway

```
OPENAI_API_KEY=

TELEGRAM_TOKEN=

ADMIN_ID=
```

---

## Chạy trên Railway

Railway sẽ tự động:

```
pip install -r requirements.txt
```

sau đó:

```
python -m app.main
```

---

## Commands

```
/start
/on
/off
/help
```

---

## Dictionary

File:

```
data/dictionary.json
```

Có thể bổ sung thuật ngữ riêng bất cứ lúc nào.

Ví dụ:

```json
{
    "Móng Cái": "芒街口岸",
    "Đông Hưng": "东兴口岸",
    "đóng container": "装柜",
    "hạt tiêu": "黑胡椒"
}
```

---

## OpenAI

Model mặc định:

```
gpt-4.1-mini
```

Có thể đổi sang model khác trong:

```
app/translator.py
```

---

## License

Private Project

Copyright © 2026
