#!/bin/bash
# ============================================================
# Régénère le PDF du manuel à partir des fichiers manuel/*.md
# Usage : ./outils/generer-pdf.sh
# ============================================================
set -e
cd "$(dirname "$0")/.."

VENV=".venv-pdf"
if [ ! -d "$VENV" ]; then
  echo "Création de l'environnement Python (une seule fois)..."
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install --quiet fpdf2
fi

"$VENV/bin/python" outils/build_pdf.py "Manuel-Alex-le-CyberHero.pdf" \
  manuel/00-introduction.md \
  manuel/01-terrain-de-jeu.md \
  manuel/02-reseau.md \
  manuel/03-observer.md \
  manuel/04-attaque-web.md \
  manuel/05-exploitation.md \
  manuel/06-defense.md \
  manuel/07-detection.md \
  manuel/08-incident.md
