import pyttsx3

# 음성 엔진 초기화
engine = pyttsx3.init()

# 사용 가능한 목소리 출력
voices = engine.getProperty('voices')
for voice in voices:
    print(f"Voice: {voice.id}, Language: {voice.languages}, Gender: {voice.gender}")

# 'EN-US'를 포함하는 목소리 선택 (Zira 또는 David)
american_voices = [voice for voice in voices if 'EN-US' in voice.id]
if american_voices:
    engine.setProperty('voice', american_voices[0].id)
    print("Selected American English voice:", american_voices[0].id)
else:
    print("No American English voice found.")

# 음성으로 변환할 텍스트 설정
text = "Hello, world!"

# 텍스트 음성 변환
engine.say(text)

# 변환된 음성 재생
engine.runAndWait()

# 엔진 종료
engine.stop()

