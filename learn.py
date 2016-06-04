import image
import csstool
import json
import requests

def get_page(url='http://code.bankrate.com.cn/getProductData/financing_gRrgLT98?pos=detail'):
    respon = requests.get(url,headers={'Referer': 'http://www.yinhang.com/licaichanpin_gRrgLT98.html',})
    return json.loads(respon.content.replace(",'js')",'').replace("setAjaxData(",''))['cssfile']

def get_image_url(cssfile):
    url_base = 'http://b1r.cn/d2/%s.png'
    return url_base % cssfile.replace('.','/').split('/')[-2]