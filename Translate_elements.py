# This Python file uses the following encoding: utf-8


from yandex.Translater import Translater


def translate():
    tr = Translater()
    tr.set_key('trnsl.1.1.20181128T091344Z.1764de5129a6aa08.f7b484a88cbe7ec9a2f4d295a1c310ba5867d9cc') # Api key found on https://translate.yandex.com/developers/keys
    text_to_translate = 'شركة ذات مسؤولية محدودة'
    tr.set_text(text_to_translate)
    tr.set_from_lang('ar')
    tr.set_to_lang('en')
    translated_txt = tr.translate()
    print(translated_txt)


translate()
