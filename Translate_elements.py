# This Python file uses the following encoding: utf-8


from yandex.Translater import Translater


def translate():
    tr = Translater()
    tr.set_key('Insert_your_API_Key_Here') # Api key found on https://translate.yandex.com/developers/keys
    text_to_translate = 'شركة ذات مسؤولية محدودة'
    tr.set_text(text_to_translate)
    tr.set_from_lang('ar')
    tr.set_to_lang('en')
    translated_txt = tr.translate()
    print(translated_txt)


translate()
