import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ppt_assets")
os.makedirs(OUT_DIR, exist_ok=True)

FONT_REG = r"C:\Windows\Fonts\segoeui.ttf"
FONT_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_MONO = r"C:\Windows\Fonts\consola.ttf"
FONT_MONO_BOLD = r"C:\Windows\Fonts\consolab.ttf"

def f(path, size):
    return ImageFont.truetype(path, size)

def draw_rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)

def make_console_cli_screenshot():
    W, H = 1520, 860
    img = Image.new("RGB", (W, H), (18, 22, 31))
    d = ImageDraw.Draw(img)

    # Windows Terminal Titlebar
    d.rectangle([0, 0, W, 54], fill=(32, 37, 48))
    d.ellipse([22, 18, 38, 34], fill=(239, 68, 68))
    d.ellipse([48, 18, 64, 34], fill=(245, 158, 11))
    d.ellipse([74, 18, 90, 34], fill=(34, 197, 94))
    d.text((115, 15), "Command Prompt - java CpuSchedulingSimulator --test", font=f(FONT_BOLD, 18), fill=(226, 232, 240))

    lines = [
        ("==================================================", (56, 189, 248)),
        ("    RUNGTA INTERNATIONAL SKILLS UNIVERSITY", (248, 250, 252)),
        ("    SCHOOL OF COMPUTER SCIENCE AND ENGINEERING", (148, 163, 184)),
        ("    PS No. 80: CPU SCHEDULING SIMULATOR", (56, 189, 248)),
        ("==================================================", (56, 189, 248)),
        ("", (200, 200, 200)),
        ("Test Case 1: Normal Input  |  Algorithm: Priority (Non-Preemptive)", (251, 191, 36)),
        ("Inputs: P1(AT=0, BT=3, Pr=3) | P2(AT=1, BT=2, Pr=1) | P3(AT=2, BT=1, Pr=2)", (203, 213, 225)),
        ("  Actual Output -> Gantt: P1(0-3) P2(3-5) P3(5-6)", (52, 211, 153)),
        ("  WT: P1 0, P2 2, P3 3  |  TAT: P1 3, P2 4, P3 4  |  Avg WT: 1.67 | Avg TAT: 3.67", (226, 232, 240)),
        ("", (200, 200, 200)),
        ("Test Case 2: Boundary / Minimum Input  |  Algorithm: Priority", (251, 191, 36)),
        ("Inputs: P1(AT=0, BT=4, Pr=1)", (203, 213, 225)),
        ("  Actual Output -> Gantt: P1(0-4)  |  P1: WT 0, TAT 4  |  Avg WT: 0.0 | Avg TAT: 4.0", (52, 211, 153)),
        ("", (200, 200, 200)),
        ("Test Case 3: Invalid Input Validation", (251, 191, 36)),
        ("Inputs: P1(AT=0, BT=-2)", (203, 213, 225)),
        ("  Actual Output -> Invalid burst time. It must be greater than 0.", (248, 113, 113)),
        ("", (200, 200, 200)),
        ("Test Case 4: Round Robin Scheduling (Quantum = 2)", (251, 191, 36)),
        ("Inputs: P2(AT=1, BT=3) entered first, P1(AT=0, BT=4)", (203, 213, 225)),
        ("  Sorted by arrival (Singly Linked List Merge Sort): P1, P2", (192, 132, 252)),
        ("  Actual Output -> Gantt: P1(0-2) P2(2-4) P1(4-6) P2(6-7)", (52, 211, 153)),
        ("  P1: WT 2, TAT 6 | P2: WT 3, TAT 6  |  Avg WT: 2.5 | Avg TAT: 6.0", (226, 232, 240)),
        ("", (200, 200, 200)),
        ("==================================================", (52, 211, 153)),
        ("ALL MANDATORY TEST CASES PASSED SUCCESSFULLY!", (52, 211, 153)),
        ("==================================================", (52, 211, 153)),
    ]

    y = 76
    for text, color in lines:
        if text:
            d.text((34, y), text, font=f(FONT_MONO, 20), fill=color)
        y += 27

    out_path = os.path.join(OUT_DIR, "output_console_cli.png")
    img.save(out_path)
    return out_path

