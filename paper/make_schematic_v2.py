#!/usr/bin/env python3
"""Build docs/induction-furnace-schematic-v2.pptx from the v1 schematic.

Requested revisions (R. Guymon, PR #3, 2026-07-07):
  - drop the control-computer icon/label
  - show chiller water entering the heating head (coil is water-cooled)
  - make the right vertical support line fully solid (no dashed top section)
  - keep every word on one line (no mid-word wraps)
  - mount the heating head on a support
  - label the vacuum chamber stack
  - shrink the chiller and generator
"""
import copy, os, shutil
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO_ROOT, "docs", "induction-furnace-schematic.pptx")
DST = os.path.join(REPO_ROOT, "docs", "induction-furnace-schematic-v2.pptx")
shutil.copyfile(SRC, DST)

prs = Presentation(DST)
slide = prs.slides[0]
shapes = slide.shapes
by_id = {sh.shape_id: sh for sh in shapes}

def delete(sid):
    el = by_id[sid]._element
    el.getparent().remove(el)

def set_text(sh, lines, size, bold=False):
    tf = sh.text_frame
    tf.word_wrap = False
    tf.text = lines[0]
    for extra in lines[1:]:
        tf.add_paragraph().text = extra
    for para in tf.paragraphs:
        para.alignment = PP_ALIGN.CENTER
        for run in para.runs:
            run.font.size = Pt(size)
            run.font.bold = bold
            run.font.color.rgb = RGBColor(0, 0, 0)

def nowrap(sid, size=None):
    sh = by_id[sid]
    sh.text_frame.word_wrap = False
    if size is not None:
        for para in sh.text_frame.paragraphs:
            for run in para.runs:
                run.font.size = Pt(size)

def tail_arrow(sh, w="med", ln_="med"):
    ln = sh.line._get_or_add_ln()
    te = ln.makeelement(qn('a:tailEnd'), {'type': 'triangle', 'w': w, 'len': ln_})
    ln.append(te)

def style_line(sh, width_pt, rgb=RGBColor(0,0,0), dash=None):
    sh.line.color.rgb = rgb
    sh.line.width = Pt(width_pt)
    if dash is not None:
        ln = sh.line._get_or_add_ln()
        d = ln.makeelement(qn('a:prstDash'), {'val': dash})
        ln.append(d)

def label(text, l, t, w, size=10, align=PP_ALIGN.LEFT, rgb=None):
    tb = shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(0.26))
    tf = tb.text_frame
    tf.word_wrap = False
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.text = text
    p = tf.paragraphs[0]
    p.alignment = align
    for run in p.runs:
        run.font.size = Pt(size)
        if rgb is not None:
            run.font.color.rgb = rgb
    return tb

def leader(x1, y1, x2, y2):
    c = shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    style_line(c, 1.0)
    tail_arrow(c, w="sm", ln_="sm")
    return c

# ---- 1. remove control computer icon + label, old chiller<->gen arrows, old RF leads
for sid in (9, 137, 121, 122, 135, 136):
    delete(sid)

# ---- 2. right vertical line fully solid (was sysDot fixturing cable over the post)
ln35 = by_id[35]._element.find('.//' + qn('a:ln'))
for d in ln35.findall(qn('a:prstDash')):
    ln35.remove(d)

# ---- 3. shrink + reposition chiller and generator
ch = by_id[71]
ch.left, ch.top, ch.width, ch.height = Inches(0.60), Inches(8.50), Inches(1.50), Inches(0.95)
set_text(ch, ["Recirculating", "Water Chiller"], 11)
gen = by_id[72]
gen.left, gen.top, gen.width, gen.height = Inches(0.60), Inches(6.55), Inches(1.40), Inches(0.90)
set_text(gen, ["Induction", "Generator"], 11)

# ---- 4. RF leads: generator -> heating head (dotted, +/- polarity labels kept)
for y in (6.85, 7.15):
    c = shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(2.00), Inches(y), Inches(6.82), Inches(y))
    style_line(c, 2.0, dash='sysDot')
plus, minus = by_id[133], by_id[134]
plus.left, plus.top = Inches(2.04), Inches(6.48)
minus.left, minus.top = Inches(2.04), Inches(6.88)

