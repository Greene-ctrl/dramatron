import time
from typing import Optional, NamedTuple, List, Dict
import google.generativeai as genai

_MAX_RETRIES = 10
_TIMEOUT = 120.0

class LanguageResponse(NamedTuple):
    prompt: str
    prompt_length: int
    text: str
    text_length: int

class LanguageAPI:
    """Language model wrapper."""

    def __init__(self,
                 sample_length: int,
                 model: Optional[str] = None,
                 model_param: Optional[str] = None,
                 config_sampling: Optional[dict] = None,
                 seed: Optional[int] = None,
                 max_retries: int = _MAX_RETRIES,
                 timeout: float = _TIMEOUT):
        self._sample_length = sample_length
        self._model = model
        self._model_param = model_param
        self._config_sampling = config_sampling or {}
        self._seed = seed
        self._max_retries = max_retries
        self._timeout = timeout

    @property
    def default_sample_length(self):
        return self._sample_length

    @property
    def model(self):
        return self._model

    @property
    def model_param(self):
        return self._model_param

    @property
    def model_metadata(self):
        return None

    @property
    def seed(self):
        return self._seed

    @property
    def config_sampling(self):
        return self._config_sampling

    def sample(self,
               prompt: str,
               sample_length: Optional[int] = None,
               seed: Optional[int] = None,
               num_samples: int = 1):
        """Sample model with provided prompt, optional sample_length and seed."""
        raise NotImplementedError('sample method not implemented in generic class')

class FilterAPI:
    """Filter model wrapper."""
    def validate(self, text: str):
        raise NotImplementedError('validate not implemented in generic class')

class GoogleAPI(LanguageAPI):
    """A class wrapping the Google Gemini language model API."""

    def __init__(self,
                 sample_length: int,
                 api_key: str,
                 model: str = "gemini-1.5-pro",
                 system_prompt: Optional[str] = None,
                 config_sampling: Optional[dict] = None,
                 seed: Optional[int] = None,
                 max_retries: int = _MAX_RETRIES,
                 timeout: float = _TIMEOUT):
        super().__init__(sample_length=sample_length,
                         model=model,
                         model_param=system_prompt,
                         config_sampling=config_sampling,
                         seed=seed,
                         max_retries=max_retries,
                         timeout=timeout)
        genai.configure(api_key=api_key)
        self._client = genai.GenerativeModel(model, system_instruction=system_prompt)

    def sample(self,
               prompt: str,
               sample_length: Optional[int] = None,
               seed: Optional[int] = None,
               num_samples: int = 1):
        if sample_length is None:
            sample_length = self._sample_length
        response = self._client.generate_content(prompt)
        results = [LanguageResponse(text=response.text,
                                    text_length=len(response.text),
                                    prompt=prompt,
                                    prompt_length=len(prompt))]
        return results

# Placeholder for OpenAIAPI and GroqAPI as they require external libraries
# that might not be installed yet or were in the colab code.
# I'll implement them more robustly if needed.

class OpenAIAPI(LanguageAPI):
    def __init__(self, sample_length, api_key, model="gpt-4-1106-preview", system_prompt=None, config_sampling=None, **kwargs):
        super().__init__(sample_length, model, system_prompt, config_sampling, **kwargs)
        from openai import OpenAI
        self._client = OpenAI(api_key=api_key)

    def sample(self, prompt, sample_length=None, seed=None, num_samples=1):
        if sample_length is None:
            sample_length = self._sample_length
        response = self._client.chat.completions.create(
            model=self._model,
            max_tokens=sample_length,
            temperature=self._config_sampling.get('temp', 1.0),
            top_p=self._config_sampling.get('prob', 0.95),
            frequency_penalty=self._config_sampling.get('frequency_penalty', 0.0),
            presence_penalty=self._config_sampling.get('presence_penalty', 0.0),
            messages=[
                {"role": "system", "content": self._model_param},
                {"role": "user", "content": prompt}
            ]
        )
        response_text = response.choices[0].message.content if response.choices else ""
        return [LanguageResponse(text=response_text, text_length=len(response_text), prompt=prompt, prompt_length=len(prompt))]

class GroqAPI(LanguageAPI):
    def __init__(self, sample_length, api_key, model="mixtral-8x7b-32768", system_prompt=None, config_sampling=None, **kwargs):
        super().__init__(sample_length, model, system_prompt, config_sampling, **kwargs)
        from groq import Groq
        self._client = Groq(api_key=api_key)

    def sample(self, prompt, sample_length=None, seed=None, num_samples=1):
        if sample_length is None:
            sample_length = self._sample_length
        response = self._client.chat.completions.create(
            model=self._model,
            max_tokens=sample_length,
            temperature=self._config_sampling.get('temp', 1.0),
            top_p=self._config_sampling.get('prob', 0.95),
            messages=[
                {"role": "system", "content": self._model_param},
                {"role": "user", "content": prompt}
            ]
        )
        response_text = response.choices[0].message.content if response.choices else ""
        return [LanguageResponse(text=response_text, text_length=len(response_text), prompt=prompt, prompt_length=len(prompt))]
