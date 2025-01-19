# Intro
This tool is used to generate the report for [OSMR](https://www.offsec.com/courses/exp-312/) exam.

This is a modified version of [OSCP-Exam-Report-Template-Markdown](https://github.com/noraj/OSCP-Exam-Report-Template-Markdown) to suit OSMR exam requirements.

# Installation
## Requirements

- [Pandoc](https://pandoc.org/installing.html)
- LaTeX (eg. [TeX Live](http://www.tug.org/texlive/)) in order to get `pdflatex` or `xelatex`
- [Eisvogel Pandoc LaTeX PDF Template](https://github.com/Wandmalfarbe/pandoc-latex-template#installation)
- [p7zip](http://p7zip.sourceforge.net/) (if you want to use the script, for generating the archive)

- ArchLinux 

```
pacman -S texlive-most pandoc p7zip
```

- openSUSE 

```
zypper in texlive-scheme-medium pandoc p7zip-full
```

- Ubuntu: 

```
sudo apt-get install pandoc texlive-fonts-extra texlive-latex-extra texlive-latex-recommended texlive-latex-base p7zip-full
```

## Downloading `eisvogel`

```
mkdir templates
wget https://raw.githubusercontent.com/Wandmalfarbe/pandoc-latex-template/8114319d5c2c17f4d047ebf7ecddd20446b2518d/eisvogel.tex -O templates/eisvogel.latex
```

## How to use

First, set your OSID in `generate.py`.

Next, write your report in `src/OSMR.md` and your assignments in `assignments/assignment*`.

Once done, generate your report with:

```
$ ./generate.py
Generating the report...
Generating archive...
```

The report and the archive have been generated:

```
$ ls output
OSMR-OS-XXXXX-Exam-Report.7z  OSMR-OS-XXXXX-Exam-Report.pdf
```

To preview the generated PDF open `OSMR-OS-XXXXX-Exam-Report.pdf`.

`OSMR-OS-XXXXX-Exam-Report.7z` archive will contain the PDF along with the assignment files stored in `assignments/` directory.

```
$ ls
OSMR-OS-XXXXX-Exam-Report.7z
$ 7z x OSMR-OS-XXXXX-Exam-Report.7z
...
$ tree
.
├── assignment1.sh
├── assignment2.c
├── assignment3.m
├── assignment4.c
├── OSMR-OS-XXXXX-Exam-Report.7z
└── OSMR-OS-XXXXX-Exam-Report.pdf
```

What you need to submit to Offsec is only `OSMR-OS-XXXXX-Exam-Report.7z`.
