"""All settings in one place. Anything you may want to tune lives here."""
import os
from pathlib import Path

try:
    from dotenv import load_dotenv  
    load_dotenv()
except ImportError:
    pass

PKG_DIR = Path(__file__).resolve().parent

REPO_ROOT = Path(os.getenv("SOILSENSE_REPO_ROOT", PKG_DIR.parent)).resolve()
TEAM_CLIMATE_CSV = REPO_ROOT / "climate.csv"

PROC_DIR = PKG_DIR / "data" / "processed"
CACHE_DIR = Path(os.getenv("SOILSENSE_CACHE_DIR", PKG_DIR / "data" / "cache"))
PROMPT_DIR = PKG_DIR / "prompts"
GLOSSARY_PATH = PKG_DIR / "data" / "glossary.json"
RAW_DIR = PKG_DIR / "data" / "raw"          


def get_secret(name: str):
   
    try:
        import streamlit as st
        try:
            if name in st.secrets:
                return str(st.secrets[name]) or None
        except Exception:      
            pass
    except ImportError:
        pass
    return os.getenv(name) or None


def _flag(name: str, default: str = "false") -> bool:
    v = get_secret(name)          
    return (v if v is not None else default).strip().lower() in ("1", "true", "yes", "on")


# --- switches ---------------------------------------------------------------
USE_MOCK = _flag("USE_MOCK")                             
USE_POWER_API = _flag("USE_POWER_API", "true")            
ENABLE_VOICE_TOOL = _flag("SS_AGENT_ENABLE_VOICE")        
FORCE_FAKE_TEAM = _flag("SS_AGENT_FORCE_FAKE")            

# --- languages ----------------------------------------------------------------
LANG_NAMES = {"ar": "العربية", "en": "English", "bn": "বাংলা", "ur": "اردو", "hi": "हिन्दी"}
ENABLED_LANGS = [c for c in os.getenv("ENABLED_LANGS", "ar,en,bn").split(",") if c in LANG_NAMES]
RTL_LANGS = {"ar", "ur"}
DEFAULT_LANG = ENABLED_LANGS[0] if ENABLED_LANGS else "en"


PROVIDERS = [
    dict(name="gemini", key_env="GEMINI_API_KEY",
         base_url="https://generativelanguage.googleapis.com/v1beta/openai",
         model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash")),
    dict(name="groq", key_env="GROQ_API_KEY",
         base_url="https://api.groq.com/openai/v1",
         model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")),
    dict(name="openrouter", key_env="OPENROUTER_API_KEY",
         base_url="https://openrouter.ai/api/v1",
         model=os.getenv("OPENROUTER_MODEL", "meta-llama/llama-3.3-70b-instruct:free")),
]
LLM_TIMEOUT = 30
MAX_TOKENS = 900
MAX_TOOL_ROUNDS = 4

ROTATION_SITE_LABEL = {   
    "ar": "موقع واحد في الداخلية (23.71 شمال، 57.91 شرق)",
    "en": "one site in Al Dakhiliyah (23.71N, 57.91E)",
    "bn": "আল দাখিলিয়ার একটি স্থান (23.71N, 57.91E)",
}
ROTATION_SITE_FALLBACK = (23.7067, 57.9065)   
ROTATION_MAX_KM = 50          


PRIORITY_CHOICES = {"not_important": 0.5, "normal": 1.0, "very_important": 2.0}
PRIORITY_KEYS = ("water", "soil", "income")
DEFAULT_PRIORITY = 1.0
DEFAULT_IRRIGATION_MM = 250   
IRRIGATION_MAX_MM = 3000      


HEAT_DAY_C = 40.0
COMPLETE_YEAR_DAYS = 360
RISK_BINS = (40, 70, 90)
LOCAL_SITE_MAX_KM = 50
DIST_MEDIUM_KM = 50
DIST_LOW_KM = 150


if not any(get_secret(p["key_env"]) for p in PROVIDERS):
    USE_MOCK = True