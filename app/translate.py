import json
import requests
from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {
        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY']}
    r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
                     '/Translate?text={}&from={}&to={}'.format(
                         text, source_language, dest_language),
                     headers=auth)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))

def translateByYoudao(text):
    r = requests.get('http://fanyi.youdao.com/translate?&doctype=json'
                     '&type=AUTO&i={}'.format(text))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    try:
        dict1 = json.loads(r.content.decode('utf-8-sig'))
        list1 = dict1['translateResult']
        list2 = list1[0]
        dict2 = list2[0]
    except Exception:
        return _('Error: the translation data parsing exception.')
    else:
        print('translateByYoudao dict1:', dict1)
        return dict2['tgt']