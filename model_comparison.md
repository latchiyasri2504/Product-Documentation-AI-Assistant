# Small Language Model Comparison

## 1. Introduction

Small Language Models (SLMs) are compact AI models that can perform tasks such as answering questions, generating text and understanding instructions.

For this project, three SLMs are compared to select a suitable model for the Product Documentation AI Assistant.

## 2. Models Selected for Comparison

### Model 1: Qwen2.5-0.5B-Instruct

- Developer: Qwen
- Model size: 0.5 Billion parameters
- Context length: 32K tokens
- License: Apache 2.0
- Capability: Instruction following and question answering
- Hardware: Suitable for experimenting with low-resource systems, especially with quantization.

### Model 2: SmolLM2-1.7B-Instruct

- Developer: Hugging Face
- Model size: 1.7 Billion parameters
- Context length: 8K tokens
- License: Apache 2.0
- Capability: Text generation and conversational question answering
- Hardware: Requires more memory than smaller models.

### Model 3: Phi-3.5-mini-instruct

- Developer: Microsoft
- Model size: 3.8 Billion parameters
- Context length: 128K tokens
- License: MIT
- Capability: Reasoning, instruction following and document question answering
- Hardware: Requires considerably more resources than the smaller models.

## 3. Model Comparison Table

| Criteria | Qwen2.5 | SmolLM2 | Phi-3.5 |
|---|---|---|---|
| Parameters | 0.5B | 1.7B | 3.8B |
| Context | 32K | 8K | 128K |
| License | Apache 2.0 | Apache 2.0 | MIT |
| Main strength | Lightweight | Conversation | Reasoning |
| Resource needs | Low | Medium | High |

## 4. Selected Model

After comparing the three models, Qwen2.5-0.5B-Instruct is selected as the initial candidate for this project.

### Reasons for Selection

1. It has fewer parameters than the other two models.
2. It requires comparatively fewer computing resources.
3. It supports instruction-based question answering.
4. It is suitable for experimenting with a product documentation assistant.
5. It uses the Apache 2.0 license.

## 5. Conclusion

Qwen2.5-0.5B-Instruct is selected as the preferred initial model because of its smaller size and lower resource requirements.

The final selection will be confirmed after testing its performance on the project dataset.