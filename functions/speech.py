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
    result = client.asr(get_file_content(filename),
                    'wav',
                    16000,
                    {'dev_pid':1537,}
                    )
    #print(result)

    if result['err_msg'] == 'success.':
        #print("result:" + result['result'][0])
        return result['result'][0]
    else:
        #print("error_message:"+ result['err_msg'])
        #print("error_NO.:"+ result['err_no'])
        return 0
            


if __name__ == '__main__':
    print(Speech_Rec('./Sounds/321.wav'))

