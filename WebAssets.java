// Helper class containing Web UI assets for the embedded HTTP server in CpuSchedulingSimulator

public class WebAssets {
    public static String getHtmlContent() {
        return "<!DOCTYPE html>\n" +
"<html lang=\"en\">\n" +
"<head>\n" +
"    <meta charset=\"UTF-8\">\n" +
"    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n" +
"    <title>CPU Scheduling Simulator - PS No. 80</title>\n" +
"    <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n" +
"    <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n" +
"    <link href=\"https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&display=swap\" rel=\"stylesheet\">\n" +
"    <style>\n" +
"        :root {\n" +
"            --bg-base: #0f172a;\n" +
"            --bg-card: #1e293b;\n" +
"            --bg-card-hover: #334155;\n" +
"            --border: #334155;\n" +
"            --border-light: #475569;\n" +
"            --text-primary: #f8fafc;\n" +
"            --text-secondary: #94a3b8;\n" +
"            --text-muted: #64748b;\n" +
"            --primary: #38bdf8;\n" +
"            --primary-glow: rgba(56, 189, 248, 0.25);\n" +
"            --accent: #818cf8;\n" +
"            --success: #34d399;\n" +
"            --warning: #fbbf24;\n" +
"            --danger: #f87171;\n" +
"            --p1-color: #38bdf8;\n" +
"            --p2-color: #ec4899;\n" +
"            --p3-color: #a855f7;\n" +
"            --p4-color: #eab308;\n" +
"            --p5-color: #10b981;\n" +
"            --p6-color: #f97316;\n" +
"            --radius-sm: 6px;\n" +
"            --radius-md: 10px;\n" +
"            --radius-lg: 16px;\n" +
"            --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.3);\n" +
"        }\n" +
"        * { box-sizing: border-box; margin: 0; padding: 0; }\n" +
"        body {\n" +
"            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;\n" +
"            background-color: var(--bg-base);\n" +
"            color: var(--text-primary);\n" +
"            line-height: 1.5;\n" +
"            padding: 24px;\n" +
"            min-height: 100vh;\n" +
"        }\n" +
"        .container {\n" +
"            max-width: 1280px;\n" +
"            margin: 0 auto;\n" +
"            display: flex;\n" +
"            flex-direction: column;\n" +
"            gap: 24px;\n" +
"        }\n" +
"        header {\n" +
"            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);\n" +
"            border: 1px solid var(--border);\n" +
"            border-radius: var(--radius-lg);\n" +
"            padding: 24px 32px;\n" +
"            display: flex;\n" +
"            justify-content: space-between;\n" +
"            align-items: center;\n" +
"            box-shadow: var(--shadow);\n" +
"            position: relative;\n" +
"            overflow: hidden;\n" +
"        }\n" +
"        header::after {\n" +
"            content: '';\n" +
"            position: absolute;\n" +
"            top: 0; right: 0; width: 300px; height: 100%;\n" +
"            background: radial-gradient(circle, rgba(56, 189, 248, 0.15) 0%, transparent 70%);\n" +
"            pointer-events: none;\n" +
"        }\n" +
"        .brand-title {\n" +
"            font-size: 0.85rem;\n" +
"            text-transform: uppercase;\n" +
"            letter-spacing: 0.1em;\n" +
"            color: var(--primary);\n" +
"            font-weight: 700;\n" +
"            margin-bottom: 4px;\n" +
"        }\n" +
"        .project-title {\n" +
"            font-size: 1.85rem;\n" +
"            font-weight: 800;\n" +
"            letter-spacing: -0.02em;\n" +
"            background: linear-gradient(to right, #ffffff, #94a3b8);\n" +
"            -webkit-background-clip: text;\n" +
"            -webkit-text-fill-color: transparent;\n" +
"        }\n" +
"        .project-meta {\n" +
"            display: flex;\n" +
"            gap: 8px;\n" +
"            margin-top: 8px;\n" +
"            flex-wrap: wrap;\n" +
"        }\n" +
"        .badge {\n" +
"            display: inline-flex;\n" +
"            align-items: center;\n" +
"            gap: 4px;\n" +
"            background: rgba(51, 65, 85, 0.8);\n" +
"            color: var(--text-secondary);\n" +
"            font-size: 0.75rem;\n" +
"            font-weight: 600;\n" +
"            padding: 4px 10px;\n" +
"            border-radius: 9999px;\n" +
"            border: 1px solid var(--border);\n" +
"        }\n" +
"        .badge-cyan { background: rgba(56, 189, 248, 0.15); color: var(--primary); border-color: rgba(56, 189, 248, 0.3); }\n" +
"        .badge-purple { background: rgba(168, 85, 247, 0.15); color: #c084fc; border-color: rgba(168, 85, 247, 0.3); }\n" +
"        .testcase-bar {\n" +
"            background: var(--bg-card);\n" +
"            border: 1px solid var(--border);\n" +
"            border-radius: var(--radius-md);\n" +
"            padding: 16px 20px;\n" +
"            display: flex;\n" +
"            flex-direction: column;\n" +
"            gap: 12px;\n" +
"        }\n" +
"        .testcase-label {\n" +
"            font-size: 0.8rem;\n" +
"            text-transform: uppercase;\n" +
"            font-weight: 700;\n" +
"            letter-spacing: 0.05em;\n" +
"            color: var(--text-secondary);\n" +
"        }\n" +
"        .testcase-btns {\n" +
"            display: grid;\n" +
"            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));\n" +
"            gap: 12px;\n" +
"        }\n" +
"        .btn-testcase {\n" +
"            background: #1e293b;\n" +
"            border: 1px solid var(--border-light);\n" +
"            color: var(--text-primary);\n" +
"            padding: 10px 14px;\n" +
"            border-radius: var(--radius-sm);\n" +
"            font-size: 0.85rem;\n" +
"            cursor: pointer;\n" +
"            display: flex;\n" +
"            flex-direction: column;\n" +
"            text-align: left;\n" +
"            transition: all 0.2s ease;\n" +
"        }\n" +
"        .btn-testcase:hover {\n" +
"            background: var(--bg-card-hover);\n" +
"            border-color: var(--primary);\n" +
"            transform: translateY(-2px);\n" +
"            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);\n" +
"        }\n" +
"        .btn-testcase .title { font-weight: 600; color: #fff; }\n" +
"        .btn-testcase .desc { font-size: 0.72rem; color: var(--text-muted); margin-top: 2px; }\n" +
"        .grid-main {\n" +
"            display: grid;\n" +
"            grid-template-columns: 420px 1fr;\n" +
"            gap: 24px;\n" +
"        }\n" +
"        @media (max-width: 1024px) {\n" +
"            .grid-main { grid-template-columns: 1fr; }\n" +
"        }\n" +
"        .card {\n" +
"            background: var(--bg-card);\n" +
"            border: 1px solid var(--border);\n" +
"            border-radius: var(--radius-lg);\n" +
"            padding: 24px;\n" +
"            box-shadow: var(--shadow);\n" +
"            display: flex;\n" +
"            flex-direction: column;\n" +
"            gap: 20px;\n" +
"        }\n" +
"        .card-header {\n" +
"            display: flex;\n" +
"            justify-content: space-between;\n" +
"            align-items: center;\n" +
"            border-bottom: 1px solid var(--border);\n" +
"            padding-bottom: 14px;\n" +
"        }\n" +
"        .card-title {\n" +
"            font-size: 1.15rem;\n" +
"            font-weight: 700;\n" +
"            color: #fff;\n" +
"        }\n" +
"        .algo-selector {\n" +
"            display: flex;\n" +
"            gap: 8px;\n" +
"            background: #0f172a;\n" +
"            padding: 4px;\n" +
"            border-radius: var(--radius-md);\n" +
"            border: 1px solid var(--border);\n" +
"        }\n" +
"        .algo-btn {\n" +
"            flex: 1;\n" +
"            padding: 8px 12px;\n" +
"            border: none;\n" +
"            background: transparent;\n" +
"            color: var(--text-secondary);\n" +
"            font-size: 0.85rem;\n" +
"            font-weight: 600;\n" +
"            border-radius: var(--radius-sm);\n" +
"            cursor: pointer;\n" +
"            transition: all 0.2s;\n" +
"            text-align: center;\n" +
"        }\n" +
"        .algo-btn.active {\n" +
"            background: var(--primary);\n" +
"            color: #0f172a;\n" +
"            box-shadow: 0 2px 8px var(--primary-glow);\n" +
"        }\n" +
"        .form-group {\n" +
"            display: flex;\n" +
"            flex-direction: column;\n" +
"            gap: 6px;\n" +
"        }\n" +
"        .form-group label {\n" +
"            font-size: 0.8rem;\n" +
"            font-weight: 600;\n" +
"            color: var(--text-secondary);\n" +
"        }\n" +
"        .form-control {\n" +
"            background: #0f172a;\n" +
"            border: 1px solid var(--border);\n" +
"            border-radius: var(--radius-sm);\n" +
"            color: #fff;\n" +
"            padding: 8px 12px;\n" +
"            font-family: inherit;\n" +
"            font-size: 0.9rem;\n" +
"            outline: none;\n" +
"            transition: border-color 0.2s;\n" +
"        }\n" +
"        .form-control:focus {\n" +
"            border-color: var(--primary);\n" +
"            box-shadow: 0 0 0 2px var(--primary-glow);\n" +
"        }\n" +
"        .process-table-wrapper {\n" +
"            max-height: 280px;\n" +
"            overflow-y: auto;\n" +
"            border: 1px solid var(--border);\n" +
"            border-radius: var(--radius-md);\n" +
"            background: #0f172a;\n" +
"        }\n" +
"        table.proc-table {\n" +
"            width: 100%;\n" +
"            border-collapse: collapse;\n" +
"            text-align: left;\n" +
"            font-size: 0.85rem;\n" +
"        }\n" +
"        table.proc-table th {\n" +
"            background: #1e293b;\n" +
"            padding: 10px 12px;\n" +
"            font-weight: 600;\n" +
"            color: var(--text-secondary);\n" +
"            position: sticky;\n" +
"            top: 0;\n" +
"            border-bottom: 1px solid var(--border);\n" +
"            z-index: 2;\n" +
"        }\n" +
"        table.proc-table td {\n" +
"            padding: 8px 12px;\n" +
"            border-bottom: 1px solid rgba(51, 65, 85, 0.4);\n" +
"        }\n" +
"        table.proc-table tr:hover td {\n" +
"            background: rgba(51, 65, 85, 0.3);\n" +
"        }\n" +
"        .input-compact {\n" +
"            width: 100%;\n" +
"            background: #1e293b;\n" +
"            border: 1px solid var(--border);\n" +
"            color: #fff;\n" +
"            padding: 4px 8px;\n" +
"            border-radius: 4px;\n" +
"            font-family: inherit;\n" +
"            font-size: 0.85rem;\n" +
"        }\n" +
"        .btn-action-row {\n" +
"            display: flex;\n" +
"            gap: 8px;\n" +
"            margin-top: 4px;\n" +
"        }\n" +
"        .btn {\n" +
"            padding: 10px 16px;\n" +
"            border-radius: var(--radius-sm);\n" +
"            font-size: 0.85rem;\n" +
"            font-weight: 600;\n" +
"            border: none;\n" +
"            cursor: pointer;\n" +
"            transition: all 0.2s;\n" +
"            display: inline-flex;\n" +
"            align-items: center;\n" +
"            justify-content: center;\n" +
"            gap: 6px;\n" +
"        }\n" +
"        .btn-primary {\n" +
"            background: var(--primary);\n" +
"            color: #0f172a;\n" +
"            font-weight: 700;\n" +
"            flex: 2;\n" +
"        }\n" +
"        .btn-primary:hover {\n" +
"            filter: brightness(1.1);\n" +
"            box-shadow: 0 4px 14px var(--primary-glow);\n" +
"        }\n" +
"        .btn-secondary {\n" +
"            background: #334155;\n" +
"            color: var(--text-primary);\n" +
"            flex: 1;\n" +
"        }\n" +
"        .btn-secondary:hover {\n" +
"            background: #475569;\n" +
"        }\n" +
"        .btn-danger-sm {\n" +
"            background: rgba(248, 113, 113, 0.2);\n" +
"            border: 1px solid rgba(248, 113, 113, 0.4);\n" +
"            color: var(--danger);\n" +
"            padding: 2px 6px;\n" +
"            border-radius: 4px;\n" +
"            cursor: pointer;\n" +
"            font-size: 0.75rem;\n" +
"        }\n" +
"        .btn-danger-sm:hover {\n" +
"            background: var(--danger);\n" +
"            color: #0f172a;\n" +
"        }\n" +
"        .gantt-container {\n" +
"            display: flex;\n" +
"            flex-direction: column;\n" +
"            gap: 16px;\n" +
"        }\n" +
"        .gantt-chart {\n" +
"            display: flex;\n" +
"            border: 1px solid var(--border);\n" +
"            border-radius: var(--radius-md);\n" +
"            overflow-x: auto;\n" +
"            background: #0f172a;\n" +
"            min-height: 80px;\n" +
"            padding: 8px;\n" +
"            position: relative;\n" +
"        }\n" +
"        .gantt-block {\n" +
"            display: flex;\n" +
"            flex-direction: column;\n" +
"            justify-content: center;\n" +
"            align-items: center;\n" +
"            border-radius: var(--radius-sm);\n" +
"            margin: 0 2px;\n" +
"            font-family: 'Fira Code', monospace;\n" +
"            font-weight: 600;\n" +
"            font-size: 0.85rem;\n" +
"            color: #0f172a;\n" +
"            min-width: 65px;\n" +
"            position: relative;\n" +
"            padding: 10px 4px;\n" +
"            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);\n" +
"            transition: transform 0.2s;\n" +
"        }\n" +
"        .gantt-block:hover {\n" +
"            transform: translateY(-2px);\n" +
"            filter: brightness(1.15);\n" +
"        }\n" +
"        .gantt-time-labels {\n" +
"            display: flex;\n" +
"            justify-content: space-between;\n" +
"            width: 100%;\n" +
"            position: absolute;\n" +
"            bottom: 2px;\n" +
"            padding: 0 6px;\n" +
"            font-size: 0.7rem;\n" +
"            font-family: 'Fira Code', monospace;\n" +
"            font-weight: 500;\n" +
"            opacity: 0.85;\n" +
"        }\n" +
"        .gantt-text-output {\n" +
"            background: #090d16;\n" +
"            border: 1px solid var(--border);\n" +
"            border-radius: var(--radius-sm);\n" +
"            padding: 12px 16px;\n" +
"            font-family: 'Fira Code', monospace;\n" +
"            font-size: 0.9rem;\n" +
"            color: var(--primary);\n" +
"            word-break: break-all;\n" +
"        }\n" +
"        .queue-visualizer {\n" +
"            background: #0f172a;\n" +
"            border: 1px solid var(--border);\n" +
"            border-radius: var(--radius-md);\n" +
"            padding: 16px;\n" +
"            display: flex;\n" +
"            flex-direction: column;\n" +
"            gap: 10px;\n" +
"        }\n" +
"        .queue-items {\n" +
"            display: flex;\n" +
"            gap: 8px;\n" +
"            overflow-x: auto;\n" +
"            padding: 4px 0;\n" +
"            min-height: 48px;\n" +
"            align-items: center;\n" +
"        }\n" +
"        .queue-node {\n" +
"            background: #1e293b;\n" +
"            border: 1px solid var(--primary);\n" +
"            color: var(--primary);\n" +
"            padding: 6px 12px;\n" +
"            border-radius: var(--radius-sm);\n" +
"            font-family: 'Fira Code', monospace;\n" +
"            font-size: 0.8rem;\n" +
"            font-weight: 600;\n" +
"            white-space: nowrap;\n" +
"            animation: popIn 0.3s ease;\n" +
"        }\n" +
"        @keyframes popIn {\n" +
"            from { transform: scale(0.8); opacity: 0; }\n" +
"            to { transform: scale(1); opacity: 1; }\n" +
"        }\n" +
"        .stats-grid {\n" +
"            display: grid;\n" +
"            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));\n" +
"            gap: 16px;\n" +
"        }\n" +
"        .stat-card {\n" +
"            background: #0f172a;\n" +
"            border: 1px solid var(--border);\n" +
"            border-radius: var(--radius-md);\n" +
"            padding: 16px;\n" +
"            display: flex;\n" +
"            flex-direction: column;\n" +
"            gap: 4px;\n" +
"        }\n" +
"        .stat-label {\n" +
"            font-size: 0.75rem;\n" +
"            color: var(--text-secondary);\n" +
"            text-transform: uppercase;\n" +
"            font-weight: 600;\n" +
"            letter-spacing: 0.05em;\n" +
"        }\n" +
"        .stat-val {\n" +
"            font-size: 1.5rem;\n" +
"            font-weight: 800;\n" +
"            color: #fff;\n" +
"            font-family: 'Fira Code', monospace;\n" +
"        }\n" +
"        .stat-val.primary { color: var(--primary); }\n" +
"        .stat-val.accent { color: var(--accent); }\n" +
"        .alert-error {\n" +
"            background: rgba(248, 113, 113, 0.15);\n" +
"            border: 1px solid var(--danger);\n" +
"            color: #fca5a5;\n" +
"            padding: 12px 16px;\n" +
"            border-radius: var(--radius-sm);\n" +
"            font-size: 0.85rem;\n" +
"            font-weight: 600;\n" +
"            display: flex;\n" +
"            align-items: center;\n" +
"            gap: 8px;\n" +
"        }\n" +
"        .sim-controls {\n" +
"            display: flex;\n" +
"            gap: 8px;\n" +
"            align-items: center;\n" +
"            flex-wrap: wrap;\n" +
"        }\n" +
"    </style>\n" +
"</head>\n" +
"<body>\n" +
"    <div class=\"container\">\n" +
"        <!-- Header -->\n" +
"        <header>\n" +
"            <div>\n" +
"                <div class=\"brand-title\">Rungta International Skills University &bull; School of CSE</div>\n" +
"                <h1 class=\"project-title\">CPU Scheduling Simulator</h1>\n" +
"                <div class=\"project-meta\">\n" +
"                    <span class=\"badge badge-cyan\">PS No. 80</span>\n" +
"                    <span class=\"badge\">Priority (Non-preemptive)</span>\n" +
"                    <span class=\"badge\">Round Robin (Circular Queue)</span>\n" +
"                    <span class=\"badge badge-purple\">Min-Heap Priority Queue</span>\n" +
"                    <span class=\"badge\">Singly Linked List Sorting</span>\n" +
"                </div>\n" +
"            </div>\n" +
"            <div>\n" +
"                <button class=\"btn btn-secondary\" onclick=\"generateReport()\">&#128196; Export Lab Report</button>\n" +
"            </div>\n" +
"        </header>\n" +
"\n" +
"        <!-- Test Cases Quick Loader Bar -->\n" +
"        <section class=\"testcase-bar\">\n" +
"            <div class=\"testcase-label\">Official Project Test Cases (Click to load & run)</div>\n" +
"            <div class=\"testcase-btns\">\n" +
"                <button class=\"btn-testcase\" onclick=\"loadTestCase(1)\">\n" +
"                    <span class=\"title\">Test Case 1: Normal Input</span>\n" +
"                    <span class=\"desc\">Priority | P1(0,3,Pr3), P2(1,2,Pr1), P3(2,1,Pr2)</span>\n" +
"                </button>\n" +
"                <button class=\"btn-testcase\" onclick=\"loadTestCase(2)\">\n" +
"                    <span class=\"title\">Test Case 2: Boundary Input</span>\n" +
"                    <span class=\"desc\">Priority | Single Process P1(0,4,Pr1)</span>\n" +
"                </button>\n" +
"                <button class=\"btn-testcase\" onclick=\"loadTestCase(3)\">\n" +
"                    <span class=\"title\">Test Case 3: Invalid Input</span>\n" +
"                    <span class=\"desc\">Error check: P1(0, BT=-2) validation reject</span>\n" +
"                </button>\n" +
"                <button class=\"btn-testcase\" onclick=\"loadTestCase(4)\">\n" +
"                    <span class=\"title\">Test Case 4: Round Robin</span>\n" +
"                    <span class=\"desc\">Quantum 2 | P2 entered 1st (1,3), P1 (0,4)</span>\n" +
"                </button>\n" +
"            </div>\n" +
"        </section>\n" +
"\n" +
"        <!-- Main Simulator Grid -->\n" +
"        <div class=\"grid-main\">\n" +
"            <!-- Left Column: Inputs & Processes -->\n" +
"            <div class=\"card\">\n" +
"                <div class=\"card-header\">\n" +
"                    <h2 class=\"card-title\">Configuration</h2>\n" +
"                    <button class=\"btn-danger-sm\" onclick=\"resetAll()\">Clear All</button>\n" +
"                </div>\n" +
"\n" +
"                <div class=\"form-group\">\n" +
"                    <label>Scheduling Algorithm</label>\n" +
"                    <div class=\"algo-selector\">\n" +
"                        <button type=\"button\" id=\"btnAlgoPriority\" class=\"algo-btn active\" onclick=\"selectAlgorithm('Priority')\">Priority (Non-preemptive)</button>\n" +
"                        <button type=\"button\" id=\"btnAlgoRR\" class=\"algo-btn\" onclick=\"selectAlgorithm('Round Robin')\">Round Robin</button>\n" +
"                    </div>\n" +
"                </div>\n" +
"\n" +
"                <div class=\"form-group\" id=\"quantumGroup\" style=\"display: none;\">\n" +
"                    <label for=\"quantumInput\">Time Quantum (ms)</label>\n" +
"                    <input type=\"number\" id=\"quantumInput\" class=\"form-control\" value=\"2\" min=\"1\">\n" +
"                </div>\n" +
"\n" +
"                <div class=\"form-group\">\n" +
"                    <div style=\"display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;\">\n" +
"                        <label>Process Table</label>\n" +
"                        <button class=\"btn-danger-sm\" style=\"background: rgba(56, 189, 248, 0.2); color: var(--primary); border-color: var(--primary);\" onclick=\"addProcessRow()\">+ Add Process</button>\n" +
"                    </div>\n" +
"                    <div class=\"process-table-wrapper\">\n" +
"                        <table class=\"proc-table\" id=\"processInputTable\">\n" +
"                            <thead>\n" +
"                                <tr>\n" +
"                                    <th>PID</th>\n" +
"                                    <th>Arrival</th>\n" +
"                                    <th>Burst</th>\n" +
"                                    <th>Priority</th>\n" +
"                                    <th></th>\n" +
"                                </tr>\n" +
"                            </thead>\n" +
"                            <tbody id=\"processTableBody\">\n" +
"                                <!-- Injected dynamically -->\n" +
"                            </tbody>\n" +
"                        </table>\n" +
"                    </div>\n" +
"                    <div style=\"font-size: 0.72rem; color: var(--text-muted); margin-top: 4px;\">\n" +
"                        * Note: In Priority scheduling, a lower number means a higher priority. All times in ms.\n" +
"                    </div>\n" +
"                </div>\n" +
"\n" +
"                <div id=\"validationAlert\" style=\"display: none;\"></div>\n" +
"\n" +
"                <div class=\"btn-action-row\">\n" +
"                    <button class=\"btn btn-primary\" onclick=\"runSimulation()\">&#9654; Run Simulation</button>\n" +
"                </div>\n" +
"            </div>\n" +
"\n" +
"            <!-- Right Column: Gantt Chart, Analytics & Visualizers -->\n" +
"            <div class=\"card\">\n" +
"                <div class=\"card-header\">\n" +
"                    <h2 class=\"card-title\">Simulation Output & Gantt Chart</h2>\n" +
"                    <div id=\"sortedOrderBadge\" style=\"font-size: 0.8rem; color: var(--text-secondary);\"></div>\n" +
"                </div>\n" +
"\n" +
"                <!-- Gantt Chart Container -->\n" +
"                <div class=\"gantt-container\">\n" +
"                    <div style=\"font-size: 0.8rem; font-weight: 600; color: var(--text-secondary);\">VISUAL TIMELINE</div>\n" +
"                    <div class=\"gantt-chart\" id=\"ganttTimeline\">\n" +
"                        <div style=\"margin: auto; color: var(--text-muted); font-size: 0.85rem;\">Run simulation or select a test case to display the Gantt chart.</div>\n" +
"                    </div>\n" +
"                    <div style=\"font-size: 0.8rem; font-weight: 600; color: var(--text-secondary);\">OUTPUT CONSOLE STRING</div>\n" +
"                    <div class=\"gantt-text-output\" id=\"ganttTextOutput\">Gantt: -</div>\n" +
"                </div>\n" +
"\n" +
"                <!-- Step-by-step Interactive Animator -->\n" +
"                <div class=\"queue-visualizer\">\n" +
"                    <div style=\"display: flex; justify-content: space-between; align-items: center;\">\n" +
"                        <div style=\"font-size: 0.8rem; font-weight: 700; color: var(--primary); text-transform: uppercase;\">\n" +
"                            Data Structure State: <span id=\"queueTypeTitle\">Ready Queue</span>\n" +
"                        </div>\n" +
"                        <div class=\"sim-controls\">\n" +
"                            <button class=\"btn-danger-sm\" onclick=\"stepBack()\">&#9198; Prev</button>\n" +
"                            <button class=\"btn-danger-sm\" id=\"playPauseBtn\" onclick=\"togglePlay()\">&#9658; Play</button>\n" +
"                            <button class=\"btn-danger-sm\" onclick=\"stepForward()\">Next &#9197;</button>\n" +
"                            <span id=\"stepTimeLabel\" style=\"font-family: 'Fira Code', monospace; font-size: 0.8rem; color: #fff;\">t = 0 ms</span>\n" +
"                        </div>\n" +
"                    </div>\n" +
"                    <div class=\"queue-items\" id=\"queueItemsContainer\">\n" +
"                        <span style=\"color: var(--text-muted); font-size: 0.8rem;\">Queue empty</span>\n" +
"                    </div>\n" +
"                    <div id=\"stepActionDesc\" style=\"font-size: 0.8rem; color: var(--text-secondary); font-style: italic;\">Ready.</div>\n" +
"                </div>\n" +
"\n" +
"                <!-- Stats Cards -->\n" +
"                <div class=\"stats-grid\">\n" +
"                    <div class=\"stat-card\">\n" +
"                        <span class=\"stat-label\">Avg Waiting Time</span>\n" +
"                        <span class=\"stat-val primary\" id=\"avgWTVal\">-</span>\n" +
"                    </div>\n" +
"                    <div class=\"stat-card\">\n" +
"                        <span class=\"stat-label\">Avg Turnaround Time</span>\n" +
"                        <span class=\"stat-val accent\" id=\"avgTATVal\">-</span>\n" +
"                    </div>\n" +
"                    <div class=\"stat-card\">\n" +
"                        <span class=\"stat-label\">Total Time</span>\n" +
"                        <span class=\"stat-val\" id=\"totalTimeVal\">-</span>\n" +
"                    </div>\n" +
"                    <div class=\"stat-card\">\n" +
"                        <span class=\"stat-label\">CPU Utilization</span>\n" +
"                        <span class=\"stat-val\" id=\"cpuUtilVal\">-</span>\n" +
"                    </div>\n" +
"                </div>\n" +
"\n" +
"                <!-- Detailed Process Metrics Table -->\n" +
"                <div style=\"margin-top: 8px;\">\n" +
"                    <div style=\"font-size: 0.8rem; font-weight: 600; color: var(--text-secondary); margin-bottom: 8px;\">CALCULATED PROCESS METRICS</div>\n" +
"                    <div class=\"process-table-wrapper\">\n" +
"                        <table class=\"proc-table\">\n" +
"                            <thead>\n" +
"                                <tr>\n" +
"                                    <th>PID</th>\n" +
"                                    <th>Arrival</th>\n" +
"                                    <th>Burst</th>\n" +
"                                    <th>Priority</th>\n" +
"                                    <th>Completion (CT)</th>\n" +
"                                    <th>Turnaround (TAT)</th>\n" +
"                                    <th>Waiting (WT)</th>\n" +
"                                </tr>\n" +
"                            </thead>\n" +
"                            <tbody id=\"resultsTableBody\">\n" +
"                                <tr><td colspan=\"7\" style=\"text-align: center; color: var(--text-muted);\">No simulation results yet.</td></tr>\n" +
"                            </tbody>\n" +
"                        </table>\n" +
"                    </div>\n" +
"                </div>\n" +
"            </div>\n" +
"        </div>\n" +
"    </div>\n" +
"\n" +
"    <script>\n" +
"        // Global State\n" +
"        let currentAlgorithm = 'Priority';\n" +
"        let processes = [\n" +
"            { id: 'P1', at: 0, bt: 3, priority: 3 },\n" +
"            { id: 'P2', at: 1, bt: 2, priority: 1 },\n" +
"            { id: 'P3', at: 2, bt: 1, priority: 2 }\n" +
"        ];\n" +
"        let lastResult = null;\n" +
"        let currentStepIdx = 0;\n" +
"        let playInterval = null;\n" +
"\n" +
"        const processColors = {\n" +
"            'P1': '#38bdf8',\n" +
"            'P2': '#ec4899',\n" +
"            'P3': '#a855f7',\n" +
"            'P4': '#eab308',\n" +
"            'P5': '#10b981',\n" +
"            'P6': '#f97316',\n" +
"            'P7': '#06b6d4',\n" +
"            'P8': '#8b5cf6',\n" +
"            'IDLE': '#475569'\n" +
"        };\n" +
"\n" +
"        function getColor(id) {\n" +
"            if (processColors[id]) return processColors[id];\n" +
"            return '#94a3b8';\n" +
"        }\n" +
"\n" +
"        function selectAlgorithm(algo) {\n" +
"            currentAlgorithm = algo;\n" +
"            document.getElementById('btnAlgoPriority').classList.toggle('active', algo === 'Priority');\n" +
"            document.getElementById('btnAlgoRR').classList.toggle('active', algo === 'Round Robin');\n" +
"            document.getElementById('quantumGroup').style.display = (algo === 'Round Robin') ? 'flex' : 'none';\n" +
"            document.getElementById('queueTypeTitle').innerText = (algo === 'Round Robin') ? 'Array-based Circular Queue' : 'Min-Heap Priority Queue';\n" +
"        }\n" +
"\n" +
"        function renderProcessInputs() {\n" +
"            const tbody = document.getElementById('processTableBody');\n" +
"            tbody.innerHTML = '';\n" +
"            processes.forEach((p, idx) => {\n" +
"                const tr = document.createElement('tr');\n" +
"                tr.innerHTML = `\n" +
"                    <td><input type=\"text\" class=\"input-compact\" style=\"width: 60px; font-weight: 700; color: ${getColor(p.id)}\" value=\"${p.id}\" onchange=\"updateProc(${idx}, 'id', this.value)\"></td>\n" +
"                    <td><input type=\"number\" class=\"input-compact\" style=\"width: 65px;\" value=\"${p.at}\" onchange=\"updateProc(${idx}, 'at', this.value)\"></td>\n" +
"                    <td><input type=\"number\" class=\"input-compact\" style=\"width: 65px;\" value=\"${p.bt}\" onchange=\"updateProc(${idx}, 'bt', this.value)\"></td>\n" +
"                    <td><input type=\"number\" class=\"input-compact\" style=\"width: 65px;\" value=\"${p.priority}\" onchange=\"updateProc(${idx}, 'priority', this.value)\"></td>\n" +
"                    <td><button class=\"btn-danger-sm\" onclick=\"removeProcessRow(${idx})\">&times;</button></td>\n" +
"                `;\n" +
"                tbody.appendChild(tr);\n" +
"            });\n" +
"        }\n" +
"\n" +
"        function updateProc(idx, field, val) {\n" +
"            if (field === 'id') {\n" +
"                processes[idx].id = val.trim();\n" +
"            } else {\n" +
"                processes[idx][field] = parseInt(val, 10);\n" +
"            }\n" +
"        }\n" +
"\n" +
"        function addProcessRow() {\n" +
"            const nextNum = processes.length + 1;\n" +
"            processes.push({ id: 'P' + nextNum, at: nextNum - 1, bt: 2, priority: nextNum });\n" +
"            renderProcessInputs();\n" +
"        }\n" +
"\n" +
"        function removeProcessRow(idx) {\n" +
"            processes.splice(idx, 1);\n" +
"            renderProcessInputs();\n" +
"        }\n" +
"\n" +
"        function resetAll() {\n" +
"            processes = [];\n" +
"            renderProcessInputs();\n" +
"            clearOutputs();\n" +
"        }\n" +
"\n" +
"        function clearOutputs() {\n" +
"            document.getElementById('ganttTimeline').innerHTML = '<div style=\"margin: auto; color: var(--text-muted); font-size: 0.85rem;\">No simulation run yet.</div>';\n" +
"            document.getElementById('ganttTextOutput').innerText = 'Gantt: -';\n" +
"            document.getElementById('avgWTVal').innerText = '-';\n" +
"            document.getElementById('avgTATVal').innerText = '-';\n" +
"            document.getElementById('totalTimeVal').innerText = '-';\n" +
"            document.getElementById('cpuUtilVal').innerText = '-';\n" +
"            document.getElementById('resultsTableBody').innerHTML = '<tr><td colspan=\"7\" style=\"text-align: center; color: var(--text-muted);\">No simulation results.</td></tr>';\n" +
"            document.getElementById('queueItemsContainer').innerHTML = '<span style=\"color: var(--text-muted); font-size: 0.8rem;\">Queue empty</span>';\n" +
"            document.getElementById('validationAlert').style.display = 'none';\n" +
"        }\n" +
"\n" +
"        function loadTestCase(tcNum) {\n" +
"            clearOutputs();\n" +
"            if (tcNum === 1) {\n" +
"                selectAlgorithm('Priority');\n" +
"                processes = [\n" +
"                    { id: 'P1', at: 0, bt: 3, priority: 3 },\n" +
"                    { id: 'P2', at: 1, bt: 2, priority: 1 },\n" +
"                    { id: 'P3', at: 2, bt: 1, priority: 2 }\n" +
"                ];\n" +
"            } else if (tcNum === 2) {\n" +
"                selectAlgorithm('Priority');\n" +
"                processes = [\n" +
"                    { id: 'P1', at: 0, bt: 4, priority: 1 }\n" +
"                ];\n" +
"            } else if (tcNum === 3) {\n" +
"                selectAlgorithm('Priority');\n" +
"                processes = [\n" +
"                    { id: 'P1', at: 0, bt: -2, priority: 1 }\n" +
"                ];\n" +
"            } else if (tcNum === 4) {\n" +
"                selectAlgorithm('Round Robin');\n" +
"                document.getElementById('quantumInput').value = 2;\n" +
"                processes = [\n" +
"                    { id: 'P2', at: 1, bt: 3, priority: 1 },\n" +
"                    { id: 'P1', at: 0, bt: 4, priority: 1 }\n" +
"                ];\n" +
"            }\n" +
"            renderProcessInputs();\n" +
"            runSimulation();\n" +
"        }\n" +
"\n" +
"        // Client-side simulation fallback in case backend server is unreachable\n" +
"        function simulateLocally(procs, algo, quantum) {\n" +
"            for (let p of procs) {\n" +
"                if (p.at < 0) return { success: false, error: 'Invalid arrival time. It cannot be negative.' };\n" +
"                if (p.bt <= 0) return { success: false, error: 'Invalid burst time. It must be greater than 0.' };\n" +
"                if (p.priority <= 0) return { success: false, error: 'Invalid priority. It must be greater than 0.' };\n" +
"            }\n" +
"            if (algo === 'Round Robin' && quantum <= 0) {\n" +
"                return { success: false, error: 'Invalid time quantum. It must be greater than 0.' };\n" +
"            }\n" +
"\n" +
"            // Stable sort by arrival time\n" +
"            let sorted = procs.map((p, i) => ({ ...p, order: i, rem: p.bt })).sort((a, b) => {\n" +
"                if (a.at !== b.at) return a.at - b.at;\n" +
"                return a.order - b.order;\n" +
"            });\n" +
"\n" +
"            let sortedOrder = sorted.map(p => p.id).join(', ');\n" +
"            let ganttSegments = [];\n" +
"            let completed = [];\n" +
"            let steps = [];\n" +
"            let time = 0;\n" +
"            let n = sorted.length;\n" +
"\n" +
"            if (algo === 'Priority') {\n" +
"                let readyHeap = [];\n" +
"                let arrivalIdx = 0;\n" +
"                while (completed.length < n) {\n" +
"                    while (arrivalIdx < n && sorted[arrivalIdx].at <= time) {\n" +
"                        readyHeap.push(sorted[arrivalIdx]);\n" +
"                        arrivalIdx++;\n" +
"                    }\n" +
"                    if (readyHeap.length === 0) {\n" +
"                        if (arrivalIdx < n) {\n" +
"                            let idleStart = time;\n" +
"                            time = sorted[arrivalIdx].at;\n" +
"                            ganttSegments.push({ id: 'IDLE', start: idleStart, end: time, isIdle: true });\n" +
"                        }\n" +
"                        continue;\n" +
"                    }\n" +
"                    readyHeap.sort((a, b) => {\n" +
"                        if (a.priority !== b.priority) return a.priority - b.priority;\n" +
"                        if (a.at !== b.at) return a.at - b.at;\n" +
"                        return a.order - b.order;\n" +
"                    });\n" +
"                    let curr = readyHeap.shift();\n" +
"                    let start = time;\n" +
"                    let end = start + curr.bt;\n" +
"                    time = end;\n" +
"                    curr.ct = end;\n" +
"                    curr.tat = curr.ct - curr.at;\n" +
"                    curr.wt = curr.tat - curr.bt;\n" +
"                    ganttSegments.push({ id: curr.id, start, end, isIdle: false });\n" +
"                    while (arrivalIdx < n && sorted[arrivalIdx].at <= time) {\n" +
"                        readyHeap.push(sorted[arrivalIdx]);\n" +
"                        arrivalIdx++;\n" +
"                    }\n" +
"                    completed.push(curr);\n" +
"                    steps.push({\n" +
"                        time: end,\n" +
"                        action: `Process ${curr.id} executed to completion.`,\n" +
"                        activeProcess: curr.id,\n" +
"                        queue: readyHeap.map(x => `${x.id}(Pr:${x.priority})`)\n" +
"                    });\n" +
"                }\n" +
"            } else {\n" +
"                // Round Robin\n" +
"                let queue = [];\n" +
"                let arrivalIdx = 0;\n" +
"                if (arrivalIdx < n && sorted[arrivalIdx].at === 0) {\n" +
"                    while (arrivalIdx < n && sorted[arrivalIdx].at === 0) {\n" +
"                        queue.push(sorted[arrivalIdx]);\n" +
"                        arrivalIdx++;\n" +
"                    }\n" +
"                } else if (arrivalIdx < n) {\n" +
"                    time = sorted[arrivalIdx].at;\n" +
"                    ganttSegments.push({ id: 'IDLE', start: 0, end: time, isIdle: true });\n" +
"                    while (arrivalIdx < n && sorted[arrivalIdx].at === time) {\n" +
"                        queue.push(sorted[arrivalIdx]);\n" +
"                        arrivalIdx++;\n" +
"                    }\n" +
"                }\n" +
"\n" +
"                while (completed.length < n) {\n" +
"                    if (queue.length === 0) {\n" +
"                        if (arrivalIdx < n) {\n" +
"                            let idleStart = time;\n" +
"                            time = sorted[arrivalIdx].at;\n" +
"                            ganttSegments.push({ id: 'IDLE', start: idleStart, end: time, isIdle: true });\n" +
"                            while (arrivalIdx < n && sorted[arrivalIdx].at <= time) {\n" +
"                                queue.push(sorted[arrivalIdx]);\n" +
"                                arrivalIdx++;\n" +
"                            }\n" +
"                        }\n" +
"                        continue;\n" +
"                    }\n" +
"                    let curr = queue.shift();\n" +
"                    let exec = Math.min(quantum, curr.rem);\n" +
"                    let start = time;\n" +
"                    let end = start + exec;\n" +
"                    ganttSegments.push({ id: curr.id, start, end, isIdle: false });\n" +
"\n" +
"                    // Arrived while running enters queue first\n" +
"                    while (arrivalIdx < n && sorted[arrivalIdx].at <= end) {\n" +
"                        queue.push(sorted[arrivalIdx]);\n" +
"                        arrivalIdx++;\n" +
"                    }\n" +
"                    curr.rem -= exec;\n" +
"                    time = end;\n" +
"                    if (curr.rem > 0) {\n" +
"                        queue.push(curr);\n" +
"                    } else {\n" +
"                        curr.ct = end;\n" +
"                        curr.tat = curr.ct - curr.at;\n" +
"                        curr.wt = curr.tat - curr.bt;\n" +
"                        completed.push(curr);\n" +
"                    }\n" +
"                    steps.push({\n" +
"                        time: end,\n" +
"                        action: `Executed ${curr.id} (${start}-${end} ms). Remaining: ${curr.rem} ms`,\n" +
"                        activeProcess: curr.id,\n" +
"                        queue: queue.map(x => `${x.id}(rem:${x.rem})`)\n" +
"                    });\n" +
"                }\n" +
"                completed.sort((a, b) => a.order - b.order);\n" +
"            }\n" +
"\n" +
"            let totalWT = completed.reduce((sum, p) => sum + p.wt, 0);\n" +
"            let totalTAT = completed.reduce((sum, p) => sum + p.tat, 0);\n" +
"            let avgWT = totalWT / n;\n" +
"            let avgTAT = totalTAT / n;\n" +
"\n" +
"            let ganttStr = ganttSegments.filter(s => !s.isIdle).map(s => `${s.id}(${s.start}-${s.end})`).join(' ');\n" +
"            let metricsStr = (completed.length === 1)\n" +
"                ? `${completed[0].id}: WT ${completed[0].wt}, TAT ${completed[0].tat}`\n" +
"                : 'WT: ' + completed.map(p => `${p.id} ${p.wt}`).join(', ') + ' | TAT: ' + completed.map(p => `${p.id} ${p.tat}`).join(', ');\n" +
"            let avgStr = `Avg WT: ${avgWT.toFixed(2)} | Avg TAT: ${avgTAT.toFixed(2)}`;\n" +
"\n" +
"            return {\n" +
"                success: true,\n" +
"                algorithm: algo,\n" +
"                quantum,\n" +
"                sortedOrder,\n" +
"                ganttString: ganttStr,\n" +
"                metricsString: metricsStr,\n" +
"                averagesString: avgStr,\n" +
"                avgWaitingTime: avgWT,\n" +
"                avgTurnaroundTime: avgTAT,\n" +
"                ganttSegments,\n" +
"                processes: completed,\n" +
"                steps\n" +
"            };\n" +
"        }\n" +
"\n" +
"        async function runSimulation() {\n" +
"            const alertDiv = document.getElementById('validationAlert');\n" +
"            alertDiv.style.display = 'none';\n" +
"\n" +
"            const quantum = parseInt(document.getElementById('quantumInput').value, 10) || 2;\n" +
"            const payload = {\n" +
"                algorithm: currentAlgorithm,\n" +
"                quantum: quantum,\n" +
"                processes: processes\n" +
"            };\n" +
"\n" +
"            let result;\n" +
"            try {\n" +
"                // Attempt to call Java embedded server\n" +
"                const res = await fetch('/api/simulate', {\n" +
"                    method: 'POST',\n" +
"                    headers: { 'Content-Type': 'application/json' },\n" +
"                    body: JSON.stringify(payload)\n" +
"                });\n" +
"                result = await res.json();\n" +
"            } catch (err) {\n" +
"                // Fallback to local simulation in browser\n" +
"                result = simulateLocally(processes, currentAlgorithm, quantum);\n" +
"            }\n" +
"\n" +
"            if (!result.success) {\n" +
"                alertDiv.className = 'alert-error';\n" +
"                alertDiv.innerHTML = `&#9888; ${result.error}`;\n" +
"                alertDiv.style.display = 'flex';\n" +
"                clearOutputs();\n" +
"                return;\n" +
"            }\n" +
"\n" +
"            lastResult = result;\n" +
"            displayResults(result);\n" +
"        }\n" +
"\n" +
"        function displayResults(data) {\n" +
"            // Sorted order badge\n" +
"            const sortedDiv = document.getElementById('sortedOrderBadge');\n" +
"            if (data.sortedOrder) {\n" +
"                sortedDiv.innerText = 'Sorted by arrival: ' + data.sortedOrder;\n" +
"            } else {\n" +
"                sortedDiv.innerText = '';\n" +
"            }\n" +
"\n" +
"            // Gantt Chart Visualization\n" +
"            const timeline = document.getElementById('ganttTimeline');\n" +
"            timeline.innerHTML = '';\n" +
"            const totalDuration = data.ganttSegments.length > 0 ? data.ganttSegments[data.ganttSegments.length - 1].end : 0;\n" +
"\n" +
"            data.ganttSegments.forEach(seg => {\n" +
"                const dur = seg.end - seg.start;\n" +
"                const flexGrow = Math.max(dur, 1);\n" +
"                const block = document.createElement('div');\n" +
"                block.className = 'gantt-block';\n" +
"                block.style.flex = `${flexGrow} 0 0`;\n" +
"                block.style.backgroundColor = seg.isIdle ? '#334155' : getColor(seg.id);\n" +
"                block.style.color = seg.isIdle ? '#94a3b8' : '#0f172a';\n" +
"                block.innerHTML = `\n" +
"                    <div style=\"font-weight: 700; margin-bottom: 12px;\">${seg.id}</div>\n" +
"                    <div class=\"gantt-time-labels\">\n" +
"                        <span>${seg.start}</span>\n" +
"                        <span>${seg.end}</span>\n" +
"                    </div>\n" +
"                `;\n" +
"                timeline.appendChild(block);\n" +
"            });\n" +
"\n" +
"            // Gantt String and metrics\n" +
"            document.getElementById('ganttTextOutput').innerText = 'Gantt: ' + data.ganttString;\n" +
"            document.getElementById('avgWTVal').innerText = data.avgWaitingTime.toFixed(2) + ' ms';\n" +
"            document.getElementById('avgTATVal').innerText = data.avgTurnaroundTime.toFixed(2) + ' ms';\n" +
"            document.getElementById('totalTimeVal').innerText = totalDuration + ' ms';\n" +
"\n" +
"            // Calculate CPU utilization\n" +
"            let idleTime = data.ganttSegments.filter(s => s.isIdle).reduce((acc, s) => acc + (s.end - s.start), 0);\n" +
"            let busyTime = totalDuration - idleTime;\n" +
"            let cpuUtil = totalDuration > 0 ? ((busyTime / totalDuration) * 100).toFixed(1) : '100';\n" +
"            document.getElementById('cpuUtilVal').innerText = cpuUtil + '%';\n" +
"\n" +
"            // Results table\n" +
"            const resBody = document.getElementById('resultsTableBody');\n" +
"            resBody.innerHTML = '';\n" +
"            data.processes.forEach(p => {\n" +
"                const tr = document.createElement('tr');\n" +
"                tr.innerHTML = `\n" +
"                    <td style=\"font-weight: 700; color: ${getColor(p.id)}\">${p.id}</td>\n" +
"                    <td>${p.at} ms</td>\n" +
"                    <td>${p.bt} ms</td>\n" +
"                    <td>${p.priority}</td>\n" +
"                    <td style=\"font-weight: 600; color: #fff;\">${p.ct} ms</td>\n" +
"                    <td style=\"font-weight: 600; color: var(--accent);\">${p.tat} ms</td>\n" +
"                    <td style=\"font-weight: 600; color: var(--primary);\">${p.wt} ms</td>\n" +
"                `;\n" +
"                resBody.appendChild(tr);\n" +
"            });\n" +
"\n" +
"            // Initialize animation step to end\n" +
"            if (data.steps && data.steps.length > 0) {\n" +
"                currentStepIdx = data.steps.length - 1;\n" +
"                renderStep(currentStepIdx);\n" +
"            }\n" +
"        }\n" +
"\n" +
"        function renderStep(idx) {\n" +
"            if (!lastResult || !lastResult.steps || lastResult.steps.length === 0) return;\n" +
"            const step = lastResult.steps[idx];\n" +
"            document.getElementById('stepTimeLabel').innerText = `t = ${step.time} ms`;\n" +
"            document.getElementById('stepActionDesc').innerText = step.action;\n" +
"\n" +
"            const queueDiv = document.getElementById('queueItemsContainer');\n" +
"            queueDiv.innerHTML = '';\n" +
"            if (step.queue && step.queue.length > 0) {\n" +
"                step.queue.forEach(item => {\n" +
"                    const node = document.createElement('span');\n" +
"                    node.className = 'queue-node';\n" +
"                    node.innerText = item;\n" +
"                    queueDiv.appendChild(node);\n" +
"                });\n" +
"            } else {\n" +
"                queueDiv.innerHTML = '<span style=\"color: var(--text-muted); font-size: 0.8rem;\">Queue empty</span>';\n" +
"            }\n" +
"        }\n" +
"\n" +
"        function stepBack() {\n" +
"            if (playInterval) togglePlay();\n" +
"            if (currentStepIdx > 0) {\n" +
"                currentStepIdx--;\n" +
"                renderStep(currentStepIdx);\n" +
"            }\n" +
"        }\n" +
"\n" +
"        function stepForward() {\n" +
"            if (playInterval) togglePlay();\n" +
"            if (lastResult && lastResult.steps && currentStepIdx < lastResult.steps.length - 1) {\n" +
"                currentStepIdx++;\n" +
"                renderStep(currentStepIdx);\n" +
"            }\n" +
"        }\n" +
"\n" +
"        function togglePlay() {\n" +
"            const btn = document.getElementById('playPauseBtn');\n" +
"            if (playInterval) {\n" +
"                clearInterval(playInterval);\n" +
"                playInterval = null;\n" +
"                btn.innerHTML = '&#9658; Play';\n" +
"            } else {\n" +
"                if (!lastResult || !lastResult.steps || lastResult.steps.length === 0) return;\n" +
"                if (currentStepIdx >= lastResult.steps.length - 1) {\n" +
"                    currentStepIdx = 0;\n" +
"                }\n" +
"                btn.innerHTML = '&#10074;&#10074; Pause';\n" +
"                playInterval = setInterval(() => {\n" +
"                    if (currentStepIdx < lastResult.steps.length - 1) {\n" +
"                        currentStepIdx++;\n" +
"                        renderStep(currentStepIdx);\n" +
"                    } else {\n" +
"                        togglePlay();\n" +
"                    }\n" +
"                }, 1000);\n" +
"            }\n" +
"        }\n" +
"\n" +
"        function generateReport() {\n" +
"            if (!lastResult) {\n" +
"                alert('Please run a simulation first before generating a report.');\n" +
"                return;\n" +
"            }\n" +
"            let report = `# RUNGTA INTERNATIONAL SKILLS UNIVERSITY\\n` +\n" +
"                `## School of Computer Science and Engineering\\n` +\n" +
"                `### Project PS No. 80: CPU Scheduling Simulator Report\\n\\n` +\n" +
"                `**Algorithm:** ${lastResult.algorithm}\\n` +\n" +
"                (lastResult.quantum ? `**Quantum:** ${lastResult.quantum} ms\\n` : '') +\n" +
"                (lastResult.sortedOrder ? `**Sorted by arrival:** ${lastResult.sortedOrder}\\n` : '') +\n" +
"                `**Gantt Chart:** ${lastResult.ganttString}\\n` +\n" +
"                `**Process Metrics:** ${lastResult.metricsString}\\n` +\n" +
"                `**Averages:** ${lastResult.averagesString}\\n\\n` +\n" +
"                `| Process ID | Arrival Time | Burst Time | Priority | Completion Time | Turnaround Time | Waiting Time |\\n` +\n" +
"                `|---|---|---|---|---|---|---|\\n`;\n" +
"\n" +
"            lastResult.processes.forEach(p => {\n" +
"                report += `| ${p.id} | ${p.at} ms | ${p.bt} ms | ${p.priority} | ${p.ct} ms | ${p.tat} ms | ${p.wt} ms |\\n`;\n" +
"            });\n" +
"\n" +
"            const blob = new Blob([report], { type: 'text/markdown' });\n" +
"            const url = URL.createObjectURL(blob);\n" +
"            const a = document.createElement('a');\n" +
"            a.href = url;\n" +
"            a.download = `CPU_Scheduling_Report_${lastResult.algorithm.replace(/\\s+/g, '_')}.md`;\n" +
"            a.click();\n" +
"        }\n" +
"\n" +
"        // Initial Load\n" +
"        window.onload = function() {\n" +
"            renderProcessInputs();\n" +
"            runSimulation();\n" +
"        };\n" +
"    </script>\n" +
"</body>\n" +
"</html>";
    }
}
