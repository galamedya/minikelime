import json

LANGUAGES = {
    "tr": "languages/tr.json",
    "en": "languages/en.json",
    "az": "languages/az.json"
}

CURRENT_LANGUAGE = "tr"

def set_language(lang_code):
    global CURRENT_LANGUAGE
    if lang_code in LANGUAGES:
        CURRENT_LANGUAGE = lang_code

def translate(key):
    with open(LANGUAGES[CURRENT_LANGUAGE], "r") as lang_file:
        translations = json.load(lang_file)
        return translations.get(key, key)

def get_languages():
    return list(LANGUAGES.keys())
