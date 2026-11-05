from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"


def load_model():
    print("Loading the SLM model...")

    try:
        tokenizer = AutoTokenizer.from_pretrained(
            MODEL_NAME,
            local_files_only=True
        )

        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            local_files_only=True,
            torch_dtype=torch.float32
        )

        model.eval()

        print("Model loaded successfully!")

        return tokenizer, model

    except Exception as error:
        print("Model is not available locally.")
        print("No internet download will be attempted.")
        print("Details:", error)

        return None, None


if __name__ == "__main__":
    tokenizer, model = load_model()

    if model is not None:
        print("SLM is ready for testing.")