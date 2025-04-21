import requests

def get_ai_reply(question):
    url = "https://yw85opafq6.execute-api.us-esat-1.amazonaws.com/default/boss_mode_15aug"
    
    payload = {
        "text": question.content,
        "country": "Asia",  # اگر بخوای کشور رو داینامیک کنی هم میشه
        "user_id": "usery3peupi26p"  # اگه خاص برای AI جواب‌دهی هست
    }

    try:
        response = requests.get(url, params=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("reply", "پاسخی از سمت AI دریافت نشد.")
    except requests.RequestException as e:
        print(f"AI API error: {e}")
        return "در حال حاضر امکان دریافت پاسخ از AI وجود ندارد."

