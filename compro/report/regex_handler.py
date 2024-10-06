import re

def get_sub_address(text):

    try:
        region = text[:re.search('обл', text).start()] + 'область'
    except:
        region = ''

    if re.search('село', text):
        sub_sext = text[re.search('село', text).end():]
        city = 'село ' + re.search(r'[\w]+', sub_sext).group()

    elif re.search("с.\ ", text):
        sub_sext = text[re.search('с.\ ', text).end():]
        city = 'село ' + re.search(r'[\w]+', sub_sext).group()

    elif re.search('місто', text):
        sub_sext = text[re.search('місто', text).end():]
        city = 'місто ' + re.search(r'[\w]+', sub_sext).group()

    elif re.search('м.\ ', text):
        sub_sext = text[re.search('м.\ ', text).end():]
        city = 'місто ' + re.search(r'[\w]+', sub_sext).group()

    else:
        city = ''

    if region != '':
        sub_address = city + ', ' + region
    else:
        sub_address = city

    return sub_address


