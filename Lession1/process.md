###  12306抢票软件的开发
* 爬虫思维
* 爬虫代码实现

一  爬虫进行页面的分析流程  
1 进行网页源代码查看是否有自己想要的数据  
2 通过抓包。许多网站是通过异步加载的方式来进行数据的请求 ajax 异步加载，在页面是无法找到数据的。所以通过抓包解决。  

二 第一步  
*1 证书验证失败报错，证书是为了让数据再传输过程中不被更改的 是因为12306的证书是没有被机构认证的
> urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:777) 
  
解决办法就是不让python去验证 
导入SSL 模块，设置一个特定的值就可以了 ，进行关闭证书的验证  
> ssl._create_default_https_context = ssl._create_unverified_context();  
