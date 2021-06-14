FROM python:3.7
RUN apt update -y && apt install -y wget apt-transport-https
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
RUN echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-7.x.list
RUN apt-get update -y && apt-get install logstash postgresql-client -y
RUN pip install pgsync fake2db psycopg2
ADD ./postgresql-42.2.20.jar /usr/share/logstash/logstash-core/lib/jars
RUN ln -s  /usr/share/logstash/bin/logstash /usr/bin/logstash
WORKDIR /workspace
ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]