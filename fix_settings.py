import re
path = "meuprojeto/settings.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
old = "'ENGINE': 'django.db.backends.sqlite3',\\n        'NAME': BASE_DIR / 'db.sqlite3',\\n    }"
new = "'ENGINE': 'django.db.backends.sqlite3',\n            'NAME': BASE_DIR / 'db.sqlite3',\n        }"
content = content.replace(old, new)
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Pronto! Arquivo corrigido.")
