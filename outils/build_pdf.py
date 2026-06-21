#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de PDF pour « Alex le CyberHero — Manuel d'apprentissage ».
Convertit un sous-ensemble Markdown en PDF stylé avec fpdf2.

Usage :
    python build_pdf.py sortie.pdf fichier1.md fichier2.md ...
"""
import sys, re
from fpdf import FPDF

FONT_DIR = "/usr/share/fonts/truetype/dejavu"

# Palette
BLEU      = (28, 58, 110)     # titres
BLEU_CLR  = (52, 96, 168)     # accents
GRIS_CODE = (244, 245, 248)   # fond des blocs de code
GRIS_TXT  = (60, 60, 60)
ENCADRE   = (233, 242, 252)   # fond des encadrés "à retenir"
ENCADRE_B = (52, 96, 168)     # barre des encadrés
NOIR      = (20, 20, 20)
BLANC     = (255, 255, 255)

LH = 5.6          # hauteur de ligne du texte courant
EMOJI_RE = re.compile(
    "[" "\U0001F000-\U0001FAFF" "\U00002600-\U000027BF"
    "\U0001F1E6-\U0001F1FF" "\U00002190-\U000021FF"
    "\U00002B00-\U00002BFF" "\U0000FE00-\U0000FE0F" "\U0000200D" "]",
    flags=re.UNICODE)

def strip_emoji(s: str) -> str:
    return EMOJI_RE.sub("", s).replace("  ", " ").rstrip()

class Manuel(FPDF):
    def __init__(self):
        super().__init__(format="A4")
        self.set_auto_page_break(True, margin=20)
        self.set_margins(20, 20, 20)
        self.add_font("DejaVu", "",  f"{FONT_DIR}/DejaVuSans.ttf")
        self.add_font("DejaVu", "B", f"{FONT_DIR}/DejaVuSans-Bold.ttf")
        self.add_font("DejaVu", "I", f"{FONT_DIR}/DejaVuSans-Oblique.ttf")
        self.add_font("Mono",   "",  f"{FONT_DIR}/DejaVuSansMono.ttf")
        self.add_font("Mono",   "B", f"{FONT_DIR}/DejaVuSansMono-Bold.ttf")
        self.chapitre = ""

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-15)
        self.set_font("DejaVu", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 8, strip_emoji(self.chapitre), align="L")
        self.cell(0, 8, f"{self.page_no()}", align="R")

    # ---- contenu courant (gras / code / italique) ----
    def ecrire_inline(self, text):
        self.set_text_color(*NOIR)
        parts = re.split(r'(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*)', text)
        for p in parts:
            if not p:
                continue
            if p.startswith("`") and p.endswith("`"):
                self.set_font("Mono", "", 9.5)
                self.set_text_color(*BLEU_CLR)
                self.write(LH, p[1:-1])
                self.set_text_color(*NOIR)
            elif p.startswith("**") and p.endswith("**"):
                self.set_font("DejaVu", "B", 11)
                self.write(LH, p[2:-2])
            elif p.startswith("*") and p.endswith("*"):
                self.set_font("DejaVu", "I", 11)
                self.write(LH, p[1:-1])
            else:
                self.set_font("DejaVu", "", 11)
                self.write(LH, p)
        self.set_font("DejaVu", "", 11)

    def wrap(self, text, w):
        out, cur = [], ""
        for word in text.split():
            test = (cur + " " + word).strip()
            if self.get_string_width(test) <= w - 2 or not cur:
                cur = test
            else:
                out.append(cur); cur = word
        if cur:
            out.append(cur)
        return out or [""]


def parse_blocks(md):
    """Découpe le markdown en blocs logiques."""
    lines = md.split("\n")
    blocks, i = [], 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            code = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i]); i += 1
            i += 1
            blocks.append(("code", code)); continue
        if line.startswith("#### "):
            blocks.append(("h4", line[5:].strip())); i += 1; continue
        if line.startswith("### "):
            blocks.append(("h3", line[4:].strip())); i += 1; continue
        if line.startswith("## "):
            blocks.append(("h2", line[3:].strip())); i += 1; continue
        if line.startswith("# "):
            blocks.append(("h1", line[2:].strip())); i += 1; continue
        if re.match(r'^\s*\|.*\|\s*$', line):
            tbl = []
            while i < len(lines) and re.match(r'^\s*\|.*\|\s*$', lines[i]):
                tbl.append(lines[i]); i += 1
            blocks.append(("table", tbl)); continue
        if line.strip() in ("---", "***", "___"):
            blocks.append(("hr", None)); i += 1; continue
        if line.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].startswith(">"):
                quote.append(lines[i].lstrip(">").strip()); i += 1
            blocks.append(("quote", quote)); continue
        if re.match(r'^\s*[-*] ', line):
            items = []
            while i < len(lines) and re.match(r'^\s*[-*] ', lines[i]):
                indent = len(lines[i]) - len(lines[i].lstrip())
                items.append((indent, re.sub(r'^\s*[-*] ', '', lines[i]))); i += 1
            blocks.append(("ul", items)); continue
        if re.match(r'^\s*\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'^\s*\d+\. ', lines[i]):
                items.append(re.sub(r'^\s*\d+\. ', '', lines[i])); i += 1
            blocks.append(("ol", items)); continue
        if line.strip() == "":
            i += 1; continue
        # paragraphe (peut s'étendre sur plusieurs lignes consécutives)
        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() != "" and not re.match(
                r'^(#{1,4} |\s*[-*] |\s*\d+\. |>|```|\s*\|)', lines[i]) \
                and lines[i].strip() not in ("---", "***", "___"):
            para.append(lines[i]); i += 1
        blocks.append(("p", " ".join(para)))
    return blocks


def render(pdf, blocks):
    for kind, payload in blocks:
        if kind == "h1":
            pdf.add_page()
            pdf.chapitre = payload
            pdf.set_fill_color(*BLEU)
            pdf.set_text_color(*BLANC)
            pdf.set_font("DejaVu", "B", 20)
            pdf.multi_cell(0, 12, strip_emoji(payload), fill=True)
            pdf.ln(4)
        elif kind == "h2":
            pdf.ln(3)
            pdf.set_text_color(*BLEU)
            pdf.set_font("DejaVu", "B", 15)
            pdf.multi_cell(0, 8, strip_emoji(payload))
            pdf.set_draw_color(*BLEU_CLR); pdf.set_line_width(0.4)
            y = pdf.get_y() + 1
            pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
            pdf.ln(3)
        elif kind == "h3":
            pdf.ln(2)
            pdf.set_text_color(*BLEU_CLR)
            pdf.set_font("DejaVu", "B", 12.5)
            pdf.multi_cell(0, 7, strip_emoji(payload))
            pdf.ln(1)
        elif kind == "h4":
            pdf.ln(1)
            pdf.set_text_color(*GRIS_TXT)
            pdf.set_font("DejaVu", "B", 11)
            pdf.multi_cell(0, 6, strip_emoji(payload))
        elif kind == "p":
            pdf.set_x(pdf.l_margin)
            pdf.ecrire_inline(strip_emoji(payload))
            pdf.ln(LH + 2)
        elif kind == "ul":
            for indent, item in payload:
                off = 4 + (4 if indent >= 2 else 0)
                pdf.set_x(pdf.l_margin + off)
                pdf.set_font("DejaVu", "B", 11); pdf.set_text_color(*BLEU_CLR)
                pdf.write(LH, "•  ")
                save = pdf.l_margin
                pdf.set_left_margin(pdf.l_margin + off + 5)
                pdf.set_x(pdf.l_margin)
                pdf.ecrire_inline(strip_emoji(item))
                pdf.set_left_margin(save)
                pdf.ln(LH + 1)
            pdf.ln(1)
        elif kind == "ol":
            for n, item in enumerate(payload, 1):
                pdf.set_x(pdf.l_margin + 4)
                pdf.set_font("DejaVu", "B", 11); pdf.set_text_color(*BLEU_CLR)
                pdf.write(LH, f"{n}.  ")
                save = pdf.l_margin
                pdf.set_left_margin(pdf.l_margin + 11)
                pdf.set_x(pdf.l_margin)
                pdf.ecrire_inline(strip_emoji(item))
                pdf.set_left_margin(save)
                pdf.ln(LH + 1)
            pdf.ln(1)
        elif kind == "code":
            pdf.ln(1)
            pdf.set_font("Mono", "", 9.5)
            pdf.set_fill_color(*GRIS_CODE)
            pdf.set_text_color(*NOIR)
            usable = pdf.w - pdf.l_margin - pdf.r_margin
            for cl in payload:
                wrapped = pdf.wrap(cl, usable - 4) if cl else [""]
                for wl in wrapped:
                    pdf.set_x(pdf.l_margin)
                    pdf.cell(usable, 5.2, "  " + wl, fill=True)
                    pdf.ln(5.2)
            pdf.ln(3)
        elif kind == "quote":
            txt = strip_emoji(" ".join(payload))
            pdf.ln(1)
            usable = pdf.w - pdf.l_margin - pdf.r_margin
            lines = pdf.wrap(re.sub(r'[*`]', '', txt), usable - 8)
            h = len(lines) * LH + 4
            y0 = pdf.get_y()
            if y0 + h > pdf.h - pdf.b_margin:
                pdf.add_page(); y0 = pdf.get_y()
            pdf.set_fill_color(*ENCADRE)
            pdf.rect(pdf.l_margin, y0, usable, h, style="F")
            pdf.set_fill_color(*ENCADRE_B)
            pdf.rect(pdf.l_margin, y0, 1.6, h, style="F")
            pdf.set_xy(pdf.l_margin + 6, y0 + 2)
            pdf.set_font("DejaVu", "I", 10.5); pdf.set_text_color(*BLEU)
            for ln_ in lines:
                pdf.set_x(pdf.l_margin + 6)
                pdf.cell(usable - 8, LH, ln_)
                pdf.ln(LH)
            pdf.set_y(y0 + h); pdf.ln(3)
        elif kind == "table":
            render_table(pdf, payload)
        elif kind == "hr":
            pdf.ln(2)
            pdf.set_draw_color(210, 210, 210); pdf.set_line_width(0.3)
            y = pdf.get_y()
            pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
            pdf.ln(4)


def render_table(pdf, rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    cells = [r for r in cells if not all(re.match(r'^:?-+:?$', x or "-") for x in r)]
    if not cells:
        return
    ncol = max(len(r) for r in cells)
    cells = [r + [""] * (ncol - len(r)) for r in cells]
    usable = pdf.w - pdf.l_margin - pdf.r_margin
    cw = usable / ncol
    pdf.ln(1)
    for ri, row in enumerate(cells):
        header = (ri == 0)
        pdf.set_font("DejaVu", "B" if header else "", 9.5)
        wrapped = [pdf.wrap(re.sub(r'[*`]', '', c), cw) for c in row]
        nlines = max(len(w) for w in wrapped)
        h = nlines * 4.8 + 2
        if pdf.get_y() + h > pdf.h - pdf.b_margin:
            pdf.add_page()
        x0, y0 = pdf.l_margin, pdf.get_y()
        for ci, w in enumerate(wrapped):
            x = x0 + ci * cw
            if header:
                pdf.set_fill_color(*BLEU); pdf.set_text_color(*BLANC)
            else:
                pdf.set_fill_color(248, 249, 251) if ri % 2 else pdf.set_fill_color(*BLANC)
                pdf.set_text_color(*NOIR)
            pdf.rect(x, y0, cw, h, style="F")
            pdf.set_draw_color(225, 225, 225); pdf.set_line_width(0.2)
            pdf.rect(x, y0, cw, h)
            for li, wl in enumerate(w):
                pdf.set_xy(x + 1.5, y0 + 1 + li * 4.8)
                pdf.cell(cw - 3, 4.6, wl)
        pdf.set_y(y0 + h)
    pdf.set_text_color(*NOIR)
    pdf.ln(4)


def cover(pdf):
    pdf.add_page()
    pdf.set_fill_color(*BLEU)
    pdf.rect(0, 0, pdf.w, pdf.h, style="F")
    pdf.set_text_color(*BLANC)

    def centre(txt, size, style="", top=None, h=None):
        if top is not None:
            pdf.set_y(top)
        pdf.set_x(pdf.l_margin)
        pdf.set_font("DejaVu", style, size)
        pdf.multi_cell(pdf.epw, h or (size * 0.5 + 2), txt, align="C")

    centre("Alex le CyberHero", 34, "B", top=70)
    pdf.ln(4)
    centre("Manuel d'apprentissage", 18)
    pdf.ln(2)
    centre("Comprendre la cyberdéfense en mots simples", 13, "I")
    pdf.set_draw_color(*BLANC); pdf.set_line_width(0.5)
    pdf.line(60, 150, pdf.w - 60, 150)
    centre("Préparé pour Alexandre", 13, top=160)
    centre("Avant l'entrée en Master Cybersécurité", 11)
    centre("8 chapitres pour débuter de zéro et arriver prêt.", 10, "I", top=pdf.h - 30)


def main():
    out = sys.argv[1]
    md_files = sys.argv[2:]
    full = ""
    for f in md_files:
        with open(f, encoding="utf-8") as fh:
            full += fh.read() + "\n\n"
    pdf = Manuel()
    cover(pdf)
    render(pdf, parse_blocks(full))
    pdf.output(out)
    print(f"PDF généré : {out} ({pdf.page_no()} pages)")


if __name__ == "__main__":
    main()
