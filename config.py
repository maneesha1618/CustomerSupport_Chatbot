import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# General settings
ENV = os.getenv("ENV", "development")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Model Config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# LLaMA model path

LLAMA_MODEL_PATH = os.getenv("LLAMA_MODEL_PATH", "models/tinyllama-q4_0.gguf")

# Other custom settings
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "512"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.0"))
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# General settings
ENV = os.getenv("ENV", "development")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Model Config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# LLaMA model path
LLAMA_MODEL_PATH = os.getenv("LLAMA_MODEL_PATH", "models/tinyllama-q4_0.gguf")

# Other custom settings
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "512"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.0"))


HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")