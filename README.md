# 淘宝拍照找同款数据爬虫
本工具用于模拟网页访问淘宝以图搜图/拍照找同款功能，可以找出与给定服装视觉上类似的商品。本工具最初被用在[京东商品图片分类比赛](http://www.wid.org.cn/data/science/player/competition.html?data=232)中，采用selenium+Chrome作为浏览器引擎，批量上传图片至淘宝，并将找出的同款的描述写入本文本件。用户可以在同款商品描述的基础上做自然语言处理。同款的描述是在淘宝返回页面上采用正则匹配而来，用户可以方便地在此基础上按自己的需要进行开发，例如拿到所有同款商品的图片和价格等。

## 平台和依赖
* [selenium](http://www.seleniumhq.org/)
* [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* [pip](https://pypi.python.org/pypi/pip)
* Ubuntu 15.04/14.10/14.04/12.04

pip安装方法：

    sudo apt-get install python-pip
    

selenium安装方法：

    sudo pip install selenium
    
Chrome Driver安装方法：

1. 到[Chrome Driver官网](https://sites.google.com/a/chromium.org/chromedriver/downloads)下载合适的版本并将其中的chromedriver解压到自己喜欢的地方
2. 将chromedriver所在的目录加到环境变量```PATH```中，如果你在使用```bash```，可以用如下命令：



        echo 'export PATH=$PATH:/path/to/your/chromedriver' >> ~/.bashrc
        source ~/.bashrc 
        
## 爬淘宝数据
1. 将需要上传至淘宝的图片的路径写入文本文件，一行一张图，相对路径绝对路径均可，格式为

        image/1.jpg
        image/2.jpg
        image/3.jpg
        ...
格式可参考[image_list.txt](image_list.txt)
2. 在命令行中执行
    
        python get_tb_description.py image_list.txt result.txt
        
后，即可将```image_list.txt```中所有图片的同款的描述写入```result.txt```中，格式为

        image/1.jpg: 描述描述描述描述描述描述描述描述描述描述描述描述
        image/2.jpg: 描述描述描述描述描述描述描述描述描述描述描述描述
        image/3.jpg: 描述描述描述描述描述描述描述描述描述描述描述描述