import wave
import pyaudio
import os

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 3
WAVE_OUTPUTFILENAME = "record.wav"

def Record_wav():
    p = pyaudio.PyAudio()
    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = CHUNK)

    print("Recording...")

    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Done!")

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUTFILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))

    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()




from aip import AipSpeech

import os

APP_ID = '22571839'
API_KEY = 'RKyGPvSDrIBRa0k4Tvb8t7iR'
SECRET_KEY = 'SQHO9eQxBC7YMhE7kgAsRM7HZ5B6RbfC'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def Speech_Rec(filename):
    print("开始识别。。。")
    result = client.asr(get_file_content(filename),
                    'wav',
                    16000,
                    {'dev_pid':1537,}
                    )
    #print(result)
    
    if result['err_msg'] == 'success.':
        #print("result:" + result['result'][0])
        print("识别成功。。。")
        return result['result'][0]
    else:
        #print("error_message:"+ result['err_msg'])
        #print("error_NO.:"+ result['err_no'])
        print("识别失败。。。")
        return 0

#Record_wav()
#result = Speech_Rec('./record.wav')
#print(result)

#if result == "第一首。":
#    os.system("sudo ~/rpitx/pifmrds -freq 98.5 -audio ../Musics/0.wav")
#elif result == "第二首。":
#    os.system("sudo ~/rpitx/pifmrds -freq 98.5 -audio ../Musics/1.wav")
#elif result == "第三首。":
#    os.system("sudo ~/rpitx/pifmrds -freq 98.5 -audio ../Musics/2.wav")
#elif result == "第四首。":
#    os.system("sudo ~/rpitx/pifmrds -freq 98.5 -audio ../Musics/3.wav")
#else:
#    os.system("sudo ~/rpitx/pifmrds -freq 98.5 -audio ./record.wav")