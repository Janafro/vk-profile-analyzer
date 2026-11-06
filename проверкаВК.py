import vk_api

ACCESS_TOKEN = "Сюда вводить токен"

def analyze_vk_profile(user_id):
    try:
        vk_session = vk_api.VkApi(token=ACCESS_TOKEN)
        vk = vk_session.get_api()
        
        print(f"Запрос данных для пользователя: {user_id}")

        user_info = vk.users.get(
            user_ids=user_id, 
            fields=['about', 'activities', 'bdate', 'city', 'common_count', 'followers_count', 'occupation', 'relation', 'site', 'last_seen']
        )
        
        if not user_info:
            print("Пользователь не найден или страница удалена/закрыта.")
            return

        info = user_info[0]
        print("\n--- Результаты анализа профиля ---")
        print(f"Имя и Фамилия: {info.get('first_name')} {info.get('last_name')}")
        print(f"ID: {info.get('id')}")
        print(f"Город: {info.get('city', {}).get('title', 'Не указан')}")
        print(f"День рождения: {info.get('bdate', 'Скрыта')}")
        print(f"Подписчиков: {info.get('followers_count', 'Нет данных')}")
        last_seen = info.get('last_seen', {})
        if last_seen:
            import datetime
            time_human = datetime.datetime.fromtimestamp(last_seen.get('time', 0)).strftime('%Y-%m-%d %H:%M:%S')
            print(f"Последний визит: {time_human}")
        
        if info.get('about'):
            print(f"О себе: {info.get('about')}")
            
    except Exception as e:
        print(f"[-] Ошибка при запросе к VK API: {e}")

if __name__ == "__main__":
    target = input("Введите ID или короткое имя пользователя VK (например, durov): ").strip()
    if target:
        analyze_vk_profile(target)