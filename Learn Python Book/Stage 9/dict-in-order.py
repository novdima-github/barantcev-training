from collections import OrderedDict

lang = OrderedDict()
lang[5] = 'One'
lang[4] = 'Two'
lang[3] = 'Tree'
lang[4] = 'Four'
lang[5] = 'Five'
for k, v in lang.items():
    print(str(k) + ' ' + v)


lang = {}
lang['aaq'] = 'Onew'
lang['aaw'] = 'Twow'
lang['aae'] = 'Tree'
lang['aar'] = 'Four'
lang['aat'] = 'Fiveqw'
for k, v in lang.items():
    print(str(k) + ' ' + v)
