#base
FROM python:3-onbuild

#expose port 5000
EXPOSE 5000

RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list

RUN apt-get update && apt-get install vim -y

RUN ["apt-get", "install", "-y", "vim"]
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
#run app
CMD ["./server.py"]
