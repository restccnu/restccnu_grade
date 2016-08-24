# RestCCNU-Grade

+ https://grade.muxixyz.com/api/ & https://ccnubox.muxixyz.com/api/
+ Grade-Search service for [restccnu](https://github.com/Muxi-Studio/restccnu)
+ RestCCNU-Grade 部署在两台服务器, 两台nginx下, 分摊IOS和安卓的流量
+ 对于CCNU服务器, 单独部署一个coroutx成绩搜索应用
+ 对于华北的服务器, 通过一个dispatchmiddleware 将 flask和 coroutx共同部署