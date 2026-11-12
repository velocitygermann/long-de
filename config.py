"""VELOCITY LONGFORM - 16:9 chapter lesson, brand and motion constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

TARGET_CHAPTERS = 8
PHRASES_PER_CHAPTER = 7
TARGET_PHRASES = TARGET_CHAPTERS * PHRASES_PER_CHAPTER

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY GERMAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "GERMAN"
HANDLE = "@velocitygerman"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'de',
 'name': 'German',
 'native_name': 'Deutsch',
 'history_key': 'german',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'de-DE-KatjaNeural',
 'native_fallback_voice': 'de-DE-ConradNeural',
 'native_engine': 'edge',
 'native_lang_code': 'de',
 'english_rate': '-4%',
 'native_rate': '-10%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': 'DEUTSCH',
 'translit_label': 'SAY IT LIKE',
 'flag': 'de',
 'greeting': 'Hallo!',
 'encouragement': 'Fantastisch!',
 'rtl': False,
 'char_tiles': False,
 'script_font': '',
 'glyphs': 'ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜäöüß'}
# ==== LANGUAGE PACK END ====

# ==== CATEGORIES START ====
CATEGORIES = {'Motivation': 'Motivation',
 'Love': 'Liebe',
 'Success': 'Erfolg',
 'Wisdom': 'Weisheit',
 'Happiness': 'Glück',
 'Self Improvement': 'Selbstverbesserung',
 'Gratitude': 'Dankbarkeit',
 'Friendship': 'Freundschaft',
 'Hope': 'Hoffnung',
 'Creativity': 'Kreativität',
 'Inner Peace': 'Innere Ruhe',
 'Confidence': 'Selbstvertrauen',
 'Perseverance': 'Ausdauer',
 'Inspiration': 'Inspiration',
 'Positive Life': 'Positives Leben',
 'Courage': 'Mut',
 'Kindness': 'Freundlichkeit',
 'Patience': 'Geduld',
 'Forgiveness': 'Verzeihung',
 'Strength': 'Stärke',
 'Joy': 'Freude',
 'Balance': 'Balance',
 'Growth': 'Wachstum',
 'Purpose': 'Zweck',
 'Mindfulness': 'Achtsamkeit',
 'Travel & Airport': 'Reisen & Flughafen',
 'Ordering Food & Dining': 'Essen bestellen & Essen gehen',
 'Shopping & Prices': 'Einkaufen & Preise',
 'Asking for Directions': 'Nach dem Weg fragen',
 'Hotel & Accommodation': 'Hotel & Unterkunft',
 'Daily Routine': 'Tagesablauf',
 'Meeting People & Greetings': 'Leute treffen & Begrüßungen',
 'Emergency & Health': 'Notfall & Gesundheit',
 'Public Transportation': 'Öffentliche Verkehrsmittel',
 'Work & Office': 'Arbeit & Büro',
 'Weather & Small Talk': 'Wetter & Small Talk',
 'Coffee Shop & Bakery': 'Café & Bäckerei',
 'Family & Home': 'Familie & Zuhause',
 'Hobbies & Free Time': 'Hobbys & Freizeit',
 'Dating & Romance': 'Dating & Romantik',
 'Phone Calls & Messages': 'Telefonate & Nachrichten',
 'Banking & Money': 'Bank & Geld',
 'Doctor & Pharmacy': 'Arzt & Apotheke',
 'Sports & Fitness': 'Sport & Fitness',
 'Celebrations & Parties': 'Feiern & Partys',
 'Feelings & Emotions': 'Gefühle & Emotionen',
 'Agreeing & Disagreeing': 'Zustimmen & Ablehnen',
 'Making Plans': 'Pläne schmieden',
 'Common Native Slang': 'Gängiger Slang',
 'Cultural Traditions': 'Kulturelle Traditionen'}
# ==== CATEGORIES END ====

CATEGORY_NAMES = list(CATEGORIES.keys())

AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-5.4-nano")
AI_FALLBACK_MODEL = os.getenv("AI_FALLBACK_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 7.2
CHAPTER_INTRO_DURATION = 4.4
OUTRO_DURATION = 13.0

EN_CARD_IN = 0.70
GAP_EN_NATIVE = 0.60
NATIVE_CARD_LEAD = 0.40
GAP_BEFORE_REPEAT = 1.00
TAIL_HOLD = 1.30

# ---------------------------------------------------------------- palette

INK = "#30303A"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#7C5CFF"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

# ==== HASHTAGS START ====
HASHTAGS = ['#learngerman',
 '#germanlessons',
 '#germanforbeginners',
 '#languagelearning',
 '#germanvocabulary',
 '#velocitygerman',
 '#dailygerman',
 '#german',
 '#learnlanguages',
 '#speakgerman']
# ==== HASHTAGS END ====
