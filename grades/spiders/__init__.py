# coding: utf-8
# URL Map :)

"""模拟登录"""
info_login_url = "http://portal.ccnu.edu.cn/loginAction.do"
info_login_test_url = "http://portal.ccnu.edu.cn/chpass.jsp"
lib_login_url = "http://202.114.34.15/reader/redr_verify.php"
lib_login_test_url = "http://202.114.34.15/reader/redr_info.php"
link_index_url = "http://portal.ccnu.edu.cn/roamingAction.do?appId=XK"
headers = {
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    'Accept-Encoding':"gzip, deflate",
}


"""成绩查询"""
grade_index_url = "http://122.204.187.6/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdmKey=N305005&sessionUserKey=%s"
grade_detail_url = "http://122.204.187.6/cjcx/cjcx_cxCjxq.html?time=1468243324589&gnmkdmKey=N305005&sessionUserKey=%s"