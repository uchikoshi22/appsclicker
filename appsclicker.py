# -*- coding:utf-8 -*-

import os
import cgi
import re
import random
import string

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template


class Main(webapp.RequestHandler):
    def get(self):

        template_values = {
            }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

class GAEasStarterskit0(webapp.RequestHandler):
    def get(self):
        template_values = {
            }
        path = os.path.join(os.path.dirname(__file__), 'gae_as_starterskit_0.html')
        self.response.out.write(template.render(path, template_values))


class GeneratePassword(webapp.RequestHandler):
    def get(self):

        template_values = {
            }

        path = os.path.join(os.path.dirname(__file__), 'generate_password.html')
        self.response.out.write(template.render(path, template_values))
                                

    
    def post(self):
        elements = ''
        SYMBOL_LIST = ['#', '$', '%', '@', '?']
        
        if self.request.get('length'):
            length = cgi.escape(self.request.get('length'))
            if int(length) > 24:
                length = "4"
                
            if str(length).isdigit():
                pass
            else:
                length = 4
            
        lcase = cgi.escape(self.request.get('lcase'))
        ucase = cgi.escape(self.request.get('ucase'))
        digit = cgi.escape(self.request.get('digit'))
        symbol = cgi.escape(self.request.get('symbol'))

        if lcase == 'on':
            elements += string.lowercase
        if ucase == 'on':
            elements += string.uppercase
        if digit == 'on':
            elements += string.digits
        if symbol == 'on':
            elements = elements + "".join(SYMBOL_LIST)

        if not lcase and not ucase and not digit and not symbol:
            lcase = 'on'
            elements += string.lowercase

        password = generate_password(int(length), elements)

        template_values = {
            'counter' : range(4, 13),
            'length': int(length),
            'password' : password,
            'lcase' : lcase,
            'ucase' : ucase,
            'digit' : digit,
            'symbol' : symbol,
            }
        
        path = os.path.join(os.path.dirname(__file__), 'generate_password.html')
        self.response.out.write(template.render(path, template_values))


class KanaToRoman(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'kanaroma.html')
        self.response.out.write(template.render(path, ''))

    
    def post(self):
        kana = cgi.escape(self.request.get('kana'))
        roman = kanaroma(kana)
        
        template_values = {
            'kana' : kana,
            'roman' : roman,
            }

        path = os.path.join(os.path.dirname(__file__), 'kanaroma.html')
        self.response.out.write(template.render(path, template_values))


application = webapp.WSGIApplication(
                                     [('/', Main),
                                      ('/generate_password', GeneratePassword),
                                      ('/kanaroma', KanaToRoman),
                                      ('/gae_as_starterskit_0', GAEasStarterskit0),
                                     ],  
                                     debug=True)

def generate_password(length, elements):
    EXCLUSION_LIST = ['0', 'o', 'O', '1', 'l']

    password = ""

    while length:
        element = random.choice(elements)
        if element in EXCLUSION_LIST:
            continue
        else:
            password += element
        length -= 1

    return password


