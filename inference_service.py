from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from src.services.prompt_service import prepare_prompt

MODEL_NAME = "HuggingFaceTB/SmolLM2-360M-Instruct"

tokenizer = None
model = None


def load_model():
    global tokenizer, model

    print("Loading SLM model...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float32
    )

    print("SLM model loaded successfully!")


def generate_answer(question):
    if model is None or tokenizer is None:
        load_model()

    prompt = prepare_prompt(question)

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=False
        )

    answer = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[1]:],
        skip_special_tokens=True
    )

    return answer.strip()