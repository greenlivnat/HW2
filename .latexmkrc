# latexmk configuration: LuaLaTeX + biber, class and figures found under ./latex
$pdf_mode = 4;                       # 4 = lualatex
my $inc = (`lualatex --version` =~ /MiKTeX/) ? '--include-directory=latex ' : '';   # MiKTeX ignores TEXINPUTS
$lualatex = "lualatex $inc-interaction=nonstopmode -file-line-error -halt-on-error %O %S";
$bibtex_use = 2;                     # run biber when needed
$max_repeat = 6;
my $sep = ($^O =~ /MSWin32|cygwin|msys/) ? ';' : ':';
$ENV{'TEXINPUTS'} = './latex//' . $sep . ($ENV{'TEXINPUTS'} // '');
