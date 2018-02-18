set datafile separator "\t"
set terminal png size 900,400
set title "Web Traffic"
set ylabel "Requests per second"
set xlabel "Time"
set xdata time
set timefmt "%s"
set format x "%s"
set key left top
set grid
plot "graph.tsv" using 1:3 with lines lw 2 title '500s', "graph.tsv" using 1:4 with lines lw 2 title '200s', "graph.tsv" using 1:5 with lines lw 2 title '404s'
