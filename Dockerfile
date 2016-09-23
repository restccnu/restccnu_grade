FROM python:2.7
ADD . /restccnu_grade
WORKDIR /restccnu_grade

RUN pip install --index-url http://pypi.doubanio.com/simple/ -r requirements.txt --trusted-host=pypi.doubanio.com
# RUN pip install -r requirements.txt
