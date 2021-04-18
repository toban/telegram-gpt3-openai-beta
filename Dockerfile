FROM python

ARG CHAT_ID
ENV CHAT_ID ${CHAT_ID}

ARG BOT_NAME
ENV BOT_NAME ${BOT_NAME}

ARG BOT_TOKEN
ENV BOT_TOKEN ${BOT_TOKEN}

ARG VOICE_PITCH
ENV VOICE_PITCH ${VOICE_PITCH}

ARG API_KEY
ENV API_KEY ${API_KEY}

RUN mkdir /app
ADD src /app

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
RUN mv config.py.docker.template config.py

RUN python main.py