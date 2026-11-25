import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# ==========================================
# CONSTANTS & THEME PALETTE
# High-tech Cyber / Dark OS Theme (Canva-inspired)
# ==========================================
SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

# Color Palette
BG_DARK = RGBColor(11, 15, 25)              # #0B0F19 - Deep Space Navy
CARD_BG = RGBColor(21, 29, 48)             # #151D30 - Elevated Dark Slate
CARD_BG_ALT = RGBColor(14, 21, 38)         # #0E1526 - Secondary Container
CARD_BORDER = RGBColor(36, 48, 72)         # #243048 - Crisp Subtle Border
BORDER_GLOW = RGBColor(56, 189, 248)       # #38BDF8 - Electric Blue Accent

TEXT_WHITE = RGBColor(248, 250, 252)       # #F8FAFC - Primary Text
TEXT_MUTED = RGBColor(148, 163, 184)       # #94A3B8 - Secondary Muted Text
TEXT_CYAN = RGBColor(0, 229, 255)          # #00E5FF - Highlighting Accent

COLOR_CYAN = RGBColor(0, 229, 255)         # Electric Cyan
COLOR_BLUE = RGBColor(56, 189, 248)        # Electric Blue
COLOR_PURPLE = RGBColor(168, 85, 247)      # Neon Purple
COLOR_GREEN = RGBColor(52, 211, 153)       # Emerald Green
COLOR_AMBER = RGBColor(251, 191, 36)       # Amber Gold
COLOR_PINK = RGBColor(236, 72, 153)        # Vibrant Pink

FONT_HEADING = "Segoe UI"
FONT_BODY = "Segoe UI"
FONT_CODE = "Consolas"

