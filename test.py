import requests
import json
import os


url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

file_path = 'C:/Jeonbar2/git_workspace/Capstone_Test/secret.json'
with open(file_path) as f:
    json_key = json.load(f)
rest_api_key = json_key['rest_api_key']

headers = {
    "Content-Type": "application/octet-stream",
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " + rest_api_key,
}
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone(sample_rate=16000) as source:
    print("say something!")
    audio=r.listen(source)
    audio.get_raw_data()
res=requests.post(url, headers=headers , data=audio.get_raw_data())

result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1]
result = json.loads(result_json_string)

print(result)
print(result['value'])