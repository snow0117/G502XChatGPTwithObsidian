import pyttsx3

def list_voices():
    # TTS 엔진 초기화
    engine = pyttsx3.init()
    # 사용 가능한 목소리 목록 출력
    voices = engine.getProperty('voices')
    for index, voice in enumerate(voices):
        print(f"Voice {index}: {voice.name} - {voice.languages}")

def text_to_speech(word, voice_index):
    # TTS 엔진 초기화
    engine = pyttsx3.init()
    # 선택한 목소리 설정
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_index].id)
    # 텍스트를 음성으로 변환
    engine.say(word)
    # 음성 출력
    engine.runAndWait()

# 사용 가능한 목소리 목록 출력
list_voices()

# 테스트용 단어와 목소리 인덱스
word = "cheese"
# 사용 가능한 목소리 목록을 보고 영어 발음을 지원하는 목소리 인덱스로 변경
voice_index = int(input("Enter the voice index for English pronunciation: "))
text_to_speech(word, voice_index)
