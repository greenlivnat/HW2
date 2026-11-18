% aibook.cls — custom, reusable class for the Hebrew book
% "מאחורי הקלעים של הבינה המלאכותית". Engine: LuaLaTeX. Bibliography: biblatex (IEEE) + biber.
% The version is checked by the qa-cls-version skill (scripts/qa.py cls-version): keep
% \aibook@version, the \ProvidesClass date/version and CHANGELOG below in sync.
%
% CHANGELOG
%   1.0.0 (2026-11-18) first version: palette, RTL-safe content boxes, chapter openers,
%                      banner header and footer, cover, figure/table helpers, IEEE bibliography.
%   1.1.0 (2026-11-18) Detector r1 fixes: Ligatures=NoCommon on Hebrew font families (reversed
%                      "fi" in RTL, IR-10); content boxes unbreakable (frame lost across pages,
%                      IR-09); keywordsbox environment (raw tcolorbox in main.tex, IR-11);
%                      \raggedbottom and float fractions (white gaps, D-m5a-08).
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{aibook}[2026/11/18 v1.1.0 Hebrew popular-science book class (LuaLaTeX)]
\def\aibook@version{1.1.0}

\RequirePackage{iftex}
\ifluatex\else
  \ClassError{aibook}{Compile with LuaLaTeX (latexmk -lualatex)}{The class supports LuaLaTeX only.}
\fi

\LoadClass[11pt,a4paper,oneside,openany]{book}

% ---------------------------------------------------------------- page and colour
\RequirePackage[top=27mm,bottom=25mm,inner=22mm,outer=22mm,headheight=16pt,headsep=9mm,footskip=12mm]{geometry}
\RequirePackage{xcolor}
\definecolor{midnight}{HTML}{101B35}
\definecolor{turquoise}{HTML}{00C9C8}
\definecolor{violet}{HTML}{7956D8}
\definecolor{gold}{HTML}{E4B65C}
\definecolor{paper}{HTML}{F5F7FA}
\definecolor{turqtext}{HTML}{007F7E}   % darker turquoise for text on light background (contrast)
\colorlet{lightturq}{turquoise!9!white}
\colorlet{lightviolet}{violet!8!white}
\colorlet{lightgold}{gold!14!white}
\pagecolor{paper}
\color{midnight}

% ---------------------------------------------------------------- graphics BEFORE polyglossia
% (load order rule from CLAUDE.md / incident IR-01: graphicx, tikz and tcolorbox come first)
\RequirePackage{graphicx}
\RequirePackage{tikz}
\usetikzlibrary{positioning,arrows.meta,calc,shapes.geometric,fit,backgrounds,decorations.pathmorphing}
\RequirePackage[most]{tcolorbox}
\RequirePackage{amsmath,amssymb}
\RequirePackage{booktabs,array,tabularx,colortbl}
\RequirePackage{enumitem}
\RequirePackage{titlesec,titletoc}
\RequirePackage{fancyhdr}
\RequirePackage{caption}
\RequirePackage{etoolbox}
\RequirePackage[hidelinks,unicode,bookmarksnumbered]{hyperref}