def create_presentation():
    prs = Presentation()
    prs.slide_width = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT
    blank_layout = prs.slide_layouts[6] # blank layout

    def new_slide():
        slide = prs.slides.add_slide(blank_layout)
        # Background shape
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_WIDTH, SLIDE_HEIGHT)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return slide

    def add_header(slide, title_text, cat_text="OPERATING SYSTEMS PROJECT | PS NO. 80"):
        # Top gradient accent strip
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.04))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = COLOR_CYAN
        top_bar.line.fill.background()

        # Category Tracker
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.52), Inches(11.733), Inches(0.3))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = cat_text.upper()
        p_cat.font.name = FONT_BODY
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_BLUE

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.733), Inches(0.65))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = FONT_HEADING
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER, border_width=1.5):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(border_width)
        else:
            card.line.fill.background()
        return card

    def add_badge(slide, text, left, top, width=Inches(1.8), height=Inches(0.35), bg_color=CARD_BG_ALT, border_color=COLOR_CYAN, text_color=COLOR_CYAN):
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        badge.fill.solid()
        badge.fill.fore_color.rgb = bg_color
        badge.line.color.rgb = border_color
        badge.line.width = Pt(1)
        tf = badge.text_frame
        tf.word_wrap = False
        p = tf.paragraphs[0]
        p.text = text
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = text_color
        p.alignment = PP_ALIGN.CENTER
        return badge

    def set_notes(slide, notes):
        ns = slide.notes_slide
        ns.notes_text_frame.text = notes.strip()

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    s1 = new_slide()
    # Hero glowing card in center
    add_card(s1, Inches(1.0), Inches(0.8), Inches(11.333), Inches(5.9), bg_color=CARD_BG, border_color=BORDER_GLOW, border_width=2)
    
    # Badges row
    add_badge(s1, "B.TECH CSE PROJECT DEMO", Inches(1.4), Inches(1.2), width=Inches(2.2), border_color=COLOR_CYAN, text_color=COLOR_CYAN)
    add_badge(s1, "OPERATING SYSTEMS (DSA)", Inches(3.8), Inches(1.2), width=Inches(2.2), border_color=COLOR_BLUE, text_color=COLOR_BLUE)
    add_badge(s1, "PROJECT PS NO. 80", Inches(6.2), Inches(1.2), width=Inches(1.8), border_color=COLOR_PURPLE, text_color=COLOR_PURPLE)

    # Title & Subtitle box
    t_box = s1.shapes.add_textbox(Inches(1.4), Inches(1.75), Inches(10.5), Inches(2.2))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    
    p_title = tf1.paragraphs[0]
    p_title.text = "CPU Scheduling Simulator"
    p_title.font.name = FONT_HEADING
    p_title.font.size = Pt(38)
    p_title.font.bold = True
    p_title.font.color.rgb = TEXT_WHITE
    p_title.space_after = Pt(10)

    p_sub = tf1.add_paragraph()
    p_sub.text = "Design, Analysis, and Implementation of Core OS Scheduling Algorithms & Interactive Visualizer"
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = COLOR_BLUE
    p_sub.space_after = Pt(8)

    p_desc = tf1.add_paragraph()
    p_desc.text = "Featuring Non-Preemptive Priority Scheduling, Round Robin with Dynamic Ready Queues, and Custom Data Structures"
    p_desc.font.name = FONT_BODY
    p_desc.font.size = Pt(13)
    p_desc.font.color.rgb = TEXT_MUTED

    # Bottom Metadata Grid (Student & Guide Info)
    m1 = add_card(s1, Inches(1.4), Inches(4.3), Inches(4.8), Inches(1.9), bg_color=CARD_BG_ALT, border_color=CARD_BORDER)
    tf_m1 = m1.text_frame
    tf_m1.margin_left = tf_m1.margin_top = Inches(0.2)
    p1 = tf_m1.paragraphs[0]
    p1.text = "PROJECT METADATA"
    p1.font.bold = True
    p1.font.size = Pt(11)
    p1.font.color.rgb = COLOR_CYAN
    p1.space_after = Pt(4)
    for line in [
        "University: Rungta International Skills University",
        "Department: School of Computer Science & Engineering",
        "Subject: Data Structures & Algorithms / Operating Systems",
        "Academic Session: 2026-2027 | Semester: V / VI"
    ]:
        p = tf_m1.add_paragraph()
        p.text = line
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_WHITE

    m2 = add_card(s1, Inches(6.5), Inches(4.3), Inches(5.4), Inches(1.9), bg_color=CARD_BG_ALT, border_color=CARD_BORDER)
    tf_m2 = m2.text_frame
    tf_m2.margin_left = tf_m2.margin_top = Inches(0.2)
    p2 = tf_m2.paragraphs[0]
    p2.text = "CANDIDATE & SUPERVISION DETAILS"
    p2.font.bold = True
    p2.font.size = Pt(11)
    p2.font.color.rgb = COLOR_PURPLE
    p2.space_after = Pt(4)
    for line in [
        "Student Name: Anugya Singh & Team",
        "Branch & Degree: B.Tech in Computer Science and Engineering",
        "Course Project ID: PS No. 80 (CPU Scheduling Simulator)",
        "Faculty Guide: Department of Computer Science & Engineering"
    ]:
        p = tf_m2.add_paragraph()
        p.text = line
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_WHITE

    set_notes(s1, """
Good morning respected examiners and faculty members.
Today, I am presenting our Operating Systems and Data Structures project: 'CPU Scheduling Simulator', designated under Problem Statement No. 80.
This presentation demonstrates the fundamental concepts of processor scheduling, the mathematical models governing process turnaround and waiting times, and the custom data structures—specifically a Singly Linked List with Merge Sort, an Array-based Circular Queue, and a Binary Min-Heap—built to achieve accurate simulation and real-time visualization.
""")

    # ==========================================
    # SLIDE 2: INTRODUCTION TO CPU SCHEDULING
    # ==========================================
    s2 = new_slide()
    add_header(s2, "Introduction to CPU Scheduling in Modern Operating Systems", "01. INTRODUCTION & CORE FOUNDATION")
    
    # 3 Horizontal Cards
    c1 = add_card(s2, Inches(0.8), Inches(1.6), Inches(3.64), Inches(4.4))
    tf_c1 = c1.text_frame
    tf_c1.margin_left = tf_c1.margin_right = tf_c1.margin_top = Inches(0.25)
    p = tf_c1.paragraphs[0]
    p.text = "WHAT IS CPU SCHEDULING?"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(12)
    for b in [
        "CPU Scheduling is the process by which the Operating System's Short-Term Scheduler decides which runnable process in memory gets CPU allocation.",
        "CPU execution alternates between CPU Bursts (active computation) and I/O Bursts (waiting for network, disk, or user input).",
        "The scheduler dispatches processes to maximize CPU activity while other processes await I/O operations."
    ]:
        p = tf_c1.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(8)

    c2 = add_card(s2, Inches(4.84), Inches(1.6), Inches(3.64), Inches(4.4))
    tf_c2 = c2.text_frame
    tf_c2.margin_left = tf_c2.margin_right = tf_c2.margin_top = Inches(0.25)
    p = tf_c2.paragraphs[0]
    p.text = "WHY IS IT REQUIRED?"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = COLOR_BLUE
    p.space_after = Pt(12)
    for b in [
        "Resource Optimization: Without scheduling, a single program waiting for slow disk I/O would leave expensive CPU cores completely idle.",
        "Throughput Maximization: Increases total work completed per unit time by keeping the execution pipeline saturated.",
        "Guaranteed Latency: Interactive applications require responsive context switching to ensure zero noticeable lag for end users."
    ]:
        p = tf_c2.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(8)

    c3 = add_card(s2, Inches(8.88), Inches(1.6), Inches(3.64), Inches(4.4))
    tf_c3 = c3.text_frame
    tf_c3.margin_left = tf_c3.margin_right = tf_c3.margin_top = Inches(0.25)
    p = tf_c3.paragraphs[0]
    p.text = "ROLE IN MULTITASKING"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = COLOR_PURPLE
    p.space_after = Pt(12)
    for b in [
        "Time-Sharing Illusion: Rapid preemption creates the perception of simultaneous execution of dozens of apps on a single CPU core.",
        "Fairness & Priority Enforcement: Prevents background tasks from starving foreground user interfaces.",
        "Determinism & Predictability: Provides real-time guarantees for critical kernel threads and hardware interrupt handlers."
    ]:
        p = tf_c3.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(8)

    # Bottom metric strip
    strip = add_card(s2, Inches(0.8), Inches(6.2), Inches(11.733), Inches(0.8), bg_color=CARD_BG_ALT, border_color=CARD_BORDER)
    tf_s = strip.text_frame
    tf_s.margin_left = Inches(0.3)
    tf_s.margin_top = Inches(0.15)
    p_s = tf_s.paragraphs[0]
    p_s.text = "CORE SCHEDULING OBJECTIVES:  Max CPU Utilization (100%)  |  Max Throughput  |  Min Turnaround Time  |  Min Waiting Time  |  Min Response Time"
    p_s.font.bold = True
    p_s.font.size = Pt(11)
    p_s.font.color.rgb = COLOR_CYAN

    set_notes(s2, """
In an operating system, the CPU is the most critical compute resource.
Historically, early batch systems ran one job to completion before loading the next. When a program executed I/O, the CPU sat idle.
CPU scheduling enables multiprogramming: by keeping multiple processes in memory, whenever the active process yields for I/O, the Short-Term Scheduler dispatches another ready process.
Modern desktop, mobile, and server OSes depend on sophisticated scheduling algorithms to balance high throughput with minimal user latency.
""")

    # ==========================================
    # SLIDE 3: PROBLEM STATEMENT (PS NO. 80)
    # ==========================================
    s3 = new_slide()
    add_header(s3, "Problem Statement: Managing Multi-Process Contention", "02. PROBLEM DEFINITION & CHALLENGES")

    # Left Card: The Resource Contention Dilemma
    p_left = add_card(s3, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.3))
    tf_pl = p_left.text_frame
    tf_pl.margin_left = tf_pl.margin_right = tf_pl.margin_top = Inches(0.3)
    p = tf_pl.paragraphs[0]
    p.text = "THE RESOURCE CONTENTION DILEMMA"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = COLOR_AMBER
    p.space_after = Pt(10)
    for b in [
        "Unpredictable Process Dynamics: In modern operating systems, processes arrive dynamically with varying burst lengths and urgent priority levels.",
        "Classical Pathologies Encountered:",
        "  - Convoy Effect: Short processes queued behind a massive CPU burst job (common in FCFS).",
        "  - Starvation (Indefinite Blocking): Lower-priority jobs never receive CPU time due to continuous higher-priority arrivals.",
        "  - Excessive Context Switch Overhead: Poorly chosen time quanta in Round Robin degrade performance through cache thrashing.",
        "No Universal Algorithm: Optimizing for average waiting time often degrades predictability and fairness, demanding configurable simulators."
    ]:
        p = tf_pl.add_paragraph()
        p.text = b
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(6)

    # Right Card: Project PS No. 80 University Mandate
    p_right = add_card(s3, Inches(6.8), Inches(1.6), Inches(5.733), Inches(5.3), border_color=BORDER_GLOW)
    tf_pr = p_right.text_frame
    tf_pr.margin_left = tf_pr.margin_right = tf_pr.margin_top = Inches(0.3)
    p = tf_pr.paragraphs[0]
    p.text = "PROJECT PS NO. 80 MANDATE & SPECIFICATION"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(10)
    for b in [
        "Project Scope: Develop a robust CPU Scheduling Simulator implementing Non-Preemptive Priority Scheduling and Preemptive Round Robin.",
        "Bare Minimum Academic Requirements:",
        "  1. Single-file Java Solution runnable directly from the command-line console.",
        "  2. Singly Linked List: All processes must be stored in a custom linked list and sorted by arrival time using a custom sorting method.",
        "  3. Array-based Circular Queue: Implement Round Robin ready queue strictly via an array circular buffer.",
        "  4. Min-Heap Priority Queue: Implement priority queue as a binary heap ordered by priority (lower number = higher priority).",
        "  5. Strict Input Validation: Reject negative arrival times and non-positive burst, priority, and quantum values.",
        "  6. Execution Outputs: Render Gantt chart timeline and compute exact Waiting Time (WT), Turnaround Time (TAT), and averages."
    ]:
        p = tf_pr.add_paragraph()
        p.text = b
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(5)

    set_notes(s3, """
Slide 3 outlines the fundamental problem and our university project scope.
In any multitasking computer, ready processes far outnumber available CPU cores. If processes are scheduled naively, severe system degradation occurs—such as the Convoy Effect or process starvation.
Problem Statement No. 80 requires us to build a simulator capable of scheduling processes under Priority and Round Robin schemes. Crucially, the assignment forbids using ready-made Java Collections like LinkedList or PriorityQueue for internal simulation, demanding that we engineer custom data structures from scratch.
""")

    # ==========================================
    # SLIDE 4: PROJECT OBJECTIVES
    # ==========================================
    s4 = new_slide()
    add_header(s4, "Project Objectives: Simulation, Calculation & Visualization", "03. PROJECT OBJECTIVES & DELIVERABLES")

    objs = [
        ("01. Algorithmic Simulation", "Simulate core scheduling disciplines with mathematical precision. Implement non-preemptive Priority Scheduling and preemptive Round Robin with configurable Time Quanta.", COLOR_CYAN),
        ("02. Custom Data Structures", "Design and verify custom Data Structures from first principles: Singly Linked List with Merge Sort, Array-based Circular Queue, and Binary Min-Heap.", COLOR_BLUE),
        ("03. Metrics Calculation Engine", "Accurately compute Completion Time (CT), Turnaround Time (TAT), and Waiting Time (WT) per process, along with overall system averages and CPU utilization.", COLOR_PURPLE),
        ("04. Dual-Interface Delivery", "Deliver a standalone interactive Console CLI application for academic evaluation alongside a high-performance modern Web Application for real-time visualization.", COLOR_GREEN),
    ]

    for idx, (title, desc, color) in enumerate(objs):
        x = Inches(0.8 + (idx % 2) * 5.95)
        y = Inches(1.6 + (idx // 2) * 2.65)
        c = add_card(s4, x, y, Inches(5.75), Inches(2.4), bg_color=CARD_BG, border_color=CARD_BORDER)
        tf = c.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(14)
        p.font.color.rgb = color
        p.space_after = Pt(8)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(11.5)
        p2.font.color.rgb = TEXT_WHITE

    set_notes(s4, """
Our project objectives are fourfold:
First, accurate algorithmic simulation of both non-preemptive and preemptive disciplines.
Second, implementing custom data structures to satisfy the university's strict bare-minimum requirements without relying on Java library abstractions.
Third, an automated mathematical metrics engine calculating completion, turnaround, and waiting times.
And fourth, providing dual delivery: a console executable for evaluation scripts and an interactive browser-based web dashboard.
""")

    # ==========================================
    # SLIDE 5: WORKING OF CPU SCHEDULING (WORKFLOW)
    # ==========================================
    s5 = new_slide()
    add_header(s5, "End-to-End Workflow: The 5-Stage Scheduling Lifecycle", "04. WORKFLOW & SYSTEM DYNAMICS")

    stages = [
        ("STAGE 1", "Process Arrival", "Processes enter system with PID, Arrival Time (AT), Burst Time (BT), and Priority.", COLOR_CYAN),
        ("STAGE 2", "Ready Queue Admission", "Sorted by arrival time and admitted into Ready Queue (Circular Queue / Min-Heap).", COLOR_BLUE),
        ("STAGE 3", "Dispatcher Allocation", "Short-term scheduler selects candidate with highest priority or next in round robin sequence.", COLOR_PURPLE),
        ("STAGE 4", "CPU Execution", "Process executes on CPU core. Track clock ticks and decrement remaining burst time.", COLOR_AMBER),
        ("STAGE 5", "Completion / Re-queue", "If remaining time > 0, re-queued behind new arrivals; if 0, marks CT and metrics finalized.", COLOR_GREEN)
    ]

    for idx, (stg, title, desc, col) in enumerate(stages):
        x = Inches(0.8 + idx * 2.4)
        y = Inches(1.6)
        card = add_card(s5, x, y, Inches(2.2), Inches(3.6), bg_color=CARD_BG, border_color=col)
        tf = card.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.15)
        
        p = tf.paragraphs[0]
        p.text = stg
        p.font.bold = True
        p.font.size = Pt(9.5)
        p.font.color.rgb = col
        p.space_after = Pt(4)

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.bold = True
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_WHITE
        p2.space_after = Pt(8)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(10)
        p3.font.color.rgb = TEXT_MUTED

    # Bottom Special Rule Box (Critical for PS No. 80)
    rule_box = add_card(s5, Inches(0.8), Inches(5.5), Inches(11.733), Inches(1.4), bg_color=CARD_BG_ALT, border_color=BORDER_GLOW)
    tf_r = rule_box.text_frame
    tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = Inches(0.2)
    p_r1 = tf_r.paragraphs[0]
    p_r1.text = "CRITICAL OPERATING SYSTEM RULE IMPLEMENTED IN PS NO. 80:"
    p_r1.font.bold = True
    p_r1.font.size = Pt(11)
    p_r1.font.color.rgb = COLOR_CYAN
    p_r1.space_after = Pt(4)

    p_r2 = tf_r.add_paragraph()
    p_r2.text = "“In Round Robin, a process that arrives while another process is running joins the ready queue BEFORE the currently running process is re-queued upon slice expiration.” This ensures strict FIFO arrival fairness and prevents starvation of newly arriving jobs."
    p_r2.font.size = Pt(10.5)
    p_r2.font.color.rgb = TEXT_WHITE

    set_notes(s5, """
Slide 5 breaks down the discrete event cycle inside our simulator:
Processes arrive at discrete timestamps. They are buffered into the Ready Queue.
The CPU dispatcher chooses the candidate according to the active algorithm.
Notice the highlighted rule at the bottom: In Round Robin, when a process exhausts its quantum, any new processes that arrived during that slice must enter the ready queue first before the preempted process is re-queued. This rule was specifically verified in Test Case 4.
""")

    # ==========================================
    # SLIDE 6: TYPES OF CPU SCHEDULING
    # ==========================================
    s6 = new_slide()
    add_header(s6, "Taxonomy: Preemptive vs. Non-Preemptive Scheduling", "05. SCHEDULING DISCIPLINES & TAXONOMY")

    c_non = add_card(s6, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2), border_color=COLOR_BLUE)
    tf_non = c_non.text_frame
    tf_non.margin_left = tf_non.margin_right = tf_non.margin_top = Inches(0.3)
    p = tf_non.paragraphs[0]
    p.text = "NON-PREEMPTIVE SCHEDULING"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_BLUE
    p.space_after = Pt(10)
    for line in [
        "Operating Mechanism: Once the CPU has been allocated to a process, the process holds the CPU until it terminates or voluntarily switches to the waiting state.",
        "Context Switching: Minimal. Switch occurs only upon job completion.",
        "Overhead: Extremely low CPU state-saving overhead.",
        "Response Time: Unpredictable. An interactive task can be blocked indefinitely by a long background task.",
        "Starvation Risk: Moderate to high if lower-priority processes wait behind high burst jobs.",
        "Algorithms: FCFS, Non-Preemptive SJF, Priority Scheduling (PS No. 80)."
    ]:
        p = tf_non.add_paragraph()
        p.text = "• " + line
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(6)

    c_pre = add_card(s6, Inches(6.8), Inches(1.6), Inches(5.733), Inches(5.2), border_color=COLOR_PURPLE)
    tf_pre = c_pre.text_frame
    tf_pre.margin_left = tf_pre.margin_right = tf_pre.margin_top = Inches(0.3)
    p = tf_pre.paragraphs[0]
    p.text = "PREEMPTIVE SCHEDULING"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_PURPLE
    p.space_after = Pt(10)
    for line in [
        "Operating Mechanism: The CPU can be forcibly reclaimed by the operating system based on timer interrupts or higher-priority arrivals.",
        "Context Switching: Frequent. Involves saving registers, Program Counter (PC), stack pointer, and memory management state.",
        "Overhead: Higher context switching overhead and cache invalidation.",
        "Response Time: Fast and highly predictable. Ideal for multi-user, time-shared graphical environments.",
        "Starvation Risk: Low in Round Robin (guaranteed time slices); potential in SRTF.",
        "Algorithms: Round Robin (PS No. 80), SRTF, Preemptive Priority."
    ]:
        p = tf_pre.add_paragraph()
        p.text = "• " + line
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(6)

    set_notes(s6, """
Slide 6 contrasts the two fundamental scheduling paradigms: Preemptive and Non-Preemptive.
In non-preemptive scheduling, once a process gets the CPU, it runs uninterrupted. This is simple and has near-zero overhead, but poor response times.
In preemptive scheduling, the OS uses hardware timer interrupts to pause a running process and switch context. This is essential for time-sharing systems like Linux and Windows, which our simulator replicates in Round Robin mode.
""")

    # ==========================================
    # SLIDE 7: ALGORITHM 1 - FCFS
    # ==========================================
    s7 = new_slide()
    add_header(s7, "Algorithm 1: First Come First Serve (FCFS)", "06. SCHEDULING ALGORITHMS | BASELINE")

    # Left card: Concept
    fcfs_left = add_card(s7, Inches(0.8), Inches(1.6), Inches(5.2), Inches(5.3))
    tf_fl = fcfs_left.text_frame
    tf_fl.margin_left = tf_fl.margin_right = tf_fl.margin_top = Inches(0.3)
    p = tf_fl.paragraphs[0]
    p.text = "WORKING PRINCIPLE & CHARACTERISTICS"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(10)
    for line in [
        "Principle: The process that requests the CPU first is allocated the CPU first using a strict FIFO queue.",
        "Type: Strictly Non-preemptive.",
        "Advantages:",
        "  - Easiest algorithm to understand and program.",
        "  - Minimal scheduling overhead and zero preemption complexity.",
        "Disadvantages:",
        "  - Average waiting time is often quite long.",
        "  - Highly vulnerable to the Convoy Effect: short processes wait behind a massive CPU burst process."
    ]:
        p = tf_fl.add_paragraph()
        p.text = line
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(5)

    # Right card: Numerical Walkthrough
    fcfs_right = add_card(s7, Inches(6.3), Inches(1.6), Inches(6.233), Inches(5.3), border_color=COLOR_BLUE)
    tf_fr = fcfs_right.text_frame
    tf_fr.margin_left = tf_fr.margin_right = tf_fr.margin_top = Inches(0.3)
    p = tf_fr.paragraphs[0]
    p.text = "NUMERICAL EXAMPLE & CONVOY EFFECT"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_BLUE
    p.space_after = Pt(8)
    for line in [
        "Processes: P1 (AT=0, BT=24), P2 (AT=0, BT=3), P3 (AT=0, BT=3)",
        "",
        "GANTT CHART TIMELINE:",
        " [   P1 (0 - 24 ms)   ] [ P2 (24-27) ] [ P3 (27-30) ]",
        "",
        "Calculation Breakdown:",
        " • Waiting Time (WT): P1 = 0 ms, P2 = 24 ms, P3 = 27 ms",
        " • Turnaround Time (TAT): P1 = 24 ms, P2 = 27 ms, P3 = 30 ms",
        " • Average Waiting Time = (0 + 24 + 27) / 3 = 17.0 ms",
        " • Average Turnaround Time = (24 + 27 + 30) / 3 = 27.0 ms",
        "",
        "Analysis: If arrival order were P2, P3, P1, Avg WT drops from 17.0 ms to just 3.0 ms! This mathematically demonstrates the Convoy Effect."
    ]:
        p = tf_fr.add_paragraph()
        p.text = line
        p.font.size = Pt(10.5)
        p.font.color.rgb = COLOR_CYAN if "GANTT" in line or "17.0" in line else TEXT_WHITE
        p.space_after = Pt(2)

    set_notes(s7, """
Slide 7 covers First Come First Serve.
While FCFS is conceptually simple, its average waiting time fluctuates wildly based on arrival order. In our worked example, P1 needs 24 milliseconds, causing P2 and P3 (which only need 3 ms each) to wait 24 and 27 ms. This is the classic Convoy Effect.
""")

    # ==========================================
    # SLIDE 8: ALGORITHM 2 - SJF (NON-PREEMPTIVE)
    # ==========================================
    s8 = new_slide()
    add_header(s8, "Algorithm 2: Shortest Job First (SJF - Non-Preemptive)", "07. SCHEDULING ALGORITHMS | BURST OPTIMIZATION")

    sjf_left = add_card(s8, Inches(0.8), Inches(1.6), Inches(5.2), Inches(5.3))
    tf_sl = sjf_left.text_frame
    tf_sl.margin_left = tf_sl.margin_right = tf_sl.margin_top = Inches(0.3)
    p = tf_sl.paragraphs[0]
    p.text = "WORKING PRINCIPLE & OPTIMALITY"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(10)
    for line in [
        "Principle: Associates each process with its CPU burst length. When CPU is available, process with shortest burst is assigned first.",
        "Type: Non-preemptive.",
        "Proven Optimality: SJF gives the minimum average waiting time for a given set of stationary processes.",
        "Major Practical Limitation: The OS cannot know the exact next CPU burst length in advance; it can only estimate it via exponential smoothing:",
        "  τ_(n+1) = α * t_n + (1 - α) * τ_n",
        "Starvation: Long jobs can starve if short jobs arrive continually."
    ]:
        p = tf_sl.add_paragraph()
        p.text = line
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(5)

    sjf_right = add_card(s8, Inches(6.3), Inches(1.6), Inches(6.233), Inches(5.3), border_color=COLOR_GREEN)
    tf_sr = sjf_right.text_frame
    tf_sr.margin_left = tf_sr.margin_right = tf_sr.margin_top = Inches(0.3)
    p = tf_sr.paragraphs[0]
    p.text = "NUMERICAL WORKED EXAMPLE"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_GREEN
    p.space_after = Pt(8)
    for line in [
        "Processes: P1 (AT=0, BT=7), P2 (AT=2, BT=4), P3 (AT=4, BT=1), P4 (AT=5, BT=4)",
        "",
        "GANTT CHART TIMELINE:",
        " [  P1 (0-7 ms)  ] [P3(7-8)] [  P2 (8-12)  ] [  P4 (12-16)  ]",
        "",
        "Execution Trace:",
        " • At t=0: Only P1 has arrived. P1 runs 0 to 7.",
        " • At t=7: P2 (BT 4), P3 (BT 1), P4 (BT 4) have arrived. Min is P3 (BT 1).",
        " • P3 runs 7 to 8. Then P2 runs 8 to 12. Finally P4 runs 12 to 16.",
        "",
        "Metrics Results:",
        " • P1: WT = 0, TAT = 7  |  P2: WT = 6, TAT = 10",
        " • P3: WT = 3, TAT = 4  |  P4: WT = 7, TAT = 11",
        " • Average Waiting Time = 4.00 ms  |  Avg TAT = 8.00 ms"
    ]:
        p = tf_sr.add_paragraph()
        p.text = line
        p.font.size = Pt(10.5)
        p.font.color.rgb = COLOR_GREEN if "GANTT" in line or "4.00" in line else TEXT_WHITE
        p.space_after = Pt(2)

    set_notes(s8, """
Slide 8 explains Shortest Job First.
SJF is mathematically optimal for minimizing average waiting time. However, in general-purpose computing, the OS cannot know future burst times with certainty, requiring statistical estimation. It is also prone to starvation for long jobs.
""")

    # ==========================================
    # SLIDE 9: ALGORITHM 3 - SRTF (PREEMPTIVE SJF)
    # ==========================================
    s9 = new_slide()
    add_header(s9, "Algorithm 3: Shortest Remaining Time First (SRTF)", "08. SCHEDULING ALGORITHMS | PREEMPTIVE VARIANT")

    srtf_left = add_card(s9, Inches(0.8), Inches(1.6), Inches(5.2), Inches(5.3))
    tf_srl = srtf_left.text_frame
    tf_srl.margin_left = tf_srl.margin_right = tf_srl.margin_top = Inches(0.3)
    p = tf_srl.paragraphs[0]
    p.text = "PREEMPTIVE SHORTEST-JOB DISCIPLINE"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(10)
    for line in [
        "Principle: Preemptive version of SJF. When a new process arrives with a remaining burst shorter than the current running process's remaining time, the running process is preempted.",
        "Optimality: Achieves the lowest possible average waiting time for dynamic arrival workloads.",
        "Trade-offs:",
        "  - Frequent context switching overhead when many short jobs arrive.",
        "  - Must track remaining burst times dynamically at every arrival tick.",
        "  - Severe starvation risk for lengthy compute jobs."
    ]:
        p = tf_srl.add_paragraph()
        p.text = line
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(6)

    srtf_right = add_card(s9, Inches(6.3), Inches(1.6), Inches(6.233), Inches(5.3), border_color=COLOR_PURPLE)
    tf_srr = srtf_right.text_frame
    tf_srr.margin_left = tf_srr.margin_right = tf_srr.margin_top = Inches(0.3)
    p = tf_srr.paragraphs[0]
    p.text = "NUMERICAL WORKED EXAMPLE WITH PREEMPTION"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_PURPLE
    p.space_after = Pt(8)
    for line in [
        "Processes: P1 (AT=0, BT=8), P2 (AT=1, BT=4), P3 (AT=2, BT=9), P4 (AT=3, BT=5)",
        "",
        "GANTT CHART TIMELINE:",
        " [P1:0-1] [ P2: 1-5 ms ] [ P4: 5-10 ms ] [ P1: 10-17 ms ] [ P3: 17-26 ms ]",
        "",
        "Preemption Event at t = 1 ms:",
        " • P1 executed from 0 to 1 ms (remaining BT = 7).",
        " • P2 arrives at t=1 with BT = 4. Since 4 < 7, P1 is PREEMPTED and P2 takes the CPU.",
        "",
        "Metrics Results:",
        " • P1: WT = 9 ms, TAT = 17 ms  |  P2: WT = 0 ms, TAT = 4 ms",
        " • P3: WT = 15 ms, TAT = 24 ms |  P4: WT = 2 ms, TAT = 7 ms",
        " • Average Waiting Time = 6.50 ms  |  Avg TAT = 13.00 ms"
    ]:
        p = tf_srr.add_paragraph()
        p.text = line
        p.font.size = Pt(10.5)
        p.font.color.rgb = COLOR_PURPLE if "GANTT" in line or "PREEMPTED" in line else TEXT_WHITE
        p.space_after = Pt(2)

    set_notes(s9, """
Slide 9 covers Shortest Remaining Time First.
Notice the preemption at timestamp 1 ms: P1 is running, but P2 arrives with a burst of 4 ms, which is less than P1's remaining 7 ms. The scheduler preempts P1 and gives the CPU to P2. This reduces average wait time to 6.5 ms.
""")

    # ==========================================
    # SLIDE 10: ALGORITHM 4 - PRIORITY SCHEDULING (PS NO. 80 IMPLEMENTED)
    # ==========================================
    s10 = new_slide()
    add_header(s10, "Algorithm 4: Priority Scheduling (Non-Preemptive - Implemented)", "09. IMPLEMENTED ALGORITHMS | MIN-HEAP SCHEDULER")

    pri_left = add_card(s10, Inches(0.8), Inches(1.6), Inches(5.2), Inches(5.3))
    tf_prl = pri_left.text_frame
    tf_prl.margin_left = tf_prl.margin_right = tf_prl.margin_top = Inches(0.3)
    p = tf_prl.paragraphs[0]
    p.text = "DESIGN & MIN-HEAP IMPLEMENTATION"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(8)
    for line in [
        "Priority Assignment: Each process has an integer priority. In our university specification, LOWER integer = HIGHER priority (e.g., Priority 1 > Priority 3).",
        "Ready Queue Architecture: Engineered using a binary Min-Heap (`PriorityHeap`). Processes that have arrived are pushed to the heap; root extraction yields highest priority.",
        "Non-Preemptive Discipline: Once assigned the CPU, the process executes its entire burst.",
        "Tie-Breaking Rule: In case of identical priority, tie is broken by earlier arrival time and entry order.",
        "Starvation Solution: In real operating systems, 'Aging' gradually increments priority of waiting processes over time."
    ]:
        p = tf_prl.add_paragraph()
        p.text = line
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(5)

    pri_right = add_card(s10, Inches(6.3), Inches(1.6), Inches(6.233), Inches(5.3), border_color=BORDER_GLOW)
    tf_prr = pri_right.text_frame
    tf_prr.margin_left = tf_prr.margin_right = tf_prr.margin_top = Inches(0.3)
    p = tf_prr.paragraphs[0]
    p.text = "OFFICIAL UNIVERSITY TEST CASE 1 VERIFICATION"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(8)
    for line in [
        "Input Processes: P1 (AT 0, BT 3, Pr 3), P2 (AT 1, BT 2, Pr 1), P3 (AT 2, BT 1, Pr 2)",
        "",
        "GANTT CHART GENERATED:",
        " P1(0-3) P2(3-5) P3(5-6)",
        "",
        "Step-by-Step Mathematical Trace:",
        " • At t=0: Only P1 is ready. P1 executes 0 to 3 ms non-preemptively.",
        " • At t=3: P2 (Pr 1) and P3 (Pr 2) are in heap. Min-Heap extracts P2 (Pr 1).",
        " • P2 executes 3 to 5 ms. At t=5, P3 executes 5 to 6 ms.",
        "",
        "Exact Output Matching Project Sheet:",
        " • WT: P1 0, P2 2, P3 3  |  TAT: P1 3, P2 4, P3 4",
        " • Avg WT: 1.67 ms  |  Avg TAT: 3.67 ms",
        " • STATUS: 100% MATHEMATICAL MATCH (PASSED)"
    ]:
        p = tf_prr.add_paragraph()
        p.text = line
        p.font.size = Pt(10.5)
        p.font.color.rgb = COLOR_CYAN if "GANTT" in line or "PASSED" in line else TEXT_WHITE
        p.space_after = Pt(2)

    set_notes(s10, """
Slide 10 details Priority Scheduling, which we implemented directly in PS No. 80 using a custom Min-Heap.
Notice the verification of Test Case 1 from our project sheet: P1 runs from 0 to 3 because it arrived first. Even though P2 has priority 1 and P3 has priority 2, P1 is non-preemptive. At time 3, our Min-Heap extracts P2 because Priority 1 is higher than Priority 2.
The computed average waiting time of 1.67 ms and turnaround time of 3.67 ms match the university test sheet exactly.
""")

    # ==========================================
    # SLIDE 11: ALGORITHM 5 - ROUND ROBIN (PS NO. 80 IMPLEMENTED)
    # ==========================================
    s11 = new_slide()
    add_header(s11, "Algorithm 5: Round Robin Scheduling (Circular Queue - Implemented)", "10. IMPLEMENTED ALGORITHMS | CIRCULAR QUEUE SCHEDULER")

    rr_left = add_card(s11, Inches(0.8), Inches(1.6), Inches(5.2), Inches(5.3))
    tf_rl = rr_left.text_frame
    tf_rl.margin_left = tf_rl.margin_right = tf_rl.margin_top = Inches(0.3)
    p = tf_rl.paragraphs[0]
    p.text = "DESIGN & CIRCULAR QUEUE DISCIPLINE"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_BLUE
    p.space_after = Pt(8)
    for line in [
        "Principle: Designed specifically for time-sharing systems. Each ready process is allocated a fixed slice of CPU time called Time Quantum (Q).",
        "Preemption: If a process does not finish within Q, the CPU preempts it, and it returns to the tail of the ready queue.",
        "Circular Queue Architecture: Built using our custom array-based `CircularQueue` with modulo arithmetic pointers `(rear + 1) % capacity`.",
        "Core PS No. 80 Rule: When a running process is preempted, any new processes arriving during that quantum join the ready queue BEFORE the running process is re-queued.",
        "Quantum Sensitivity: Too small = excessive context switching overhead; too large = degenerates into FCFS."
    ]:
        p = tf_rl.add_paragraph()
        p.text = line
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(5)

    rr_right = add_card(s11, Inches(6.3), Inches(1.6), Inches(6.233), Inches(5.3), border_color=COLOR_PURPLE)
    tf_rr = rr_right.text_frame
    tf_rr.margin_left = tf_rr.margin_right = tf_rr.margin_top = Inches(0.3)
    p = tf_rr.paragraphs[0]
    p.text = "OFFICIAL UNIVERSITY TEST CASE 4 VERIFICATION"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_PURPLE
    p.space_after = Pt(8)
    for line in [
        "Input Scenario: P2 (AT 1, BT 3) entered 1st, P1 (AT 0, BT 4), Quantum Q = 2",
        "Linked List Sorting by Arrival: Correctly sorted as P1, P2.",
        "",
        "GANTT CHART GENERATED:",
        " P1(0-2) P2(2-4) P1(4-6) P2(6-7)",
        "",
        "Queue Event Trace:",
        " • t=0: P1 enters queue. P1 executes 0-2 ms (rem BT = 2).",
        " • t=1: P2 arrives during P1's slice -> P2 enters queue BEFORE P1 re-queues!",
        " • t=2: Queue is [P2, P1]. P2 runs 2-4 ms (rem BT = 1). Re-queues: [P1, P2].",
        " • t=4: P1 runs 4-6 ms (completes!). t=6: P2 runs 6-7 ms (completes!).",
        "",
        "Exact Output Matching Project Sheet:",
        " • P1: WT 2, TAT 6  |  P2: WT 3, TAT 6",
        " • Avg WT: 2.5 ms  |  Avg TAT: 6.0 ms  |  STATUS: PASSED (100%)"
    ]:
        p = tf_rr.add_paragraph()
        p.text = line
        p.font.size = Pt(10.5)
        p.font.color.rgb = COLOR_PURPLE if "GANTT" in line or "PASSED" in line else TEXT_WHITE
        p.space_after = Pt(2)

    set_notes(s11, """
Slide 11 highlights Round Robin scheduling with Time Quantum 2.
Here, we demonstrate compliance with the university's exact Test Case 4: Notice that P2 was entered first in input, but our Singly Linked List sorted them by arrival: P1 then P2.
At time 2, P2 entered the queue ahead of P1 being re-queued. The resulting Gantt chart P1(0-2) P2(2-4) P1(4-6) P2(6-7) and averages of 2.5 ms WT and 6.0 ms TAT match the university specification to the decimal place.
""")

    # ==========================================
    # SLIDE 12: CORE IMPLEMENTATION - CUSTOM DATA STRUCTURES
    # ==========================================
    s12 = new_slide()
    add_header(s12, "Core Implementation: Custom Data Structures (Req #2, #3, #4)", "11. DATA STRUCTURES & ALGORITHMIC RIGOR")

    ds_items = [
        ("ProcessLinkedList with Custom Merge Sort", "Bare Minimum Req #2", [
            "Stores all submitted processes in individual `ProcessNode` objects.",
            "Implements custom Merge Sort on Singly Linked List (no Arrays.sort).",
            "Uses slow and fast pointers to split list at midpoint in O(n).",
            "Recursively sorts and merges with O(n log n) stable arrival ordering."
        ], COLOR_CYAN),
        ("Array-Based Circular Queue (`CircularQueue`)", "Bare Minimum Req #3", [
            "Fixed-capacity array with `front`, `rear`, and `count` pointers.",
            "Wraps around seamlessly using modulo arithmetic: (rear + 1) % cap.",
            "Dynamic resize helper doubles capacity while preserving circular order.",
            "Enforces arrival insertion prior to running process re-queueing."
        ], COLOR_BLUE),
        ("Binary Min-Heap Priority Queue (`PriorityHeap`)", "Bare Minimum Req #4", [
            "Array-based binary heap for arrived processes awaiting CPU.",
            "Children at 2i + 1, 2i + 2; Parent at (i - 1) / 2.",
            "Implements `heapifyUp()` and `heapifyDown()` in O(log n) time.",
            "Enforces: Lower integer = higher priority, with stable tie-breaker."
        ], COLOR_PURPLE)
    ]

    for idx, (title, tag, bullets, col) in enumerate(ds_items):
        x = Inches(0.8 + idx * 3.95)
        y = Inches(1.6)
        card = add_card(s12, x, y, Inches(3.8), Inches(5.3), border_color=col)
        tf = card.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)
        
        # Tag
        add_badge(s12, tag, x + Inches(0.2), y + Inches(0.2), width=Inches(2.2), border_color=col, text_color=col)

        p = tf.paragraphs[0]
        p.text = "\n\n" + title
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(10)

        for b in bullets:
            p2 = tf.add_paragraph()
            p2.text = "• " + b
            p2.font.size = Pt(10.5)
            p2.font.color.rgb = TEXT_MUTED
            p2.space_after = Pt(6)

    set_notes(s12, """
Slide 12 is critical for the viva examination.
The faculty specifically mandated: 'Store all processes in a singly linked list and sort it using your own sorting method', 'implement the Round Robin ready queue as an array-based circular queue', and 'implement Priority Scheduling using a priority queue (heap)'.
We wrote all three from scratch in Java without importing java.util.LinkedList or java.util.PriorityQueue.
""")

    # ==========================================
    # SLIDE 13: PERFORMANCE METRICS & FORMULAS
    # ==========================================
    s13 = new_slide()
    add_header(s13, "Performance Metrics: Mathematical Formulations & Definitions", "12. MATHEMATICAL MODEL & EVALUATION")

    metrics = [
        ("Arrival Time (AT)", "The timestamp when a process enters the ready queue and is available for CPU scheduling.", "Unit: milliseconds (ms)"),
        ("Burst Time (BT)", "Total CPU time required by the process to execute completely.", "Unit: milliseconds (ms)"),
        ("Completion Time (CT)", "The clock timestamp when the process finishes its final instruction.", "CT = Final End Timestamp"),
        ("Turnaround Time (TAT)", "Total elapsed time from process arrival to complete execution.", "TAT = Completion Time - Arrival Time"),
        ("Waiting Time (WT)", "Total time spent by a process waiting in the ready queue for CPU allocation.", "WT = Turnaround Time - Burst Time"),
        ("CPU Utilization & Averages", "Overall fraction of time CPU was actively processing workloads.", "Avg WT = Σ WT / n  |  Util = (Busy/Makespan)*100")
    ]

    for idx, (m_title, m_desc, m_formula) in enumerate(metrics):
        x = Inches(0.8 + (idx % 3) * 3.95)
        y = Inches(1.6 + (idx // 3) * 2.65)
        c = add_card(s13, x, y, Inches(3.8), Inches(2.4), bg_color=CARD_BG, border_color=CARD_BORDER)
        tf = c.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
        
        p = tf.paragraphs[0]
        p.text = m_title
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = COLOR_CYAN
        p.space_after = Pt(6)

        p2 = tf.add_paragraph()
        p2.text = m_desc
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_WHITE
        p2.space_after = Pt(8)

        p3 = tf.add_paragraph()
        p3.text = m_formula
        p3.font.name = FONT_CODE
        p3.font.bold = True
        p3.font.size = Pt(10.5)
        p3.font.color.rgb = COLOR_BLUE

    set_notes(s13, """
Slide 13 provides the formal mathematical definitions.
Turnaround Time measures total residency: from the instant of arrival to completion.
Waiting Time isolates queueing delays: Turnaround Time minus Burst Time.
These two metrics, along with CPU utilization, form the primary benchmark figures of merit across all scheduling algorithms.
""")

    # ==========================================
    # SLIDE 14: SYSTEM ARCHITECTURE
    # ==========================================
    s14 = new_slide()
    add_header(s14, "System Architecture: End-to-End Pipeline & Component Flow", "13. ARCHITECTURE & SUBSYSTEM PIPELINE")

    pipeline_cards = [
        ("1. Presentation Tier", "Dual Interface:\n• Web UI (HTML5/CSS3/JS)\n• Console Terminal CLI\n• Preset Test Case Loaders", COLOR_CYAN),
        ("2. Ingestion & Validation", "Validation Subsystem:\n• Rejects AT < 0\n• Rejects BT <= 0\n• Rejects Priority <= 0\n• Rejects Quantum <= 0", COLOR_BLUE),
        ("3. Custom Data Tier", "Core Structures:\n• Singly Linked List\n• Merge Sort on Nodes\n• Circular Array Queue\n• Binary Min-Heap", COLOR_PURPLE),
        ("4. Scheduling Engine", "Simulation Core:\n• schedulePriority()\n• scheduleRoundRobin()\n• Discrete Clock Tick\n• State Snapshot Logs", COLOR_AMBER),
        ("5. Output Generation", "Results Formatter:\n• Gantt Timeline Blocks\n• Metric Math Engine\n• Per-Process WT/TAT\n• JSON API Responses", COLOR_GREEN)
    ]

    for idx, (title, content, col) in enumerate(pipeline_cards):
        x = Inches(0.8 + idx * 2.4)
        y = Inches(1.8)
        c = add_card(s14, x, y, Inches(2.2), Inches(4.8), bg_color=CARD_BG, border_color=col)
        tf = c.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.18)
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = col
        p.space_after = Pt(10)

        p2 = tf.add_paragraph()
        p2.text = content
        p2.font.size = Pt(10)
        p2.font.color.rgb = TEXT_WHITE

    set_notes(s14, """
Slide 14 maps out our 5-tier architecture.
The presentation layer accepts user input either from the web or terminal.
The validation layer guarantees data hygiene.
The data structure tier organizes processes into the linked list and active ready queues.
The simulation engine executes the schedule tick-by-tick.
Finally, the output tier builds the Gantt chart and computes averages.
""")

    # ==========================================
    # SLIDE 15: TECHNOLOGY STACK
    # ==========================================
    s15 = new_slide()
    add_header(s15, "Technology Stack: Zero-Dependency High-Efficiency Tooling", "14. TECHNOLOGY & IMPLEMENTATION STACK")

    tech_items = [
        ("Core Language: Java 21 / OpenJDK", [
            "Single-File Architecture: Entire Java solution encapsulated in `CpuSchedulingSimulator.java` for effortless compilation.",
            "Object-Oriented Design: Encapsulated `Process`, `ProcessNode`, `ProcessLinkedList`, `CircularQueue`, and `PriorityHeap`.",
            "Zero External JARs: Completely independent of third-party libraries (no Spring Boot, no external JSON libraries needed)."
        ], COLOR_CYAN),
        ("Embedded HTTP Server: com.sun.net.httpserver", [
            "Native JDK Server: Uses Java's built-in `HttpServer` to host REST endpoints on port 8080.",
            "REST Endpoints: `/api/simulate` handles JSON simulation requests; `/api/testcases` serves standard test payloads.",
            "CORS & Static Asset Serving: Serves modern web assets directly from disk or embedded fallback."
        ], COLOR_BLUE),
        ("Frontend: Modern HTML5 & CSS3", [
            "Cyber / Dark Theme: Styled with CSS Variables, Flexbox, and CSS Grid matching modern engineering dashboards.",
            "Responsive Gantt Visualizer: SVG and CSS flexbox timeline scaling dynamically to process burst durations.",
            "Typography: Google Fonts `Inter` for clean UI typography and `Fira Code` for monospace terminal outputs."
        ], COLOR_PURPLE),
        ("Client Engine: Vanilla JavaScript (ES6+)", [
            "Dual-Mode Simulation: Capable of running simulation client-side completely offline or querying Java backend.",
            "Interactive Queue Animator: Step-by-step playback controller with Play, Pause, and Step Next/Prev buttons.",
            "Zero Framework Bloat: No React, Vue, or Angular dependencies—ensures instant launch on any device."
        ], COLOR_GREEN)
    ]

    for idx, (title, bullets, col) in enumerate(tech_items):
        x = Inches(0.8 + (idx % 2) * 5.95)
        y = Inches(1.6 + (idx // 2) * 2.65)
        c = add_card(s15, x, y, Inches(5.75), Inches(2.4), bg_color=CARD_BG, border_color=CARD_BORDER)
        tf = c.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.22)
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = col
        p.space_after = Pt(6)

        for b in bullets:
            p2 = tf.add_paragraph()
            p2.text = "• " + b
            p2.font.size = Pt(10)
            p2.font.color.rgb = TEXT_WHITE
            p2.space_after = Pt(4)

    set_notes(s15, """
Slide 15 emphasizes our zero-dependency engineering strategy.
Rather than pulling in heavy web frameworks or bulky packages, we utilized standard Java 21 and Vanilla HTML5/CSS3/JavaScript.
This ensures our project is 100% portable: any examiner can compile and run `CpuSchedulingSimulator.java` with a single command without worrying about missing maven dependencies or npm install failures.
""")

    # ==========================================
    # SLIDE 16: PROJECT IMPLEMENTATION
    # ==========================================
    s16 = new_slide()
    add_header(s16, "Project Implementation: Execution Flow & Code Mechanics", "15. CODE IMPLEMENTATION & MECHANICS")

    steps = [
        ("Step 1: Input Ingestion", "Process instances are collected via console Scanner or Web Table with ID, Arrival Time, Burst Time, and Priority.", COLOR_CYAN),
        ("Step 2: Validation Check", "Sanity engine validates inputs. If BT <= 0, AT < 0, or Pr <= 0, execution halts with the exact assignment error text.", COLOR_BLUE),
        ("Step 3: Linked List Sorting", "All valid processes enter `ProcessLinkedList` and are sorted stably by Arrival Time using Merge Sort.", COLOR_PURPLE),
        ("Step 4: Queue Event Ticks", "Discrete clock progresses: arrived jobs enter heap or circular queue; dispatcher runs active job for burst or quantum.", COLOR_AMBER),
        ("Step 5: Metric Computation", "Clock marks CT when burst hits 0. Calculates TAT = CT - AT, WT = TAT - BT, averages, and builds Gantt string.", COLOR_GREEN)
    ]

    for idx, (step_title, step_desc, col) in enumerate(steps):
        y = Inches(1.6 + idx * 1.05)
        c = add_card(s16, Inches(0.8), y, Inches(11.733), Inches(0.9), bg_color=CARD_BG, border_color=CARD_BORDER)
        tf = c.text_frame
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.12)
        
        p = tf.paragraphs[0]
        p.text = step_title
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = col
        
        p2 = tf.add_paragraph()
        p2.text = step_desc
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_WHITE

    set_notes(s16, """
Slide 16 details the code execution sequence:
First, processes are ingested. Second, validation rules reject invalid numbers.
Third, our custom Merge Sort arranges the singly linked list in arrival order.
Fourth, the clock ticks forward, managing queue admissions, preemption, and completion.
Fifth, metrics are computed and formatted into the exact output format.
""")

    # ==========================================
    # SLIDE 17: USER INTERFACE & DASHBOARD ARCHITECTURE
    # ==========================================
    s17 = new_slide()
    add_header(s17, "User Interface & Dashboard Architecture", "16. INTERACTIVE VISUALIZER & UI ARCHITECTURE")

    # Wireframe Top Bar
    add_card(s17, Inches(0.8), Inches(1.5), Inches(11.733), Inches(0.7), bg_color=CARD_BG_ALT, border_color=COLOR_CYAN)
    add_badge(s17, "TEST CASE 1 (Priority)", Inches(1.0), Inches(1.65), width=Inches(2.4), border_color=COLOR_CYAN, text_color=COLOR_CYAN)
    add_badge(s17, "TEST CASE 2 (Single)", Inches(3.6), Inches(1.65), width=Inches(2.2), border_color=COLOR_BLUE, text_color=COLOR_BLUE)
    add_badge(s17, "TEST CASE 3 (Invalid)", Inches(6.0), Inches(1.65), width=Inches(2.2), border_color=COLOR_AMBER, text_color=COLOR_AMBER)
    add_badge(s17, "TEST CASE 4 (Round Robin)", Inches(8.4), Inches(1.65), width=Inches(2.4), border_color=COLOR_PURPLE, text_color=COLOR_PURPLE)

    # Wireframe Left Panel (Inputs)
    left_ui = add_card(s17, Inches(0.8), Inches(2.35), Inches(4.5), Inches(4.6), bg_color=CARD_BG, border_color=CARD_BORDER)
    tf_lui = left_ui.text_frame
    tf_lui.margin_left = tf_lui.margin_top = Inches(0.2)
    p = tf_lui.paragraphs[0]
    p.text = "CONFIGURATION & PROCESS TABLE"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_CYAN
    for item in [
        "",
        "• Algorithm Toggle: [Priority] | [Round Robin]",
        "• Time Quantum Input: Configurable in ms",
        "• Interactive Table:",
        "    PID   | Arrival | Burst | Priority | Action",
        "    P1    |   0 ms  |  3 ms |    3     |   [X] ",
        "    P2    |   1 ms  |  2 ms |    1     |   [X] ",
        "    P3    |   2 ms  |  1 ms |    2     |   [X] ",
        "",
        "• Controls: [+ Add Process]  |  [Clear All]",
        "• Primary Action: [ ▶ RUN SIMULATION ]"
    ]:
        p = tf_lui.add_paragraph()
        p.text = item
        p.font.name = FONT_CODE if "PID" in item or "P1" in item else FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = TEXT_WHITE

    # Wireframe Right Panel (Outputs)
    right_ui = add_card(s17, Inches(5.5), Inches(2.35), Inches(7.033), Inches(4.6), bg_color=CARD_BG, border_color=BORDER_GLOW)
    tf_rui = right_ui.text_frame
    tf_rui.margin_left = tf_rui.margin_top = Inches(0.2)
    p = tf_rui.paragraphs[0]
    p.text = "GANTT TIMELINE, QUEUE ANIMATOR & METRICS"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_BLUE
    for item in [
        "",
        "• Visual Gantt Chart Timeline (Scaled colored blocks):",
        "    [ P1 (0 - 3 ms) ] [ P2 (3 - 5 ms) ] [ P3 (5 - 6 ms) ]",
        "",
        "• Exact Formatted Console String Output:",
        "    Gantt: P1(0-3) P2(3-5) P3(5-6)",
        "    WT: P1 0, P2 2, P3 3 | TAT: P1 3, P2 4, P3 4",
        "    Avg WT: 1.67 | Avg TAT: 3.67",
        "",
        "• Queue State Visualizer (Array Circular Queue / Min-Heap):",
        "    State at t=3 ms: [ P2(Pr 1), P3(Pr 2) ]  Controls: [Play] [Next] [Prev]",
        "",
        "• Performance Summary Cards:",
        "    Avg WT: 1.67 ms | Avg TAT: 3.67 ms | CPU Util: 100% | Makespan: 6 ms"
    ]:
        p = tf_rui.add_paragraph()
        p.text = item
        p.font.name = FONT_CODE if "Gantt:" in item or "P1 (" in item else FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = COLOR_CYAN if "Gantt:" in item else TEXT_WHITE

    set_notes(s17, """
Slide 17 illustrates the user interface layout of our web application.
The top bar provides one-click presets for all mandatory university test cases.
The left column handles dynamic process insertion and algorithm selection.
The right column renders the real-time visual Gantt chart, the exact console strings, and the step-by-step queue state animator.
""")

    # ==========================================
    # SLIDE 18: SAMPLE EXECUTION & TEST VERIFICATION
    # ==========================================
    s18 = new_slide()
    add_header(s18, "Sample Execution: Verification of University Test Cases", "17. TEST RESULTS & MATHEMATICAL PROOF")

    t1_box = add_card(s18, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), border_color=COLOR_CYAN)
    tf_t1 = t1_box.text_frame
    tf_t1.margin_left = tf_t1.margin_right = tf_t1.margin_top = Inches(0.25)
    p = tf_t1.paragraphs[0]
    p.text = "TEST CASE 1: PRIORITY (NORMAL INPUT)"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(6)
    for line in [
        "Algorithm: Non-Preemptive Priority",
        "Inputs: P1 (AT 0, BT 3, Pr 3), P2 (AT 1, BT 2, Pr 1), P3 (AT 2, BT 1, Pr 2)",
        "",
        "Expected vs Actual Output:",
        "  Gantt Chart : P1(0-3) P2(3-5) P3(5-6)",
        "  Waiting Time: P1 0, P2 2, P3 3",
        "  Turnaround  : P1 3, P2 4, P3 4",
        "  Avg WT      : 1.67 ms (Expected: 1.67 ms)",
        "  Avg TAT     : 3.67 ms (Expected: 3.67 ms)",
        "",
        "TEST CASE 2: SINGLE PROCESS BOUNDARY",
        "Input : P1 (AT 0, BT 4, Pr 1)",
        "Output: Gantt: P1(0-4) | P1: WT 0, TAT 4",
        "Avg WT: 0.0 ms | Avg TAT: 4.0 ms (PASSED)",
        "",
        "STATUS: VERIFIED & 100% ACCURATE"
    ]:
        p = tf_t1.add_paragraph()
        p.text = line
        p.font.name = FONT_CODE if "Gantt" in line or "Avg" in line else FONT_BODY
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_CYAN if "STATUS" in line or "1.67" in line else TEXT_WHITE

    t4_box = add_card(s18, Inches(6.8), Inches(1.6), Inches(5.733), Inches(5.3), border_color=COLOR_PURPLE)
    tf_t4 = t4_box.text_frame
    tf_t4.margin_left = tf_t4.margin_right = tf_t4.margin_top = Inches(0.25)
    p = tf_t4.paragraphs[0]
    p.text = "TEST CASE 4: ROUND ROBIN (QUANTUM 2)"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_PURPLE
    p.space_after = Pt(6)
    for line in [
        "Algorithm: Round Robin (Quantum Q = 2)",
        "Input Entered: P2 (AT 1, BT 3) entered 1st, P1 (AT 0, BT 4)",
        "Sorting Check: Singly linked list auto-sorted by arrival -> P1, P2",
        "",
        "Expected vs Actual Output:",
        "  Sorted Order: P1, P2",
        "  Gantt Chart : P1(0-2) P2(2-4) P1(4-6) P2(6-7)",
        "  Process WT  : P1: WT 2, TAT 6 | P2: WT 3, TAT 6",
        "  Avg WT      : 2.5 ms (Expected: 2.5 ms)",
        "  Avg TAT     : 6.0 ms (Expected: 6.0 ms)",
        "",
        "TEST CASE 3: INVALID INPUT REJECTION",
        "Input : P1 (AT 0, BT -2)",
        "Output: 'Invalid burst time. It must be greater than 0.'",
        "",
        "STATUS: VERIFIED & 100% ACCURATE"
    ]:
        p = tf_t4.add_paragraph()
        p.text = line
        p.font.name = FONT_CODE if "Gantt" in line or "Avg" in line else FONT_BODY
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_PURPLE if "STATUS" in line or "2.5" in line else TEXT_WHITE

    set_notes(s18, """
Slide 18 provides formal proof of correctness for all 4 test cases assigned by Rungta International Skills University.
Notice how Test Case 1 produces exactly 1.67 ms average waiting time and 3.67 ms turnaround time.
Notice also how Test Case 3 correctly rejects negative burst times, and Test Case 4 sorts arriving processes and produces 2.5 ms and 6.0 ms.
Every test case passes with 100% precision.
""")

    # ==========================================
    # SLIDE 19: COMPREHENSIVE ALGORITHM COMPARISON
    # ==========================================
    s19 = new_slide()
    add_header(s19, "Comprehensive Algorithm Comparison Matrix", "18. BENCHMARKING & COMPARATIVE ANALYSIS")

    # Table
    table_shape = s19.shapes.add_table(6, 7, Inches(0.8), Inches(1.6), Inches(11.733), Inches(4.5))
    table = table_shape.table

    headers = ["Algorithm", "Preemptive?", "Avg Wait Time", "Starvation?", "Fairness", "Context Overhead", "Optimal For"]
    col_widths = [Inches(1.8), Inches(1.3), Inches(1.5), Inches(1.3), Inches(1.2), Inches(1.8), Inches(2.833)]
    for i, w in enumerate(col_widths):
        table.columns[i].width = w

    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(30, 41, 59)
        p = cell.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_CYAN

    data = [
        ("FCFS", "No", "High (Convoy)", "None", "High", "Zero", "Batch jobs of uniform duration"),
        ("SJF (Non-Preempt)", "No", "Optimal (Static)", "High", "Low", "Low", "Long-term batch systems with known bursts"),
        ("SRTF", "Yes", "Optimal (Dynamic)", "High", "Low", "High", "Time-critical short interactive workloads"),
        ("Priority (PS No. 80)", "No", "Moderate", "High (Low Pr)", "Low", "Low", "Real-time task priority classification"),
        ("Round Robin (PS No. 80)", "Yes", "Moderate", "Zero (Fair)", "Very High", "Moderate (Q-depend)", "General-purpose desktop & server OS")
    ]

    for row_idx, row_data in enumerate(data, start=1):
        bg_col = CARD_BG if row_idx % 2 == 1 else CARD_BG_ALT
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_col
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(10)
            p.font.color.rgb = COLOR_BLUE if col_idx == 0 else TEXT_WHITE
            if "PS No. 80" in text:
                p.font.bold = True

    # Bottom summary callout
    bot_card = add_card(s19, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.7), bg_color=CARD_BG_ALT, border_color=CARD_BORDER)
    tf_bc = bot_card.text_frame
    tf_bc.margin_left = Inches(0.3)
    tf_bc.margin_top = Inches(0.12)
    p = tf_bc.paragraphs[0]
    p.text = "CORE ENGINEERING TAKEAWAY: No single algorithm is optimal across all dimensions. Operating Systems balance throughput against latency by selecting Round Robin for user tasks and Priority for real-time interrupts."
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN

    set_notes(s19, """
Slide 19 is our comparative matrix summarizing all five major CPU scheduling algorithms.
Notice the trade-offs:
SJF and SRTF offer mathematically optimal average wait times, but risk starving long jobs.
Round Robin provides absolute fairness and zero starvation, but incurs context switching overhead.
Priority Scheduling ensures critical tasks run first, but requires aging to prevent indefinite blocking.
""")

    # ==========================================
    # SLIDE 20: ADVANTAGES AND LIMITATIONS
    # ==========================================
    s20 = new_slide()
    add_header(s20, "System Evaluation: Advantages & Technical Limitations", "19. EVALUATION & ENGINEERING CRITIQUE")

    adv_card = add_card(s20, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), border_color=COLOR_GREEN)
    tf_adv = adv_card.text_frame
    tf_adv.margin_left = tf_adv.margin_right = tf_adv.margin_top = Inches(0.3)
    p = tf_adv.paragraphs[0]
    p.text = "SYSTEM STRENGTHS & ADVANTAGES"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = COLOR_GREEN
    p.space_after = Pt(10)
    for b in [
        "Pure First-Principles Implementation: Engineered bare-metal Singly Linked List with Merge Sort, Circular Queue, and Binary Min-Heap without external library shortcuts.",
        "Zero-Dependency Portability: Single `.java` file compiles and runs instantaneously on any system with OpenJDK.",
        "Millisecond-Accurate Step Animator: Allows students and examiners to inspect exact queue contents at every clock tick.",
        "100% University Verified: Confirmed against all benchmark test cases with zero discrepancies.",
        "Dual-Delivery Flexibility: Interactive Web GUI for visual intuition alongside terminal CLI for automated grading."
    ]:
        p = tf_adv.add_paragraph()
        p.text = "✓ " + b
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(8)

    lim_card = add_card(s20, Inches(6.8), Inches(1.6), Inches(5.733), Inches(5.3), border_color=COLOR_AMBER)
    tf_lim = lim_card.text_frame
    tf_lim.margin_left = tf_lim.margin_right = tf_lim.margin_top = Inches(0.3)
    p = tf_lim.paragraphs[0]
    p.text = "TECHNICAL LIMITATIONS & CONSTRAINTS"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = COLOR_AMBER
    p.space_after = Pt(10)
    for b in [
        "CPU-Bound Workload Focus: Assumes processes only perform CPU bursts; does not simulate interleaved I/O wait states or disk blocking.",
        "Uniprocessor Core Modeling: Simulates a single CPU core, omitting multi-core SMP load balancing and processor affinity.",
        "Deterministic Workload Inputs: Workload arrival times are static inputs rather than stochastically generated Poisson arrivals.",
        "Fixed Priority Without Aging: Priority scheduling does not yet implement dynamic priority promotion (aging) to counter starvation."
    ]:
        p = tf_lim.add_paragraph()
        p.text = "⚠ " + b
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(8)

    set_notes(s20, """
In Slide 20, we provide an honest engineering evaluation of our simulator.
Its strengths lie in its first-principles data structures, zero external dependencies, and verified precision.
Its limitations reflect academic project boundaries: it focuses strictly on CPU-bound workloads on a single core and does not simulate complex I/O wait queues.
""")

    # ==========================================
    # SLIDE 21: FUTURE SCOPE
    # ==========================================
    s21 = new_slide()
    add_header(s21, "Future Scope: Advanced Extensions & Roadmap", "20. FUTURE RESEARCH & EXTENSIONS")

    fs_items = [
        ("Multi-Level Feedback Queue (MLFQ)", "Implement dynamic multi-tier priority queues with automatic demotion of CPU-heavy jobs and priority boosting (aging) to eliminate starvation.", COLOR_CYAN),
        ("Multi-Core SMP Scheduling", "Simulate multi-core architectures (Dual-core, Quad-core) with processor affinity, work-stealing, and load-balancing algorithms.", COLOR_BLUE),
        ("Real-Time Scheduling (EDF / RMS)", "Incorporate hard and soft real-time scheduling algorithms such as Earliest Deadline First (EDF) and Rate Monotonic Scheduling (RMS).", COLOR_PURPLE),
        ("Stochastic Process Generation", "Incorporate random workload generation using Poisson arrival distributions and exponential burst durations for realistic stress testing.", COLOR_GREEN)
    ]

    for idx, (title, desc, col) in enumerate(fs_items):
        x = Inches(0.8 + (idx % 2) * 5.95)
        y = Inches(1.6 + (idx // 2) * 2.65)
        c = add_card(s21, x, y, Inches(5.75), Inches(2.4), bg_color=CARD_BG, border_color=CARD_BORDER)
        tf = c.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = col
        p.space_after = Pt(8)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_WHITE

    set_notes(s21, """
Slide 21 outlines exciting future directions for our project:
Adding Multi-Level Feedback Queues—which modern OSes like Linux and Windows actually use.
Expanding from single-core to Multi-Core Symmetric Multiprocessing.
Adding Real-Time algorithms like Earliest Deadline First.
And generating stochastic Poisson workloads for realistic stress testing.
""")

    # ==========================================
    # SLIDE 22: CONCLUSION & LEARNING OUTCOMES
    # ==========================================
    s22 = new_slide()
    add_header(s22, "Conclusion & Key Educational Takeaways", "21. CONCLUSION & SUMMARY")

    conc_cards = [
        ("Bridging Theory and Practice", "Transformed theoretical operating system scheduling concepts into a fully functional, mathematically accurate software simulator.", COLOR_CYAN),
        ("Data Structure Mastery", "Mastered low-level pointer management and memory layouts by implementing Singly Linked List Merge Sort, Circular Queues, and Min-Heaps from scratch.", COLOR_BLUE),
        ("Pedagogical Value", "Delivered an intuitive, interactive visualization tool that simplifies the comprehension of complex scheduling dynamics for students and educators.", COLOR_PURPLE)
    ]

    for idx, (title, desc, col) in enumerate(conc_cards):
        x = Inches(0.8 + idx * 3.95)
        y = Inches(1.6)
        c = add_card(s22, x, y, Inches(3.8), Inches(4.3), bg_color=CARD_BG, border_color=col)
        tf = c.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(14)
        p.font.color.rgb = col
        p.space_after = Pt(12)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(11.5)
        p2.font.color.rgb = TEXT_WHITE

    # Bottom summary banner
    summary_card = add_card(s22, Inches(0.8), Inches(6.1), Inches(11.733), Inches(0.9), bg_color=CARD_BG_ALT, border_color=BORDER_GLOW)
    tf_sc = summary_card.text_frame
    tf_sc.margin_left = Inches(0.3)
    tf_sc.margin_top = Inches(0.15)
    p = tf_sc.paragraphs[0]
    p.text = "PROJECT PS NO. 80 COMPLETION STATUS: 100% OF BARE MINIMUM REQUIREMENTS ACHIEVED & RIGOROUSLY VERIFIED."
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_CYAN

    set_notes(s22, """
To conclude, this project successfully bridges the gap between theoretical operating system principles and practical software engineering.
By designing custom data structures from scratch and building an interactive visualizer, we achieved a deep, comprehensive mastery of CPU scheduling dynamics and satisfied 100% of university project requirements.
""")

    # ==========================================
    # SLIDE 23: THANK YOU & Q&A
    # ==========================================
    s23 = new_slide()
    # Centered hero card
    add_card(s23, Inches(1.5), Inches(1.0), Inches(10.333), Inches(5.5), bg_color=CARD_BG, border_color=BORDER_GLOW, border_width=2)
    
    # Badges
    add_badge(s23, "DEFENSE COMPLETE", Inches(5.3), Inches(1.4), width=Inches(2.7), border_color=COLOR_GREEN, text_color=COLOR_GREEN)

    tbox = s23.shapes.add_textbox(Inches(2.0), Inches(2.0), Inches(9.333), Inches(3.8))
    tf23 = tbox.text_frame
    tf23.word_wrap = True
    
    p = tf23.paragraphs[0]
    p.text = "Thank You!"
    p.font.name = FONT_HEADING
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.alignment = PP_ALIGN.CENTER
    p.space_after = Pt(10)

    p2 = tf23.add_paragraph()
    p2.text = "Questions & Discussion"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(20)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_CYAN
    p2.alignment = PP_ALIGN.CENTER
    p2.space_after = Pt(18)

    p3 = tf23.add_paragraph()
    p3.text = "Project PS No. 80: CPU Scheduling Simulator\nSchool of Computer Science & Engineering | Rungta International Skills University\n\nLive Simulator Demonstration Available on Request"
    p3.font.name = FONT_BODY
    p3.font.size = Pt(13)
    p3.font.color.rgb = TEXT_MUTED
    p3.alignment = PP_ALIGN.CENTER

    set_notes(s23, """
Thank you very much for your time, attention, and guidance.
I am now open to any questions, algorithmic inquiries, or requests for a live simulator demonstration from the examination panel.
""")

    output_path = r"C:\Users\ANUGYA\.gemini\antigravity\scratch\cpu-scheduling-simulator\CPU_Scheduling_Simulator_Presentation.pptx"
    prs.save(output_path)
    print(f"Successfully generated 23-slide PowerPoint presentation at: {output_path}")

if __name__ == "__main__":
    create_presentation()
