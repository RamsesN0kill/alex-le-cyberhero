#!/bin/bash
# 🚀 Alex le CyberHero — vérificateur de réponses de quiz
# ------------------------------------------------------------
# Usage : ./verifie.sh "ta réponse"
# Le script affiche l'empreinte SHA-256 de ta réponse.
# Compare-la à celle indiquée dans le tableau de la semaine.
# Si les deux empreintes sont identiques : bonne réponse ! ✅
#
# Règle de format des réponses :
#   - tout en MINUSCULES
#   - SANS accents (ex : "filtre" et non "filtré")
#   - exactement le format demandé, espaces compris
# ------------------------------------------------------------
if [ -z "$1" ]; then
  echo "Usage : ./verifie.sh \"ta réponse\""
  exit 1
fi
echo -n "$1" | sha256sum | awk '{print $1}'