% ---------------------------------------------------------------- language and fonts
\RequirePackage{fontspec}
\RequirePackage{polyglossia}
\setmainlanguage{hebrew}
\setotherlanguage{english}
\setmainfont{Assistant}[Scale=1.0]
\setsansfont{Assistant}
% Ligatures=NoCommon: in RTL runs LuaTeX/HarfBuzz reverses Latin "fi" ("artfiicial", IR-10)
\newfontfamily\hebrewfont[Script=Hebrew,Ligatures=NoCommon]{Assistant}
\newfontfamily\hebrewfontsf[Script=Hebrew,Ligatures=NoCommon]{Assistant}
\newfontfamily\headingfont[Script=Hebrew,Ligatures=NoCommon]{Assistant ExtraBold}
\newfontfamily\lightfont[Script=Hebrew,Ligatures=NoCommon]{Assistant Light}
\setmonofont{Latin Modern Mono}[Scale=0.95]
\newfontfamily\hebrewfonttt[Script=Hebrew,Ligatures=NoCommon]{Assistant}
% Bibliography: IEEE numeric style, citation order (biblatex must follow polyglossia)
\RequirePackage[style=ieee,backend=biber,sorting=none,dashed=false,doi=true,url=true,isbn=false]{biblatex}
\DeclareFieldFormat{url}{\url{#1}}
\linespread{1.18}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.55em plus 0.15em}
\emergencystretch=2em
\raggedbottom                         % no stretched white gaps between paragraphs (D-m5a-08)
\renewcommand{\topfraction}{0.85}\renewcommand{\bottomfraction}{0.6}
\renewcommand{\textfraction}{0.12}\renewcommand{\floatpagefraction}{0.75}

% Hebrew names (explicit, so they do not depend on polyglossia defaults)
\AtBeginDocument{%
  \renewcommand{\contentsname}{תוכן העניינים}%
  \renewcommand{\listfigurename}{רשימת איורים}%
  \renewcommand{\listtablename}{רשימת טבלאות}%
  \renewcommand{\figurename}{איור}%
  \renewcommand{\tablename}{טבלה}%
  \renewcommand{\chaptername}{פרק}%
  \renewcommand{\appendixname}{נספח}}

% ---------------------------------------------------------------- RTL-safe box wrapper
% LuaTeX + polyglossia: a tcolorbox placed in an RTL paragraph is shifted outside the text
% block (found in M5A smoke test, see docs/INCIDENTS.md IR-05). Fix: typeset the box frame
% left-to-right and switch the content back to right-to-left.
\newcommand{\aibook@rtl}{\pardir TRT\textdir TRT}
\tcbset{
  aibook/base/.style={enhanced,unbreakable,arc=2.5mm,boxrule=0.9pt,left=4mm,right=4mm,top=2.5mm,bottom=2.5mm,
    fonttitle=\headingfont\small,coltitle=midnight,before upper=\aibook@rtl,before lower=\aibook@rtl,
    before title=\aibook@rtl,halign title=flush left,toptitle=0.8mm,bottomtitle=0.8mm,
    before skip=1.1em,after skip=1.1em},
}
\newenvironment{aibook@ltrbox}[1]{%
  \par\begingroup\pardir TLT\textdir TLT%
  \begin{tcolorbox}[#1]}{\end{tcolorbox}\endgroup\par}

% icon glyphs drawn in TikZ (no external images)
\newcommand{\aibook@icon}[1]{\leavevmode\hbox dir TLT{\tikz[baseline=-0.6ex,scale=0.9]{#1}}}
\newcommand{\icongears}{\aibook@icon{\draw[white,line width=1.2pt] (0,0) circle (0.13); \foreach \a in {0,45,...,315}{\draw[white,line width=1.6pt] (\a:0.13) -- (\a:0.21);}}}
\newcommand{\iconquestion}{\aibook@icon{\node[white,font=\bfseries\small,inner sep=0pt]{?};}}
\newcommand{\iconflask}{\aibook@icon{\draw[white,line width=1pt,line join=round] (-0.06,0.2)--(-0.06,0.05)--(-0.18,-0.17)--(0.18,-0.17)--(0.06,0.05)--(0.06,0.2);}}
\newcommand{\iconbulb}{\aibook@icon{\draw[midnight,line width=1pt] (0,0.05) circle (0.13); \draw[midnight,line width=1pt] (-0.06,-0.12)--(0.06,-0.12) (-0.05,-0.18)--(0.05,-0.18);}}
\newcommand{\iconscales}{\aibook@icon{\draw[white,line width=1pt] (0,-0.18)--(0,0.18) (-0.2,0.12)--(0.2,0.12) (-0.2,0.12)--(-0.26,-0.02)--(-0.14,-0.02)--cycle (0.2,0.12)--(0.14,-0.02)--(0.26,-0.02)--cycle;}}

% Five content boxes (docs/STYLE_GUIDE.md section 4)
\newenvironment{behindbox}[1]{\begin{aibook@ltrbox}{aibook/base,colback=white,colframe=midnight,
    borderline west={3pt}{0pt}{turquoise},colbacktitle=midnight,coltitle=white,
    title={\icongears\enspace מאחורי הקלעים: #1}}}{\end{aibook@ltrbox}}
\newenvironment{thinkbox}{\begin{aibook@ltrbox}{aibook/base,colback=lightviolet,colframe=violet,
    colbacktitle=violet,coltitle=white,title={\iconquestion\enspace רגע של מחשבה}}}{\end{aibook@ltrbox}}
\newenvironment{labbox}[1]{\begin{aibook@ltrbox}{aibook/base,colback=lightturq,colframe=turquoise,
    colbacktitle=midnight,coltitle=white,title={\iconflask\enspace במעבדה: #1}}}{\end{aibook@ltrbox}}
\newenvironment{conceptbox}[1]{\begin{aibook@ltrbox}{aibook/base,colback=lightgold,colframe=gold,
    colbacktitle=gold,coltitle=midnight,title={\iconbulb\enspace מושג שכדאי להכיר: #1}}}{\end{aibook@ltrbox}}
\newenvironment{mythbox}{\begin{aibook@ltrbox}{aibook/base,colback=white,colframe=violet,
    colbacktitle=violet,coltitle=white,title={\iconscales\enspace מיתוס מול מציאות},
    segmentation style={draw=turquoise,line width=0.8pt,dashed},colbacklower=lightturq}}{\end{aibook@ltrbox}}
\newenvironment{keywordsbox}{\begin{aibook@ltrbox}{aibook/base,colback=lightturq,colframe=turquoise,
    before skip=1.5em}{\headingfont מילות מפתח:}\enspace}{\end{aibook@ltrbox}}
\newcommand{\mythlabel}{{\headingfont\color{violet}מיתוס: }}
\newcommand{\realitylabel}{{\headingfont\color{turqtext}מציאות: }}
\newenvironment{insightsbox}{\begin{aibook@ltrbox}{aibook/base,colback=midnight!4!white,colframe=midnight,
    boxrule=0pt,borderline north={2.5pt}{0pt}{gold},colbacktitle=midnight,coltitle=gold,
    title={תובנות מרכזיות}}}{\end{aibook@ltrbox}}
% Visible placeholder: the qa-typeset skill fails the build if any remains in the PDF.
\newcommand{\placeholder}[1]{\begin{aibook@ltrbox}{aibook/base,colback=red!6!white,colframe=red!70!black,
    title={סימון מקום (חסר תוכן)}}#1\end{aibook@ltrbox}}

\setlist{itemsep=0.25em,topsep=0.4em,leftmargin=1.4em}
\setlist[itemize]{label={\textcolor{turquoise}{\small$\blacktriangleleft$}}}

% ---------------------------------------------------------------- chapter openers
\newcommand{\aibook@question}{}
\newcommand{\chapterquestion}[1]{\gdef\aibook@question{#1}}
\titleformat{\chapter}[display]
  {\headingfont\color{midnight}}
  {}{0pt}
  {\aibook@chapterbanner}
  [\aibook@printquestion]
\titlespacing*{\chapter}{0pt}{-12mm}{6mm}
\newif\ifaibook@app
\newcommand{\aibook@chapterlabel}{\ifaibook@app נספח\else\ifnum\c@chapter>0 \chaptername\ \thechapter\fi\fi}
\newcommand{\bookappendix}{\appendix\aibook@apptrue\renewcommand{\thechapter}{נ}\setcounter{chapter}{0}}
\newcommand{\aibook@chapterbanner}[1]{%
  \hbox dir TLT to \textwidth\bgroup\begin{tikzpicture}
    \fill[midnight,rounded corners=3mm] (0,0) rectangle (\textwidth,32mm);
    \fill[turquoise] (0,0) rectangle (\textwidth,1.2mm);
    \foreach \x/\y/\c in {8/22/turquoise,16/12/violet,24/25/gold,30/8/turquoise,38/18/violet}
      {\fill[\c,opacity=0.55] (\x mm,\y mm) circle (1.1mm);}
    \draw[turquoise,opacity=0.35] (8mm,22mm)--(16mm,12mm)--(24mm,25mm)--(30mm,8mm)--(38mm,18mm)--(24mm,25mm);
    \node[anchor=north east,text=gold,font=\headingfont\large,inner sep=0pt] at (\textwidth-7mm,26mm)
      {\textdir TRT\aibook@chapterlabel};
    \node[anchor=south east,text=white,font=\headingfont\fontsize{24}{28}\selectfont,inner sep=0pt,
      text width=\textwidth-58mm,align=right] at (\textwidth-7mm,6mm) {\textdir TRT #1};
  \end{tikzpicture}\hss\egroup}
\newcommand{\aibook@printquestion}{%
  \ifx\aibook@question\empty\else
    \par\vspace{5mm}{\lightfont\fontsize{16}{22}\selectfont\color{midnight}\aibook@question\par}%
    \vspace{1mm}{\color{gold}\rule{28mm}{1.6pt}}\par
  \fi\gdef\aibook@question{}}
\titleformat{\section}{\headingfont\Large\color{midnight}}{\textcolor{turqtext}{\thesection}}{0.7em}{}
\titlespacing*{\section}{0pt}{1.4em}{0.5em}
\titleformat{\subsection}{\headingfont\large\color{midnight}}{}{0pt}{}

% ---------------------------------------------------------------- header banner and footer
\newcommand{\booktitle}{מאחורי הקלעים של הבינה המלאכותית}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\fancyhead[C]{\hbox dir TLT to \textwidth\bgroup\begin{tikzpicture}
    \fill[midnight] (0,0) rectangle (\textwidth,5.2mm);
    \fill[turquoise] (0,0) rectangle (\textwidth,0.6mm);
    \node[anchor=east,text=white,font=\small\headingfont,inner sep=0pt] at (\textwidth-3mm,2.9mm) {\textdir TRT\booktitle};
    \node[anchor=west,text=turquoise,font=\small,inner sep=0pt] at (3mm,2.9mm) {\textdir TRT\leftmark};
  \end{tikzpicture}\hss\egroup}
\fancyfoot[C]{\hbox dir TLT to \textwidth\bgroup\begin{tikzpicture}
    \draw[gold,line width=0.6pt] (0,0) -- (0.42\textwidth,0);
    \draw[gold,line width=0.6pt] (0.58\textwidth,0) -- (\textwidth,0);
    \node[circle,fill=midnight,text=white,font=\small\headingfont,minimum size=7mm,inner sep=0pt] at (0.5\textwidth,0) {\thepage};
  \end{tikzpicture}\hss\egroup}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\hbox dir TLT{\tikz{\node[circle,fill=midnight,text=white,font=\small\headingfont,minimum size=7mm,inner sep=0pt]{\thepage};}}}}
\fancypagestyle{frontmatter}{\fancyhf{}\fancyfoot[C]{\small\color{midnight!70}\thepage}}

% ---------------------------------------------------------------- floats and captions
\captionsetup{font={small},labelfont={bf,color=midnight},textfont={color=midnight},labelsep=colon,skip=6pt}
\captionsetup[figure]{position=bottom}
\captionsetup[table]{position=top}
\renewcommand{\thefigure}{\thechapter.\arabic{figure}}
\renewcommand{\thetable}{\thechapter.\arabic{table}}
\newcommand{\figurenote}[1]{\par\vspace{2pt}{\footnotesize\color{midnight!75}#1\par}}
\newcommand{\booktablerule}{\arrayrulecolor{turquoise}}
\newcolumntype{R}{>{\raggedleft\arraybackslash}X}
% Tables: RTL-safe wrapper, header row on Midnight Blue
\newcommand{\tablehead}[1]{\rowcolor{midnight}#1}
\newcommand{\tabhead}[1]{{\color{white}\headingfont #1}}

% ---------------------------------------------------------------- diagrams
% TikZ diagrams are laid out left-to-right (coordinates) while every node is typeset RTL.
\tikzset{
  he/.style={execute at begin node={\textdir TRT}},   % no \pardir here: see IR-05
  blk/.style={draw=midnight,line width=0.8pt,rounded corners=2mm,fill=white,align=center,inner sep=2.2mm},
  flow/.style={-{Stealth[length=2.6mm]},line width=1pt,draw=turquoise},
  loop/.style={-{Stealth[length=2.6mm]},line width=1pt,draw=violet,dashed},
  num/.style={circle,fill=midnight,text=white,font=\scriptsize\headingfont,inner sep=0pt,minimum size=4.2mm},
}
% The picture lives in an explicit left-to-right box; nodes switch only \textdir (IR-05).
\newenvironment{bookdiagram}[1][]{\par\noindent\hbox dir TLT to \linewidth\bgroup\hss
  \begin{tikzpicture}[he,font=\small,#1]}{\end{tikzpicture}\hss\egroup\par}
\newcommand{\ltrbox}[1]{\hbox dir TLT{#1}}

% ---------------------------------------------------------------- misc helpers
\newcommand{\en}[1]{\textenglish{#1}}
\newcommand{\projref}[1]{{\footnotesize\color{midnight!70}[#1]}}
\setcounter{tocdepth}{1}
\titlecontents{chapter}[0pt]{\addvspace{0.6em}\headingfont\color{midnight}}
  {\contentslabel[\textcolor{turqtext}{\thecontentslabel}]{2.2em}}{}{\titlerule*[0.6pc]{.}\contentspage}
\titlecontents{section}[2.2em]{\small}{\contentslabel{2.6em}}{}{\titlerule*[0.6pc]{.}\contentspage}

% Cover: drawn in TikZ, deterministic (fixed seed), no external images.
\newcommand{\makecover}[3]{% #1 title, #2 subtitle, #3 bottom line
  \begin{titlepage}\thispagestyle{empty}
  \hbox dir TLT\bgroup\begin{tikzpicture}[remember picture,overlay]
    \fill[midnight] (current page.south west) rectangle (current page.north east);
    \pgfmathsetseed{1998}
    \begin{scope}[shift={(current page.south west)}]
      \foreach \i in {1,...,46}{%
        \pgfmathsetmacro{\px}{0.6+rnd*19.8}\pgfmathsetmacro{\py}{9.5+rnd*19.0}%
        \expandafter\xdef\csname aibook@cx\i\endcsname{\px}%
        \expandafter\xdef\csname aibook@cy\i\endcsname{\py}%
        \coordinate (n\i) at (\px,\py);}
      \foreach \i in {1,...,46}{\foreach \j in {1,...,46}{%
        \ifnum\i<\j
          \pgfmathsetmacro{\dd}{veclen(\csname aibook@cx\i\endcsname-\csname aibook@cx\j\endcsname,
                                       \csname aibook@cy\i\endcsname-\csname aibook@cy\j\endcsname)}%
          \ifdim\dd pt<3.4pt \draw[turquoise,opacity=0.28,line width=0.5pt] (n\i)--(n\j);\fi
        \fi}}
      \foreach \i in {1,...,46}{%
        \pgfmathtruncatemacro{\c}{mod(\i,7)}%
        \ifcase\c \def\col{gold}\or\def\col{turquoise}\or\def\col{violet}\or\def\col{turquoise}\or\def\col{turquoise}\or\def\col{violet}\else\def\col{turquoise}\fi
        \pgfmathsetmacro{\rr}{1.6+mod(\i,3)*0.8}%
        \fill[\col] (n\i) circle (\rr pt);}
      \fill[gold] (2.2,7.2) rectangle (18.8,7.35);
    \end{scope}
    \node[anchor=south east,text=white,font=\headingfont\fontsize{38}{46}\selectfont,text width=16cm,align=right]
      at ($(current page.south west)+(18.8,7.7)$) {\textdir TRT #1};
    \node[anchor=north east,text=turquoise,font=\lightfont\fontsize{17}{22}\selectfont,text width=16cm,align=right]
      at ($(current page.south west)+(18.8,6.7)$) {\textdir TRT #2};
    \node[anchor=south east,text=gold,font=\small,align=right]
      at ($(current page.south west)+(18.8,1.2)$) {\textdir TRT #3};
  \end{tikzpicture}\egroup
  \end{titlepage}}

\endinput
