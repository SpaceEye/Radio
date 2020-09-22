import web
import json
from functions import recognize
from functions import play_rpitx

urls = ('/','index',
        '/(js|css|images|fonts)/(.+)', 'static',
        '/func/(.*)','function',
        '/(.*)', 'other')
app = web.application(urls, globals())

playing_music = 0

class index:        
    def GET(self):
        with open('html/index.html', 'rb') as f:
            html = f.read()
        return html

    def POST(self):
        return

class static:
    def GET(self, file_type, file_path):
        try:
            with open('html/' + file_type + '/' + file_path, 'rb') as f:
                text = f.read()
        except FileNotFoundError:
            return web.notfound()
        return text

class function:
    def POST(self, func_name):
        data = web.data()
        print(data)
        if func_name == "music_ctl":
            recognize.Record_wav()
            result = recognize.Speech_Rec('./record.wav')
            print(result)
        global playing_music
        if result == "第一首。":
            playing_music = 0
        elif result == "第二首。":
            playing_music = 1
        elif result == "第三首。":
            playing_music = 2
        elif result == "第四首。":
            playing_music = 3
        elif result == "第五首。":
            playing_music = 4
        elif result == "第六首。":
            playing_music = 5
        elif result == "第七首。":
            playing_music = 6
        elif result == "第八首。":
            playing_music = 7
        elif result == "上一首。":
            playing_music = playing_music - 1
        elif result == "下一首。":
            playing_music = playing_music + 1
        else:
            pass

        playing_music = playing_music % 8

        respone = json.dumps({"music_num":playing_music})
        return respone

class other:
    def GET(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                text = f.read()
            if file_path.split(".")[1] == "wav":
                play_rpitx.play_music(file_path)
        except FileNotFoundError:
            return web.notfound()
        return text


if __name__ == "__main__":
    app.run()