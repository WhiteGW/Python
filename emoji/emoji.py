import requests
import parsel
import os


def open_url():
    page = int(input("请输入要下载的页数然后回车即可："))
    url = "https://www.fabiaoqing.com/biaoqing/lists/page/"+str(page)+".html"
    response = requests.get(url)
    html = response.text
    sel = parsel.Selector(html)
    divs = sel.css('.tagbqppdiv')
    urls = []
    for div in divs:
        img_url = div.css('img.ui::attr(data-original)').getall()
        img_title = div.css('img.ui::attr(title)').getall()
        urls.append((img_url,img_title))        
    return urls


def save_img(folder):
    urls =open_url()
    for url in urls:
        try:
            rep = requests.get(url[0][0])
            suffix = url[0][0].split('.')[-1]
            with open(url[1][0]+'.'+suffix,mode='wb') as f:
                f.write(rep.content)
                print("正在下载："+str(url[1][0]))
        except OSError:
            print("保存的文件名不规范，将跳过此文件")
    print("恭喜你！现在完成！")            

def download_emoji(folder="emoji"):
    print("本程序会自动采集表情网【fabiaoqing.com】的热门分类表情包")
    print("表情包会保存到和本程序同一目录下的emoji文件夹里面")
    print("打开链接地址：https://www.fabiaoqing.com/biaoqing查看要下载页面的页码")
    if os.path.exists('emoji'):
        pass
    else:
        os.mkdir(folder)
    os.chdir(folder)
    save_img(folder)

if __name__ == "__main__":
    download_emoji()
