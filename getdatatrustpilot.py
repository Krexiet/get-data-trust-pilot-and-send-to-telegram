import requests

def get_trustpilot_data(website_url, api_key):
    trustpilot_url = f"https://api.trustpilot.com/v1/business-units/find?websiteUrl={website_url}"
    headers = {"apikey": api_key}
    try:
        response = requests.get(trustpilot_url, headers=headers)
        response.raise_for_status()  # Проверяем успешность запроса
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к Trustpilot API: {e}")
        return None
    except ValueError as ve:
        print(f"Ошибка при разборе JSON: {ve}")
        return None

def send_telegram_message(bot_token, chat_id, message):
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    try:
        response = requests.post(telegram_url, json=params)
        response.raise_for_status()  # Проверяем успешность запроса
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке сообщения в Telegram: {e}")
        return None
    except ValueError as ve:
        print(f"Ошибка при разборе JSON: {ve}")
        return None

def main():
    # Данные для доступа к Telegram API
    telegram_bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
    telegram_chat_id = "YOUR_TELEGRAM_CHAT_ID"
    
    # Ключ API Trustpilot
    trustpilot_api_key = "YOUR_TRUSTPILOT_API_KEY"
    
    # URL вашего веб-сайта для получения данных с Trustpilot
    website_url = "YOUR_WEBSITE_URL"
    
    # Получаем данные с Trustpilot
    trustpilot_data = get_trustpilot_data(website_url, trustpilot_api_key)
    
    # Обработка данных
    if trustpilot_data and "id" in trustpilot_data:
        reviews = trustpilot_data["numberOfReviews"]
        stars = trustpilot_data["stars"]
        message = f"Ваш сайт имеет {reviews} отзывов со средней оценкой {stars} звезд."
    else:
        message = "Не удалось получить данные о вашем сайте с Trustpilot."
    
    # Отправляем сообщение в Telegram
    send_telegram_message(telegram_bot_token, telegram_chat_id, message)

if __name__ == "__main__":
    main()
