# Human-AI Collaboration Enables More Empathic Conversations in Text-based Peer-to-Peer Mental Health Support
This repository contains a demo for our Human-AI Collaboration Approach For Enabling More Empathic Conversations in Text-based Peer-to-Peer Mental Health Support.

[[arxiv preprint](https://arxiv.org/pdf/2203.15144)] [[project webpage](bdata.uw.edu/empathy)]

If this code helps you in your research, please cite the following publication:
```bash
@article{Sharma2022Human,
  title={Human-AI Collaboration Enables More Empathic Conversations in Text-based Peer-to-Peer Mental Health Support},
  author={Sharma, Ashish and Lin, Inna W and Miner, Adam S and Atkins, David C and Althoff, Tim},
  journal={Nature Machine Intelligence (in press)},
  year={2022},
}
```
## Introduction

We develop Hailey, an AI-in-the-loop agent that provides just-in-time feedback to help participants who provide support (peer supporters) respond more empathically to those seeking help (support seekers). We evaluate Hailey in a randomized controlled trial with real-world peer supporters on TalkLife (N=300). We show that our Human-AI collaboration approach leads to a 19.60% increase in conversational empathy between peers overall.

![HAILEY_Overview](hailey_overview.JPG?raw=true "Title") 

## Quickstart

### 1. Prerequisites

Our framework can be compiled on Python 3 environments. The modules used in our code can be installed using:
```
$ pip install -r requirements.txt
```

### 2. Run API

We will use an API to request just-in-feedback. To run the API, please run the following command:

```
$ python api.py
```

**Note:** In this demo, the API only works with a sample example. To create a generalized version, use [empathic rewriting](https://arxiv.org/pdf/2101.07714.pdf). 


### 3. Start the Demo

Open [hailey_demo](hailey_demo.html) in your browser to start the demo.