def kanaroma (kana):
    kana = kana.encode('utf-8')

    hepbum = {
        'あ' : 'a', 'い' :  'i', 'う' : 'u', 'え' : 'e', 'お' : 'o',
        'か' : 'ka', 'き' : 'ki', 'く' : 'ku', 'け' : 'ke', 'こ' : 'ko',
        'さ' : 'sa', 'し' : 'shi', 'す' : 'su', 'せ' : 'se', 'そ' : 'so',
        'た' : 'ta', 'ち' : 'chi', 'つ' : 'tsu', 'て' : 'te', 'と' : 'to',
        'な' : 'na', 'に' : 'ni', 'ぬ' : 'nu', 'ね' : 'ne', 'の' : 'no',
        'は' : 'ha', 'ひ' : 'hi', 'ふ' : 'fu', 'へ' : 'he', 'ほ' : 'ho',
        'ま' : 'ma', 'み' : 'mi', 'む' : 'mu', 'め' : 'me', 'も' : 'mo',
        'や' : 'ya', 'ゆ' : 'yu', 'よ' : 'yo',
        'ら' : 'ra', 'り' : 'ri', 'る' : 'ru', 'れ' : 're', 'ろ' : 'ro',
        'わ' : 'wa', 'ゐ' : 'i', 'ゑ' : 'e', 'を' : 'wo', 'ん' : 'n',

        'が' : 'ga', 'ぎ' : 'gi', 'ぐ' : 'gu', 'げ' : 'ge', 'ご' : 'go',
        'ざ' : 'za', 'じ' : 'ji', 'ず' : 'zu', 'ぜ' : 'ze', 'ぞ' : 'zo',
        'だ' : 'da', 'ぢ' : 'ji', 'づ' : 'zu', 'で' : 'de', 'ど' : 'do',
        'ば' : 'ba', 'び' : 'bi', 'ぶ' : 'bu', 'べ' : 'be', 'ぼ' : 'bo',
        'ぱ' : 'pa', 'ぴ' : 'pi', 'ぷ' : 'pu', 'ぺ' : 'pe', 'ぽ' : 'po',

        'きゃ' : 'kya', 'きゅ' : 'kyu', 'きょ' : 'kyo',
        'しゃ' : 'sha', 'しゅ' : 'shu', 'しょ' : 'sho',
        'ちゃ' : 'cha', 'ちゅ' : 'chu', 'ちょ' : 'cho',
        'にゃ' : 'nya', 'にゅ' : 'nyu', 'にょ' : 'nyo',
        'ひゃ' : 'hya', 'ひゅ' : 'hyu', 'ひょ' : 'hyo',
        'みゃ' : 'mya', 'みゅ' : 'myu', 'みょ' : 'myo',
        'りゃ' : 'rya', 'りゅ' : 'ryu', 'りょ' : 'ryo',

        'ぎゃ' : 'gya', 'ぎゅ' : 'gyu', 'ぎょ' :'gya',
        'じゃ' : 'ja', 'じゅ' : 'ju', 'じょ' : 'jo',
        'びゃ' : 'bya', 'びゅ' : 'byu', 'びょ' : 'byo',
        'ぴゃ' : 'pya', 'ぴゅ' : 'pyu', 'ぴょ' : 'pyo',

        'ア' : 'a', 'イ' :  'i', 'ウ' : 'u', 'エ' : 'e', 'オ' : 'o',
        'カ' : 'ka', 'キ' : 'ki', 'ク' : 'ku', 'ケ' : 'ke', 'コ' : 'ko',
        'サ' : 'sa', 'シ' : 'shi', 'ス' : 'su', 'セ' : 'se', 'ソ' : 'so',
        'タ' : 'ta', 'チ' : 'chi', 'ツ' : 'tsu', 'テ' : 'te', 'ト' : 'to',
        'ナ' : 'na', 'ニ' : 'ni', 'ヌ' : 'nu', 'ネ' : 'ne', 'ノ' : 'no',
        'ハ' : 'ha', 'ヒ' : 'hi', 'フ' : 'fu', 'ヘ' : 'he', 'ホ' : 'ho',
        'マ' : 'ma', 'ミ' : 'mi', 'ム' : 'mu', 'メ' : 'me', 'モ' : 'mo',
        'ヤ' : 'ya', 'ユ' : 'yu', 'ヨ' : 'yo',
        'ラ' : 'ra', 'リ' : 'ri', 'ル' : 'ru', 'レ' : 're', 'ロ' : 'ro',
        'ワ' : 'wa', 'ヲ' : 'wo', 'ン' : 'n',

        'ガ' : 'ga', 'ギ' : 'gi', 'グ' : 'gu', 'ゲ' : 'ge', 'ゴ' : 'go',
        'ザ' : 'za', 'ジ' : 'ji', 'ズ' : 'zu', 'ゼ' : 'ze', 'ゾ' : 'zo',
        'ダ' : 'da', 'ヂ' : 'ji', 'ヅ' : 'zu', 'デ' : 'de', 'ド' : 'do',
        'バ' : 'ba', 'ビ' : 'bi', 'ブ' : 'bu', 'ベ' : 'be', 'ボ' : 'bo',
        'パ' : 'pa', 'ピ' : 'pi', 'プ' : 'pu', 'ペ' : 'pe', 'ポ' : 'po',
        'ヴ' : 'vu',

        'キャ' : 'kya', 'キュ' : 'kyu', 'キョ' : 'kyo',
        'シャ' : 'sha', 'シュ' : 'shu', 'ショ' : 'sho',
        'チャ' : 'cha', 'チュ' : 'chu', 'チョ' : 'cho',
        'ニャ' : 'nya', 'ニュ' : 'nyu', 'ニョ' : 'nyo',
        'ヒャ' : 'hya', 'ヒュ' : 'hyu', 'ヒョ' : 'hyo',
        'ミャ' : 'mya', 'ミュ' : 'myu', 'ミョ' : 'myo',
        'リャ' : 'rya', 'リュ' : 'ryu', 'リョ' : 'ryo',

        'ギャ' : 'gya', 'ギュ' : 'gyu', 'ギョ' :'gya',
        'ジャ' : 'ja', 'ジュ' : 'ju', 'ジョ' : 'jo',
        'ビャ' : 'bya', 'ビュ' : 'byu', 'ビョ' : 'byo',
        'ピャ' : 'pya', 'ピュ' : 'pyu', 'ピョ' : 'pyo'
                }

    hepbum_keys = hepbum.keys()
    hepbum_keys.sort(key=lambda x: len(x), reverse=True)
    re_kanaroma = re.compile("|".join(map(re.escape, hepbum_keys)))
    re_xtu = re.compile("っ(.)")
    re_xtu_katakana = re.compile("ッ(.)")
    re_ltu = re.compile("っ$")
    re_n = re.compile(r"n(b|p)([aiueo])")
    re_oo = re.compile(r"([aiueo])\1")
    roman = re_kanaroma.sub(lambda x: hepbum[x.group(0)], kana)
    roman = re_xtu.sub(r"\1\1", roman)
    roman = re_xtu_katakana.sub(r"\1\1", roman)
    roman = re_ltu.sub(r"", roman)
    roman = re_n.sub(r"m\1\2", roman)
    roman = re_oo.sub(r"\1", roman)

    return roman


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
