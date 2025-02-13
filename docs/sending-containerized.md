# Containerizing 'Sending'

This document explains how to containerize and deploy the ['sending.py' application](https://github.com/meganbloemsma/send-message/blob/main/src/send-message.py) using Docker and Azure AI services.

## Prerequisites

Ensure you have the following installed:  

* [Docker](https://docs.docker.com/get-docker/)
* This guide uses [Docker Desktop](https://docs.docker.com/get-started/introduction/get-docker-desktop/)
* Azure Speech resource. Create an .env file in the 'sending' folder for `SPEECH_API_KEY`, `SPEECH_BILLING_URL` and `SPEECH_REGION`

## Configure the environment variables

Create an `.env` file in the `src\sending` folder with the following content:

```
SPEECH_API_KEY={SPEECH_API_KEY}
SPEECH_BILLING_URL={SPEECH_BILLING_URL}
SPEECH_REGION={SPEECH_REGION}
```

## Build and start the containers

Run the following command in the root directory to build and start the containers:

```
docker-compose up --build
```

## Verify the containers are running

You can check the logs for each container:

```
docker-compose logs sending
```

We are expecting two containers to run: `speech-to-text` and `language-detection`.

## Troubleshooting

If you encounter issues, follow these steps:

1. Shut down the containers
To stop the containers, run:

```
docker-compose down
```

2. Make changes and restart
After debugging and making the necessary changes to the code, restart the containers with:

```
docker-compose up --build
```

Repeat this process as needed to resolve any issues.

## Learnings: issues and limitations

* Audio Input: running containers with direct access to audio devices (e.g., microphone) is not straightforward. *Docker containers do not natively support audio input devices*.

* On Linux-based containers, it is possible to use audio libraries like ALSA or PulseAudio. On Windows containers it is not possible to use audio devices.

**Since I was using Windows containers, I encountered limitations with audio input. With these learnings I conclude my research for now.**

## Documentation

[Install and run speech container](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-container-howto)

[Speech-to-text container](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-container-stt?tabs=container&pivots=programming-language-python)

[Running audio devices on Docker](https://www.reddit.com/r/docker/comments/yne4qy/tricky_with_audio_and_microphone_in_docker/)

[ALSA or Pulseaudio (for Linux containers)](https://github.com/mviereck/x11docker/wiki/Container-sound:-ALSA-or-Pulseaudio)
