FROM python:3.7.4
Maintainer sudhanshumathur01@gmail.com
Copy . /opt/assignment/
WORKDIR /opt/assignment
RUN pip3 install -r requirement.txt