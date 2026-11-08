"""Optional Hugging Face causal-language-model adapter.

Importing this module does not download weights. Model loading only occurs when
``TransformersPredictor`` is instantiated explicitly by an inference command.
"""

from __future__ import annotations


class TransformersPredictor:
    """Minimal predictor compatible with :func:`runner.run_inference`."""

    def __init__(self, model_id: str, *, max_new_tokens: int = 32, temperature: float = 0.0):
        try:
            import torch
            from transformers import AutoModelForCausalLM, AutoTokenizer
        except ImportError as exc:
            raise RuntimeError("Install the inference extra: pip install -e '.[inference]'") from exc

        self._torch = torch
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        self.model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=dtype, device_map="auto")
        self.model.eval()
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature

    def __call__(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        generation_kwargs = {"max_new_tokens": self.max_new_tokens, "do_sample": self.temperature > 0}
        if self.temperature > 0:
            generation_kwargs["temperature"] = self.temperature
        with self._torch.no_grad():
            output = self.model.generate(**inputs, **generation_kwargs)
        generated = output[0][inputs["input_ids"].shape[-1] :]
        return self.tokenizer.decode(generated, skip_special_tokens=True).strip()
