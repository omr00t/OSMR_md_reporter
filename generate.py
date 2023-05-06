#!/usr/bin/env python
from subprocess import check_output
from pathlib import Path

# Your OSID
osid    = "OS-XXXXX"

# Template info
osmr_template = {
    "exam"    : "OSMR",
    "name"    : "Official Offensive Security template v1.0",
    "path"    : "src/OSMR.md",
}

md_path = osmr_template["path"]
exam    = osmr_template["exam"]

# Syntax highlight style
style = "breezedark"

# Generating report
print("Generating the report...")
pdf = f"output/{exam}-{osid}-Exam-Report.pdf"

# Assignment paths
assignments = "assignments/assignment*"

resource_path = "".join(md_path.split('/')[:-1])

check_output(f"pandoc {md_path} -o {pdf} \
  --resource-path {resource_path} \
  --from markdown+yaml_metadata_block+raw_html \
  --template eisvogel \
  --table-of-contents \
  --toc-depth 6 \
  --number-sections \
  --top-level-division=chapter \
  --highlight-style {style} \
  --listings", shell=True)

current_path = str(Path(__file__).parent.absolute()) + "/"
print("Generating archive...")
check_output(f"7z a output/{exam}-{osid}-Exam-Report.7z \
        {current_path}{pdf} \
        {current_path}{assignments}", shell=True)
