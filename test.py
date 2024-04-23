import time
import requests

# replace your vercel domain
base_url = 'http://localhost:3000'


def custom_generate_audio(payload):
    url = f"{base_url}/api/custom_generate"
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    return response.json()


def generate_audio_by_prompt(payload):
    url = f"{base_url}/api/generate"
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    return response.json()

def generate_audio_by_prompt_lyrics():
    payload = {
        "prompt": """
            Куплет 1:
            Во мгле прошлого темного, глубоко запрятано,
            Тайна скрытая, болью в сердце упрятана.
            Тяжелый груз таился в одинокой душе,
            Своими мыслями погибал я в темноте.

            Куплет 2:
            Голова моя, она была моим врагом,
            Проблемы в ней угрожали мне с каждым днем.
            А лезвие в руке не давало покоя изрезанной руке.
            Оно оставило шрамы в мёртвой душе.

            Бридж:
            Суицидальные мысли, как снежный покров.
            Окутали меня, открыв мне новый проход.

            Припев:
            В сердце моём огонь, надежду не терял,
            Любовь и силу в глубине души он сохранял.
            Однажды смог я расправить крылья свои,
            Подняться выше, оставив темноту позади.

            Аутро:
            Шрамы на руке стали свидетелями безответной любви,
            Напоминая мне, о сильной борьбе моего сердца и голоса в голове.
        """,
        "tags": "sad rap",
        "title": "test",
        "make_instrumental": False,
        "wait_audio": False
        }
    
    url = f"{base_url}/api/custom_generate"
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    return response.json()

