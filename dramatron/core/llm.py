import time
from typing import Optional, NamedTuple, List, Dict, Any
import google.generativeai as genai

_MAX_RETRIES = 10
_TIMEOUT = 120.0

DEFAULT_SYSTEM_PROMPT = (
    "You are a writing assistant. You are given formatted examples of storytelling structures "
    "including a logline, characters, plot points, location descriptions, and dialogue. "
    "Your goal is to continue the story following exactly the same format. "
    "Write detailed, rich descriptions and creative ideas. "
    "Always finish your response with **END**."
)

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
        self._model_param = model_param or DEFAULT_SYSTEM_PROMPT
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
        self._client = genai.GenerativeModel(model, system_instruction=self._model_param)

    def sample(self,
               prompt: str,
               sample_length: Optional[int] = None,
               seed: Optional[int] = None,
               num_samples: int = 1):
        if sample_length is None:
            sample_length = self._sample_length

        generation_config = {
            "temperature": self._config_sampling.get("temp", 1.0),
            "top_p": self._config_sampling.get("prob", 0.95),
            "max_output_tokens": sample_length,
        }

        try:
            response = self._client.generate_content(prompt, generation_config=generation_config)

            # Robust check for text in response
            if response.candidates and response.candidates[0].content.parts:
                text = response.text
            else:
                # Handle cases where response might be blocked or empty
                text = ""
                if hasattr(response, 'prompt_feedback') and response.prompt_feedback.block_reason:
                     text = f"Content blocked by safety filters. Reason: {response.prompt_feedback.block_reason} "

            results = [LanguageResponse(text=text,
                                        text_length=len(text),
                                        prompt=prompt,
                                        prompt_length=len(prompt))]
            return results
        except Exception as e:
            # Fallback for unexpected errors
            return [LanguageResponse(text=f"Error during generation: {str(e)}", text_length=0, prompt=prompt, prompt_length=len(prompt))]

class OpenAIAPI(LanguageAPI):
    def __init__(self, sample_length, api_key, model="gpt-4-1106-preview", system_prompt=None, config_sampling=None, **kwargs):
        super().__init__(sample_length, model, system_prompt, config_sampling, **kwargs)
        try:
            from openai import OpenAI
            self._client = OpenAI(api_key=api_key)
        except ImportError:
            self._client = None

    def sample(self, prompt, sample_length=None, seed=None, num_samples=1):
        if self._client is None:
             return [LanguageResponse(text="Error: openai library not installed.", text_length=0, prompt=prompt, prompt_length=len(prompt))]

        if sample_length is None:
            sample_length = self._sample_length
        try:
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
        except Exception as e:
            return [LanguageResponse(text=f"Error: {str(e)}", text_length=0, prompt=prompt, prompt_length=len(prompt))]

class GroqAPI(LanguageAPI):
    def __init__(self, sample_length, api_key, model="mixtral-8x7b-32768", system_prompt=None, config_sampling=None, **kwargs):
        super().__init__(sample_length, model, system_prompt, config_sampling, **kwargs)
        try:
            from groq import Groq
            self._client = Groq(api_key=api_key)
        except ImportError:
            self._client = None

    def sample(self, prompt, sample_length=None, seed=None, num_samples=1):
        if self._client is None:
             return [LanguageResponse(text="Error: groq library not installed.", text_length=0, prompt=prompt, prompt_length=len(prompt))]

        if sample_length is None:
            sample_length = self._sample_length
        try:
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
        except Exception as e:
             return [LanguageResponse(text=f"Error: {str(e)}", text_length=0, prompt=prompt, prompt_length=len(prompt))]
