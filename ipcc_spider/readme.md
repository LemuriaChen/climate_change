<div align="left">
    <img src='https://github.com/HUANGZHIHAO1994/climate_change/blob/master/wos_spider/images/IMG_1869.jpg?raw=true' height="50" width="50" >
 </div>

## 说明：

1. 这个项目小就先不用scrapy了，用selenium会拖慢点速度（影响不大忽视）
2. 文件夹名称编号：如12代表ar1wg2
3. 所有的full_report一共15个都没下载，太大了，所以爬下来空目录是只有一个full_report的
4. 下载时默认//div[@class='section-content']//a 下的href全部下载，因此多国语言文件全下载下来了
5. pdf命名方式：如：href="https://www.ipcc.ch/site/assets/uploads/2018/07/WGIIAR5-Chap24_OLSM.pdf"，取最后'/'之后的文字
    因此，有些链接没有.pdf后缀名点击下一页，复制链接，将链接中page=2修改为page=1
