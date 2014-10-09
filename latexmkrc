$pdflatex=q/pdflatex %O -shell-escape %S/;
$hash_calc_ignore_pattern{'pdf'} = '^/CreationDate |^/ModDate |^/ID \\[<';
