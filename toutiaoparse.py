# -*- coding:utf-8 -*-
import urllib
import urllib2
url = 'http://123.56.88.126/video/toutiao'
#values = {'iid':'11449388001','app':'news_article','tt_from':'copy_link','utm_source':'copy_link','utm_medium':'toutiao_ios','utm_campaign':'client_share'}
values = {'link':'https://www.365yg.com/group/6434712093349380610/?iid=11449388001&app=news_article&tt_from=copy_link&utm_source=copy_link&utm_medium=toutiao_ios&utm_campaign=client_share'}
data = urllib.urlencode(values)
header_data = {
'Accept':'application/json, text/javascript, */*; q=0.01',
'Origin':'http://toutiao.iiilab.com',
}
req = urllib2.Request(url, data,header_data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
