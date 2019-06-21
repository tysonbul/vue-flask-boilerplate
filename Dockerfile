FROM node:10.16.0 AS build
ARG ENV="staging"
ENV NODE_ENV="${ENV}"

WORKDIR /build

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM python:3.6 AS run
ARG ENV="staging"
ENV NODE_ENV="${ENV}"
ENV PYTHONPATH "${PYTHONPATH}:/app"

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY docker-run.sh .
RUN chmod a+x docker-run.sh

COPY --from=build /build/dist dist
COPY server server
COPY app.py .
COPY config.py .

EXPOSE 5000

ENTRYPOINT ["bash", "docker-run.sh"]
