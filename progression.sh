#!/bin/bash
# ============================================================
# 🚀 Alex le CyberHero — Suivi de progression
# ============================================================
# Tableau de bord de ton avancement dans le programme.
# Ta progression est sauvegardée en local dans .progression.state
# (fichier perso, non versionné).
#
# UTILISATION
#   ./progression.sh                 -> affiche le tableau de bord
#   ./progression.sh done 1 quiz     -> valide le quiz de la semaine 1
#   ./progression.sh done 1 boss     -> valide le défi du Boss
#   ./progression.sh done 1 badge    -> valide la room/badge en ligne
#   ./progression.sh done 1 all      -> valide les 3 d'un coup
#   ./progression.sh undo 1 quiz     -> annule une validation
#   ./progression.sh reset           -> remet tout à zéro
#   ./progression.sh help            -> affiche l'aide
# ============================================================

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATE="$DIR/.progression.state"
touch "$STATE"

# Titres des badges (index 1..8)
TITRES=( "" \
  "Maître du Terminal" \
  "Cartographe du Réseau" \
  "Œil de Lynx Réseau" \
  "Briseur de Requêtes" \
  "Maître de l'Exploit" \
  "Gardien du Système" \
  "Sentinelle du SOC" \
  "Alex le CyberHero — Niveau Maître" )

THEMES=( "" \
  "Linux, terminal, permissions" \
  "OSI/TCP-IP, IP, sous-réseaux" \
  "Wireshark, Nmap, DNS" \
  "OWASP, SQLi, XSS, Burp" \
  "Metasploit, reverse shell" \
  "Hardening, ufw, SSH, fail2ban" \
  "Logs, IDS, SIEM" \
  "Réponse à incident (final)" )

est_fait() { grep -qx "$1:$2" "$STATE"; }

marque() {
  local w="$1" k="$2"
  if ! est_fait "$w" "$k"; then echo "$w:$k" >> "$STATE"; fi
}

demarque() {
  local w="$1" k="$2"
  grep -vx "$w:$k" "$STATE" > "$STATE.tmp" 2>/dev/null
  mv "$STATE.tmp" "$STATE"
}

case_coche() { est_fait "$1" "$2" && echo "[x]" || echo "[ ]"; }

valide_arg() {
  if ! [[ "$1" =~ ^[1-8]$ ]]; then echo "❌ Numéro de semaine invalide (1 à 8)."; exit 1; fi
  case "$2" in quiz|boss|badge|all) ;; *) echo "❌ Étape invalide (quiz, boss, badge ou all)."; exit 1;; esac
}

# Pad un texte à une largeur donnée en comptant les CARACTÈRES (gère les accents)
pad() {
  local s="$1" w="$2" len=${#1} n
  printf "%s" "$s"
  n=$(( w - len ))
  [ "$n" -gt 0 ] && printf '%*s' "$n" ""
}

barre() {
  # $1 = nb faits, $2 = total, $3 = largeur
  local fait=$1 total=$2 larg=${3:-24} plein vide s="" i
  plein=$(( total > 0 ? fait * larg / total : 0 ))
  vide=$(( larg - plein ))
  for (( i=0; i<plein; i++ )); do s+="█"; done
  for (( i=0; i<vide;  i++ )); do s+="░"; done
  printf "[%s] %d/%d" "$s" "$fait" "$total"
}

dashboard() {
  local total_etapes=24 faits=0 badges=0
  echo
  echo "  🚀 ALEX LE CYBERHERO — TABLEAU DE BORD D'ALEXANDRE"
  echo "  ══════════════════════════════════════════════════════════"
  echo
  printf "  "; pad "Sem" 5; pad "Thème" 32; pad "Quiz" 6; pad "Boss" 6; pad "Badge" 7; printf "🏆\n"
  echo "  ----------------------------------------------------------------------"
  for w in 1 2 3 4 5 6 7 8; do
    local q b g trophee=" "
    q=$(case_coche "$w" quiz); b=$(case_coche "$w" boss); g=$(case_coche "$w" badge)
    est_fait "$w" quiz && faits=$((faits+1))
    est_fait "$w" boss && faits=$((faits+1))
    est_fait "$w" badge && faits=$((faits+1))
    if est_fait "$w" quiz && est_fait "$w" boss && est_fait "$w" badge; then
      trophee="🏆"; badges=$((badges+1))
    fi
    printf "  "; pad "$w" 5; pad "${THEMES[$w]}" 32; pad "$q" 6; pad "$b" 6; pad "$g" 7; printf "%s\n" "$trophee"
  done
  echo "  ----------------------------------------------------------------------"
  echo
  printf "  Progression  : "; barre "$faits" "$total_etapes" 24; echo
  printf "  Badges gagnés: %d/8\n" "$badges"
  echo
  if [ "$badges" -eq 8 ]; then
    echo "  🎖️  FÉLICITATIONS ALEXANDRE — tu es Alex le CyberHero, Niveau Maître !"
  else
    local prochaine=$((badges+1))
    echo "  🎯 Prochain objectif : Semaine $prochaine — Badge « ${TITRES[$prochaine]} »"
  fi
  echo
  echo "  (Valide une étape avec : ./progression.sh done <sem> <quiz|boss|badge|all>)"
  echo
}

aide() {
  sed -n '2,30p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
}

# ---- Routage des commandes ----
case "$1" in
  ""|dashboard) dashboard ;;
  help|-h|--help) aide ;;
  reset)
    : > "$STATE"
    echo "🧹 Progression remise à zéro. Bon courage pour le grand recommencement !"
    ;;
  done)
    valide_arg "$2" "$3"
    if [ "$3" = "all" ]; then
      marque "$2" quiz; marque "$2" boss; marque "$2" badge
      echo "✅ Semaine $2 : quiz + boss + badge validés."
    else
      marque "$2" "$3"
      echo "✅ Semaine $2 — $3 validé."
    fi
    if est_fait "$2" quiz && est_fait "$2" boss && est_fait "$2" badge; then
      echo "🏆 BADGE DÉBLOQUÉ : « ${TITRES[$2]} » ! 🎉"
    fi
    ;;
  undo)
    valide_arg "$2" "$3"
    if [ "$3" = "all" ]; then
      demarque "$2" quiz; demarque "$2" boss; demarque "$2" badge
    else
      demarque "$2" "$3"
    fi
    echo "↩️  Semaine $2 — $3 annulé."
    ;;
  *)
    echo "❌ Commande inconnue : '$1'. Tape : ./progression.sh help"
    exit 1
    ;;
esac