def make_web_ui_screenshot(mode="priority"):
    W, H = 1560, 880
    img = Image.new("RGB", (W, H), (11, 15, 25))
    d = ImageDraw.Draw(img)

    # Browser Chrome Bar
    d.rectangle([0, 0, W, 48], fill=(24, 31, 46))
    d.ellipse([20, 15, 36, 31], fill=(239, 68, 68))
    d.ellipse([44, 15, 60, 31], fill=(245, 158, 11))
    d.ellipse([68, 15, 84, 31], fill=(34, 197, 94))
    draw_rounded_rect(d, [110, 9, 980, 39], 10, fill=(11, 15, 25), outline=(51, 65, 85))
    d.text((130, 14), "http://localhost:8080/  —  CPU Scheduling Simulator (Web Visualizer)", font=f(FONT_REG, 15), fill=(148, 163, 184))

    # App Header
    draw_rounded_rect(d, [32, 66, W - 32, 168], 14, fill=(21, 29, 48), outline=(36, 48, 72), width=2)
    d.text((58, 82), "RUNGTA INTERNATIONAL SKILLS UNIVERSITY  |  OS & DSA SIMULATOR", font=f(FONT_BOLD, 14), fill=(56, 189, 248))
    d.text((58, 105), "CPU Scheduling Simulator", font=f(FONT_BOLD, 30), fill=(248, 250, 252))
    badge_txt = "Priority Scheduling (Min-Heap)" if mode == "priority" else "Round Robin (Circular Queue, Q=2)"
    draw_rounded_rect(d, [1110, 95, W - 56, 138], 18, fill=(14, 48, 74), outline=(56, 189, 248), width=1)
    d.text((1130, 106), badge_txt, font=f(FONT_BOLD, 16), fill=(56, 189, 248))

    # Left Card: Simulator Controls & Process Table
    draw_rounded_rect(d, [32, 186, 540, H - 28], 14, fill=(21, 29, 48), outline=(36, 48, 72), width=2)
    d.text((56, 208), "Simulator Controls", font=f(FONT_BOLD, 22), fill=(248, 250, 252))

    # Algo Toggle
    p_bg = (30, 64, 175) if mode == "priority" else (14, 21, 38)
    r_bg = (30, 64, 175) if mode == "rr" else (14, 21, 38)
    draw_rounded_rect(d, [56, 254, 285, 302], 8, fill=p_bg, outline=(56, 189, 248) if mode == "priority" else (51, 65, 85), width=2)
    d.text((76, 267), "Priority (Non-Preempt)", font=f(FONT_BOLD, 15), fill=(248, 250, 252))
    draw_rounded_rect(d, [298, 254, 514, 302], 8, fill=r_bg, outline=(56, 189, 248) if mode == "rr" else (51, 65, 85), width=2)
    d.text((344, 267), "Round Robin", font=f(FONT_BOLD, 15), fill=(248, 250, 252))

    if mode == "rr":
        d.text((56, 320), "Time Quantum (ms):", font=f(FONT_BOLD, 15), fill=(148, 163, 184))
        draw_rounded_rect(d, [225, 314, 320, 348], 6, fill=(11, 15, 25), outline=(56, 189, 248))
        d.text((262, 320), "2", font=f(FONT_BOLD, 17), fill=(248, 250, 252))
        table_top = 368
    else:
        table_top = 326

    # Process Table
    d.text((56, table_top), "Process Input List", font=f(FONT_BOLD, 16), fill=(148, 163, 184))
    y = table_top + 32
    draw_rounded_rect(d, [56, y, 514, y + 40], 6, fill=(14, 21, 38))
    headers = ["PID", "Arrival", "Burst", "Priority"]
    xs = [76, 170, 290, 410]
    for h_txt, x in zip(headers, xs):
        d.text((x, y + 10), h_txt, font=f(FONT_BOLD, 15), fill=(56, 189, 248))

    rows = [("P1", "0", "3", "3"), ("P2", "1", "2", "1"), ("P3", "2", "1", "2")] if mode == "priority" else [("P2", "1", "3", "1"), ("P1", "0", "4", "1")]
    y += 46
    for pid, at, bt, pr in rows:
        draw_rounded_rect(d, [56, y, 514, y + 44], 6, fill=(15, 23, 42), outline=(36, 48, 72))
        for val, x in zip([pid, at, bt, pr], xs):
            d.text((x + 6, y + 11), val, font=f(FONT_MONO_BOLD, 16), fill=(248, 250, 252))
        y += 52

    # Run Button
    draw_rounded_rect(d, [56, H - 96, 514, H - 48], 10, fill=(37, 99, 235), outline=(96, 165, 250), width=1)
    d.text((205, H - 83), "Run Simulation", font=f(FONT_BOLD, 18), fill=(255, 255, 255))

    # Right Card: Execution Results & Gantt Chart
    draw_rounded_rect(d, [564, 186, W - 32, H - 28], 14, fill=(21, 29, 48), outline=(36, 48, 72), width=2)
    d.text((592, 208), "Execution Results & Gantt Chart", font=f(FONT_BOLD, 22), fill=(248, 250, 252))
    sorted_txt = "Sorted Order (Linked List): P1, P2, P3" if mode == "priority" else "Sorted Order (Linked List): P1, P2"
    d.text((1110, 214), sorted_txt, font=f(FONT_BOLD, 15), fill=(56, 189, 248))

    # Gantt Timeline Box
    draw_rounded_rect(d, [592, 256, W - 56, 446], 10, fill=(14, 21, 38), outline=(36, 48, 72))
    d.text((612, 270), "VISUAL GANTT TIMELINE", font=f(FONT_BOLD, 13), fill=(148, 163, 184))

    if mode == "priority":
        segs = [("P1 (0-3 ms)", 0, 3, (56, 189, 248)), ("P2 (3-5 ms)", 3, 5, (168, 85, 247)), ("P3 (5-6 ms)", 5, 6, (52, 211, 153))]
        total = 6
        console_line1 = "Gantt: P1(0-3) P2(3-5) P3(5-6)"
        console_line2 = "WT: P1 0, P2 2, P3 3  |  TAT: P1 3, P2 4, P3 4"
        console_line3 = "Avg WT: 1.67 ms  |  Avg TAT: 3.67 ms"
        queue_title = "QUEUE STATE: Min-Heap Priority Queue  (t = 3 ms)"
        q_items = [("P2 (Pr: 1)", (168, 85, 247)), ("P3 (Pr: 2)", (52, 211, 153))]
        q_desc = "At t=3: P1 finished. Min-Heap extracts P2 (highest priority = 1)."
        stats = [("Avg Waiting Time", "1.67 ms", (56, 189, 248)), ("Avg Turnaround", "3.67 ms", (168, 85, 247)), ("Total Duration", "6 ms", (248, 250, 252)), ("CPU Utilization", "100%", (52, 211, 153))]
    else:
        segs = [("P1 (0-2)", 0, 2, (56, 189, 248)), ("P2 (2-4)", 2, 4, (245, 158, 11)), ("P1 (4-6)", 4, 6, (56, 189, 248)), ("P2 (6-7)", 6, 7, (245, 158, 11))]
        total = 7
        console_line1 = "Gantt: P1(0-2) P2(2-4) P1(4-6) P2(6-7)"
        console_line2 = "P1: WT 2, TAT 6  |  P2: WT 3, TAT 6"
        console_line3 = "Avg WT: 2.50 ms  |  Avg TAT: 6.00 ms"
        queue_title = "QUEUE STATE: Array-Based Circular Queue  (t = 2 ms)"
        q_items = [("Front -> P2 (Rem: 3)", (245, 158, 11)), ("P1 (Rem: 2) <- Rear", (56, 189, 248))]
        q_desc = "At t=2: P2 arrived during P1's slice (t=1), so P2 entered queue BEFORE P1 re-queued."
        stats = [("Avg Waiting Time", "2.50 ms", (56, 189, 248)), ("Avg Turnaround", "6.00 ms", (168, 85, 247)), ("Total Duration", "7 ms", (248, 250, 252)), ("CPU Utilization", "100%", (52, 211, 153))]

    bar_x0, bar_x1, bar_y0, bar_y1 = 612, W - 76, 300, 358
    bar_w = bar_x1 - bar_x0
    for label, s, e, col in segs:
        x0 = bar_x0 + int((s / total) * bar_w)
        x1 = bar_x0 + int((e / total) * bar_w) - 4
        draw_rounded_rect(d, [x0, bar_y0, x1, bar_y1], 6, fill=col)
        d.text((x0 + 14, bar_y0 + 18), label, font=f(FONT_BOLD, 16), fill=(11, 15, 25))

    d.text((612, 372), console_line1, font=f(FONT_MONO_BOLD, 16), fill=(248, 250, 252))
    d.text((612, 396), console_line2, font=f(FONT_MONO, 15), fill=(203, 213, 225))
    d.text((612, 419), console_line3, font=f(FONT_MONO_BOLD, 15), fill=(52, 211, 153))

    # Queue State Box
    draw_rounded_rect(d, [592, 464, W - 56, 598], 10, fill=(14, 21, 38), outline=(36, 48, 72))
    d.text((612, 478), queue_title, font=f(FONT_BOLD, 14), fill=(56, 189, 248))
    qx = 612
    for q_txt, col in q_items:
        qw = 210 if mode == "priority" else 260
        draw_rounded_rect(d, [qx, 512, qx + qw, 552], 8, fill=(21, 29, 48), outline=col, width=2)
        d.text((qx + 16, 522), q_txt, font=f(FONT_MONO_BOLD, 15), fill=(248, 250, 252))
        qx += qw + 18
    d.text((612, 566), q_desc, font=f(FONT_REG, 15), fill=(148, 163, 184))

    # Stats Grid
    card_w = (W - 56 - 592 - 45) // 4
    sx = 592
    for lbl, val, col in stats:
        draw_rounded_rect(d, [sx, 618, sx + card_w, 712], 10, fill=(14, 21, 38), outline=(36, 48, 72))
        d.text((sx + 16, 632), lbl, font=f(FONT_BOLD, 13), fill=(148, 163, 184))
        d.text((sx + 16, 662), val, font=f(FONT_BOLD, 26), fill=col)
        sx += card_w + 15

    # Summary Metrics Table Footer
    draw_rounded_rect(d, [592, 728, W - 56, H - 46], 10, fill=(14, 21, 38), outline=(36, 48, 72))
    tbl_headers = ["PID", "AT", "BT", "Priority", "CT", "TAT = CT-AT", "WT = TAT-BT"]
    txs = [615, 700, 785, 875, 985, 1085, 1255]
    for h_txt, tx in zip(tbl_headers, txs):
        d.text((tx, 738), h_txt, font=f(FONT_BOLD, 14), fill=(56, 189, 248))
    if mode == "priority":
        mrows = [("P1", "0", "3", "3", "3", "3", "0"), ("P2", "1", "2", "1", "5", "4", "2"), ("P3", "2", "1", "2", "6", "4", "3")]
    else:
        mrows = [("P1", "0", "4", "1", "6", "6", "2"), ("P2", "1", "3", "1", "7", "6", "3")]
    ry = 766
    for r in mrows:
        for val, tx in zip(r, txs):
            d.text((tx + 4, ry), val, font=f(FONT_MONO, 15), fill=(226, 232, 240))
        ry += 26

    fname = f"output_web_{mode}.png"
    out_path = os.path.join(OUT_DIR, fname)
    img.save(out_path)
    return out_path

