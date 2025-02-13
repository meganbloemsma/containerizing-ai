# AI on the Edge

This repository contains learnings on **containerizing Azure AI models** and running them in local or hybrid environments. This is a **living repository**, meaning it will be updated over time as I gain more experience with containerizing specific AI models.

- The `src/` folder contains quickstart examples for Azure AI models, including installation instructions (if applicable).  
- The `docs/` folder contains in-depth learnings, organized by Azure AI service.

## General Learnings

Microsoft provides official [documentation](https://learn.microsoft.com/en-us/azure/ai-services/containers/container-faq) on how to containerize Azure AI services. However, it can differ per service what the set-up looks like and whether there are differences from the Azure service variant.

For example, Azure Speech contains language detection and speech-to-text when deployed on Azure. But when you use the container version language detection is not included and you need a separate container service.

This repository complements the official resources with hands-on insights and practical examples.

## Detailed Insights and Learnings per Service

| Azure AI Service | Documentation Link                                   | Status    |
|------------------|-------------------------------------------------------|-----------|
| Azure Speech     | [Azure Speech Learnings](docs/azure-speech-learnings.md) | In Progress |
| *TBD* | *TBD*                          | *Planned*  |

---

## 'Sending': containerizing a D&D spell

**(WIP)**
'Sending' is a spell used in Dungeons and Dragons, and I've created a [personal project to bring it to life](https://github.com/meganbloemsma/send-message). In this repo you may find code to containerize the application [here](https://github.com/meganbloemsma/ai-on-the-edge/src/sending-containerized).

## Contributions

Feel free to explore the resources and check back for updates as new services and insights are added. If you'd like to share your own learnings, please create a pull request.
