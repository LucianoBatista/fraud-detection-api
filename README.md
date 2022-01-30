# FRAUD-DETECTION-API

This repository contains the API that will serve the Fraud Detection Model, developed during the Third Challenge of the Tera's Bootcamp. If you want to learn more about the development of the model, please access the following repo:

- https://github.com/LucianoBatista/fraud-detection-classifier

## Installation

In order to run this API locally is important to you to have docker and docker-compose installed on you machine. If you don't have, please check the [link](https://docs.docker.com/engine/install/ubuntu/) and [that](https://docs.docker.com/compose/install/).

After that:

1. `mkdir fraud-detect-api`
2. `cd fraud-detect-api`
3. `docker-compose up --build -d`

If everything works well, you'll probably have access to the service on the 5005 port. To check that, access http://localhost:5005/docs.

For a detailed explanation about the routes, check:

- https://lucianobatista.github.io/fraud-detection-classifier/api/