#__stripe_mid=ae96d275-3cac-4cfb-8aad-a76e8e7ad0536a6ba8; _cfuvid=YbE4jnOGZwxdvKOOU4icxBd.6NDoA4gwIHLtsxOwKnU-1713715981592-0.0.1.1-604800000; __cf_bm=iei2xhFUEXhIs89XnTU1wV_UcwKKCmyIh2UM9hvZYyg-1713757184-1.0.1.1-JQISyui9qOiToRqEZUReq7Npx9yA7owvmeicw2M6LspLUkMDkkWFeERNl8jgGnrkYtRgRLSdv8zZ2LBhYM6xPA; __cf_bm=LL1zc94ARfFzSgWDQY0ANfC.i_YGZRjkPYi0lceuQgY-1713757504-1.0.1.1-pLdcnM9DzwDGEPUVBHYeEcauuZUoQ8WWVByZIZ0qKpwAQtXo.8IKoBrCWkUGNqmIvdvJ6TMdqn.64yuox3Anmg; __client=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImNsaWVudF8yZlJKQmd2VTZvZVFzYUVPOU4wQWlMYm9waDgiLCJyb3RhdGluZ190b2tlbiI6IjkyYXpoaHVqZnN0OGR2d2ttNnNvcHRzNHByczhvZTFueGhyOTY0emoifQ.jlLFnmTOivKvHCgJCc2JpbAFXaYtkUg9qxcrh4SZfEDpG1EleORomMQmYrVq9uPBPOqZJq41BHe41tGdJ59ja6w-AUTmGz-LnJu_SnxzoRDlPwb2mZ2Tcn-Y-c_a8FtnfvyExLUvri-S7XXLoZo7FLTafoBZcu9QSYEtlmX2ftRw2gKFVlC9LFceQml589crVXNqNP-fdalaW-YNQvtz7qNgcHRvfxJ-cZoiYc8rbb1Q8gjMcISeK6xXfMKzX24GjCLmAozOe-eaQmzdY6iZHkSeUHp5fnJgu5n7C2BZA7YLhuLFGJWPzKhJRmL0qfhczYvediEVO9zMdWt7r3598A; __client_uat=1713757842; mp_26ced217328f4737497bd6ba6641ca1c_mixpanel=%7B%22distinct_id%22%3A%20%228c882a99-7675-4476-b5a8-61cfb3c6901d%22%2C%22%24device_id%22%3A%20%2218efc77eddcd3a-0b5a31ec927ebe-26001d51-144000-18efc77eddcd3a%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fgithub.com%2Fgcui-art%2Fsuno-api%3Ftab%3Dreadme-ov-file%22%2C%22%24initial_referring_domain%22%3A%20%22github.com%22%2C%22%24user_id%22%3A%20%228c882a99-7675-4476-b5a8-61cfb3c6901d%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D
#__cf_bm=uZtJh7fiPXtx.1fo0uKanRImd4Bn5B8KerzDFdXmWKY-1713758443-1.0.1.1-HKnmNhJnUD9zXmxlX6Lh0QdFsLw11jXxCyyVvJpvxuJWtaOsb6.IkHrJipxpdhuwpvScCrAW4lm7exrJSoQ5og; _cfuvid=DmIX_ZTw_s60jUh3xDUXp9kXAfYvZnJ.I90u0XbC0YU-1713758444952-0.0.1.1-604800000;
# __client=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImNsaWVudF8yZlJLVVc4ektjc2QyNDFKc1k3U0w5SlBzcTMiLCJyb3RhdGluZ190b2tlbiI6ImM1dXUyeDFrdHNlMDhkMm0yc3Y0aGx0OXdqcDNpZ2RvMWN3bmozdHgifQ.g06jbb4NyH8oY8WpqecivUEztIo-Mw55NttAhJEP2mGi1HYD0U021d2YPVHoYsB9WuLzVEeUEFmE3PRkJrDW23FqQlQxHHsNvIfW5xB1zxgZoV3dpbOn0iRSgmkhCZNOw4LReTy-RZVGLngVobT3Gs6E6TiMYzh6T3cts_GCp0Zc6uO6k5L9z4YsLC7o9g6Yq_egtv71en3LSzUHC4p02t5ERo7ttFiak3YxnNejDTWwLNFI0Hlk5NLvS1X3IewWfx90mVu2FZssB3oVWJumMkpUF_-grrsz1KZuZeQhfD96rJzgJ5WGLUfUxn66mWJ-VxmibDK6kjXlOWi4cXuvqA;
# __client_uat=1713758490;
# mp_26ced217328f4737497bd6ba6641ca1c_mixpanel=%7B%22distinct_id%22%3A%20%22d3753762-9382-4a8e-9ef6-e016a7eca2d4%22%2C%22%24device_id%22%3A%20%2218f03f696903ed9-02d73c84848bcb-26001d51-144000-18f03f696903ed9%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%22d3753762-9382-4a8e-9ef6-e016a7eca2d4%22%7D; 
# __cf_bm=3Bo5DVyL.OuT9QYqnsneEqGFp7vfbcxohBT_v5aXat4-1713758516-1.0.1.1-OyloCtNYf22dnd86URmBJm1t8h7cADO34z0aOu6Q43TYi_mUKD37SKC473RQryLgPKYMR8YkLabNteKol1InGA

def get_audio_information(audio_ids):
    url = f"{base_url}/api/get?ids={audio_ids}"
    response = requests.get(url)
    return response.json()


def get_quota_information():
    url = f"{base_url}/api/get_limit"
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
    # data = generate_audio_by_prompt_lyrics({
    #     "prompt": "A popular heavy metal song about war, sung by a deep-voiced male singer, slowly and melodiously. The lyrics depict the sorrow of people after the war.",
    #     "make_instrumental": False,
    #     "wait_audio": False
    # })
    
    data = generate_audio_by_prompt_lyrics()

    ids = f"{data[0]['id']},{data[1]['id']}"
    print(f"ids: {ids}")

    for _ in range(60):
        data = get_audio_information(ids)
        if data[0]["status"] == 'streaming':
            print(f"{data[0]['id']} ==> {data[0]['audio_url']}")
            print(f"{data[1]['id']} ==> {data[1]['audio_url']}")
            break
        # sleep 5s
        time.sleep(5)