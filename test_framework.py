import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# ==========================================
# CONSTANTS & COLOR PALETTE (Canva Cyber / Dark OS Theme)
# ==========================================
SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

# Colors
BG_DARK = RGBColor(11, 15, 25)          # Deep Navy/Black #0B0F19
BG_HEADER = RGBColor(8, 12, 20)        # Header background #080C14
CARD_BG = RGBColor(21, 29, 48)         # Card Dark Slate #151D30
CARD_BG_ALT = RGBColor(14, 21, 38)     # Secondary Card #0E1526
CARD_BORDER = RGBColor(36, 48, 72)     # Card Border #243048
CARD_BORDER_GLOW = RGBColor(56, 189, 248) # Electric Blue glow #38BDF8

TEXT_WHITE = RGBColor(248, 250, 252)   # Pure White #F8FAFC
TEXT_MUTED = RGBColor(148, 163, 184)   # Slate Muted #94A3B8
TEXT_DARK = RGBColor(15, 23, 42)       # Dark for badges #0F172A

CYAN_ELECTRIC = RGBColor(0, 229, 255)  # Electric Cyan #00E5FF
BLUE_PRIMARY = RGBColor(56, 189, 248)  # Primary Electric Blue #38BDF8
PURPLE_NEON = RGBColor(168, 85, 247)   # Neon Purple #A855F7
GREEN_SUCCESS = RGBColor(52, 211, 153) # Success Green #34D399
AMBER_WARNING = RGBColor(251, 191, 36) # Amber #FBBF24
PINK_ACCENT = RGBColor(236, 72, 153)   # Pink Accent #EC4899

FONT_TITLE = "Segoe UI"
FONT_BODY = "Segoe UI"
FONT_CODE = "Consolas"

def create_base_presentation():
    prs = Presentation()
    prs.slide_width = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT
    return prs

def set_slide_background(slide):
    # Add dark background rectangle covering whole slide
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_WIDTH, SLIDE_HEIGHT)
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_DARK
    bg.line.fill.background()
    return bg

def add_header(slide, title_text, category_text="OPERATING SYSTEMS PROJECT | PS NO. 80"):
    # Top decorative line
    top_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.04))
    top_line.fill.solid()
    top_line.fill.fore_color.rgb = CYAN_ELECTRIC
    top_line.line.fill.background()

    # Category badge
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.55), Inches(11.733), Inches(0.35))
    tf_cat = cat_box.text_frame
    tf_cat.word_wrap = True
    p_cat = tf_cat.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.name = FONT_BODY
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = BLUE_PRIMARY

    # Main Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.733), Inches(0.7))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.name = FONT_TITLE
    p_title.font.size = Pt(24)
    p_title.font.bold = True
    p_title.font.color.rgb = TEXT_WHITE

def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
    else:
        card.line.fill.background()
    return card

def add_badge(slide, text, left, top, width=Inches(1.8), height=Inches(0.35), bg_color=CARD_BORDER, text_color=CYAN_ELECTRIC):
    badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    badge.fill.solid()
    badge.fill.fore_color.rgb = bg_color
    badge.line.color.rgb = text_color
    badge.line.width = Pt(1)
    
    tf = badge.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.text = text
    p.font.name = FONT_BODY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = text_color
    p.alignment = PP_ALIGN.CENTER
    return badge

def add_bullet_list(text_frame, items, font_size=Pt(12), space_after=Pt(6)):
    for idx, item in enumerate(items):
        if idx == 0:
            p = text_frame.paragraphs[0]
        else:
            p = text_frame.add_paragraph()
        p.text = item
        p.font.name = FONT_BODY
        p.font.size = font_size
        p.font.color.rgb = TEXT_WHITE
        p.space_after = space_after
        p.level = 0

def add_speaker_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = notes_text.strip()

print("Presentation template framework loaded successfully.")
