# 大模型究竟是什么？NLP 导论和 LLM API 调用

## 关键概念

### NLP

**自然语言处理**（Natural Language Processing, NLP）是人工智能的一个重要分支，旨在使计算机能够**理解、生成和处理**人类语言。

NLP 涉及多个领域的知识，包括计算机科学、语言学和统计学。其应用范围广泛，包括机器翻译、情感分析、文本生成、语音识别等。

### 词向量

**词向量**（Word Embeddings）是将词语映射到高维空间中的向量表示。通过这种方式，计算机可以更好地理解词语之间的关系和语义。

> 计算文字背后的概念：国王 - 男人 + 女人 = 女王

> 可视化演示：[Embedding Projector](https://projector.tensorflow.org/)

### 注意力机制

**注意力机制**（Attention Mechanism）是一种模仿人类注意力的机制，允许模型在处理输入数据时动态地关注不同部分的信息。

> Transformer 注解：[The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html)

> BERT 图解：[The Illustrated BERT, ELMo, and co.](https://jalammar.github.io/illustrated-bert/)

> BERT 注意力机制演示：[BertViz](https://github.com/jessevig/bertviz)

### 大模型

**大模型**（Large Language Models, LLMs）是指具有大量参数和复杂结构的语言模型，能够处理和生成自然语言文本。

从完形填空到写作大师。大模型所擅长的任务是生成文本，而不仅仅是理解文本。

大模型一般会先进行**预训练**，然后通过**微调**来适应特定任务。

## 实践应用

有不同的方法可以接触和使用大模型，由浅到深地：

1. 使用现有的大模型应用程序或网页：例如 ChatGPT、DeepSeek 等，这些平台提供了用户友好的界面，允许用户直接与大模型进行交互，但是无法深入了解模型的工作原理。
2. 调用现有的大模型 API：例如 OpenAI API 等，这些服务允许开发者通过编程接口调用大模型的功能，适合有一定编程基础的用户。
3. 自行部署或微调大模型：例如使用开源模型在本地或云端部署或微调，适合有较强技术背景以及算力资源的用户。
4. 自行训练大模型：需要极其大量的数据和计算资源，适合研究机构或大型企业。

本节课程将重点介绍第二种方法，后续课节可能会设计第三种方法。