# ---- 5. cooling-water loop: chiller -> heating head -> chiller
BLUE = RGBColor(0x1F, 0x6F, 0xC4)
def water(points):
    fb = shapes.build_freeform(Emu(Inches(points[0][0])), Emu(Inches(points[0][1])), scale=1.0)
    fb.add_line_segments([(Emu(Inches(x)), Emu(Inches(y))) for x, y in points[1:]], close=False)
    sh = fb.convert_to_shape()
    sh.fill.background()
    sh.shadow.inherit = False
    style_line(sh, 2.0, rgb=BLUE)
    tail_arrow(sh)
    return sh
water([(2.10, 8.70), (5.35, 8.70), (5.35, 7.75), (6.95, 7.75), (6.95, 7.31)])   # supply
water([(7.20, 7.31), (7.20, 7.95), (5.55, 7.95), (5.55, 9.00), (2.10, 9.00)])   # return
label("Cooling Water", 2.35, 8.38, 1.15, size=10, rgb=BLUE)

# ---- 6. heating-head support post, drawn behind the plumbing, standing on an
#         extension of the stand's base bar
post = shapes.add_shape(1, Inches(7.38), Inches(7.29), Inches(0.13), Inches(2.15))  # 1 = rectangle
post.fill.solid(); post.fill.fore_color.rgb = RGBColor(0xA6, 0xA6, 0xA6)
post.line.color.rgb = RGBColor(0, 0, 0); post.line.width = Pt(1.0)
post.shadow.inherit = False
spTree = post._element.getparent()
spTree.remove(post._element)
spTree.insert(2, post._element)   # first drawable -> everything else renders on top
foot = shapes.add_shape(1, Inches(7.28), Inches(9.435), Inches(0.90), Inches(0.055))
foot.fill.solid(); foot.fill.fore_color.rgb = RGBColor(0, 0, 0)
foot.line.fill.background()
foot.shadow.inherit = False
base = by_id[91]
base.left, base.width = Inches(7.28), Inches(2.50)
nowrap(91, 12)

# the support-stand group's upper post segments were dotted ("dashed section near
# the top" of an otherwise solid line) -- make the whole stand solid
grp = by_id[115]
for d in grp._element.findall('.//' + qn('a:prstDash')):
    d.getparent().remove(d)

# ---- 7. bellows text off the hose (support post would cross it)
by_id[14].text_frame.text = ""
label("Bellows", 5.72, 8.28, 0.70, size=10)

# ---- 8. single-line words everywhere
nowrap(11, 11)          # T-Station 85 (Pump)
nowrap(23, 12)          # Pyrometer (rotated)
nowrap(24, 9)           # Pressure Sensor
nowrap(25, 12)          # Pyrometer Holder
nowrap(26, 12)          # Quartz Disc
set_text(by_id[38], ["Fixturing Cable", "(with slack)"], 12)
set_text(by_id[70], ["Heating", "Head"], 11)

# ---- 9. crucible inside the quartz tube, at coil height
cru = shapes.add_shape(1, Inches(8.47), Inches(6.95), Inches(0.20), Inches(0.15))
cru.fill.solid(); cru.fill.fore_color.rgb = RGBColor(0x59, 0x59, 0x59)
cru.line.color.rgb = RGBColor(0, 0, 0); cru.line.width = Pt(0.75)
cru.shadow.inherit = False

# ---- 10. vacuum-stack labels with leader arrows
label("Quartz Tube (Vacuum Chamber)", 4.42, 6.33, 2.18, align=PP_ALIGN.RIGHT)
leader(6.65, 6.46, 8.40, 6.55)
label("KF40 Fitting", 9.02, 6.16, 0.95)
leader(9.00, 6.29, 8.74, 6.29)
label("Crucible", 9.05, 6.52, 0.85)
leader(9.03, 6.65, 8.66, 6.98)
label("Induction Coil", 9.02, 6.93, 0.95)
leader(9.00, 7.06, 8.77, 7.06)
label("KF40 Cross", 9.02, 7.80, 0.95)
leader(9.00, 7.93, 8.74, 7.93)

prs.save(DST)
print("saved", DST)