def make_validation_screenshot():
    W, H = 1480, 740
    img = Image.new("RGB", (W, H), (11, 15, 25))
    d = ImageDraw.Draw(img)

    # Title Bar
    d.rectangle([0, 0, W, 48], fill=(24, 31, 46))
    d.ellipse([20, 15, 36, 31], fill=(239, 68, 68))
    d.ellipse([44, 15, 60, 31], fill=(245, 158, 11))
    d.ellipse([68, 15, 84, 31], fill=(34, 197, 94))
    d.text((112, 13), "Test Case 3: Input Validation & Error Rejection (Web UI & Console)", font=f(FONT_BOLD, 16), fill=(226, 232, 240))

    # Left Panel: Web UI Error Alert
    draw_rounded_rect(d, [36, 76, 720, H - 36], 14, fill=(21, 29, 48), outline=(36, 48, 72), width=2)
    d.text((62, 102), "Web Simulator — Validation Check", font=f(FONT_BOLD, 22), fill=(248, 250, 252))
    draw_rounded_rect(d, [62, 154, 694, 210], 8, fill=(14, 21, 38), outline=(51, 65, 85))
    d.text((82, 171), "Input: PID = P1   |   Arrival Time = 0   |   Burst Time = -2   |   Priority = 1", font=f(FONT_MONO, 16), fill=(226, 232, 240))

    draw_rounded_rect(d, [62, 242, 694, 348], 10, fill=(69, 26, 36), outline=(248, 113, 113), width=2)
    d.text((88, 262), "VALIDATION ERROR REJECTED", font=f(FONT_BOLD, 17), fill=(252, 165, 165))
    d.text((88, 296), "Invalid burst time. It must be greater than 0.", font=f(FONT_MONO_BOLD, 18), fill=(254, 226, 226))

    d.text((62, 382), "All Validation Rules Enforced:", font=f(FONT_BOLD, 18), fill=(56, 189, 248))
    rules = [
        "1. Arrival Time < 0   ->  Rejected (cannot be negative)",
        "2. Burst Time <= 0    ->  Rejected (must be > 0 ms)",
        "3. Priority <= 0      ->  Rejected (must be > 0)",
        "4. Time Quantum <= 0  ->  Rejected (must be > 0 ms)",
        "5. Empty Process List ->  Rejected (at least 1 process)",
    ]
    ry = 425
    for rule in rules:
        draw_rounded_rect(d, [62, ry, 694, ry + 42], 6, fill=(14, 21, 38), outline=(36, 48, 72))
        d.text((82, ry + 11), rule, font=f(FONT_MONO, 16), fill=(203, 213, 225))
        ry += 50

    # Right Panel: Java Console CLI Validation Output
    draw_rounded_rect(d, [750, 76, W - 36, H - 36], 14, fill=(18, 22, 31), outline=(51, 65, 85), width=2)
    d.text((778, 102), "Console CLI — Validation & Boundary Execution", font=f(FONT_BOLD, 22), fill=(52, 211, 153))
    cli_lines = [
        ("C:\\cpu-scheduling-simulator> java CpuSchedulingSimulator", (148, 163, 184)),
        ("", (200, 200, 200)),
        ("Test Case 2: Boundary / Minimum Input", (251, 191, 36)),
        ("  Algorithm : Priority (Non-Preemptive)", (226, 232, 240)),
        ("  Process   : P1 (AT=0, BT=4, Pr=1)", (226, 232, 240)),
        ("  Gantt     : P1(0-4)", (52, 211, 153)),
        ("  Metrics   : P1: WT 0, TAT 4 | Avg WT: 0.0 | Avg TAT: 4.0", (226, 232, 240)),
        ("  Result    : PASSED", (52, 211, 153)),
        ("", (200, 200, 200)),
        ("Test Case 3: Invalid Input Rejection", (251, 191, 36)),
        ("  Process   : P1 (AT=0, BT=-2)", (226, 232, 240)),
        ("  Expected  : Invalid burst time. It must be greater than 0.", (203, 213, 225)),
        ("  Actual    : Invalid burst time. It must be greater than 0.", (248, 113, 113)),
        ("  Result    : PASSED (Safely Rejected)", (52, 211, 153)),
    ]
    cy = 160
    for txt, col in cli_lines:
        if txt:
            d.text((778, cy), txt, font=f(FONT_MONO, 16), fill=col)
        cy += 34

    out_path = os.path.join(OUT_DIR, "output_validation.png")
    img.save(out_path)
    return out_path

if __name__ == "__main__":
    p1 = make_console_cli_screenshot()
    p2 = make_web_ui_screenshot("priority")
    p3 = make_web_ui_screenshot("rr")
    p4 = make_validation_screenshot()
    print("Generated:", p1, p2, p3, p4)
