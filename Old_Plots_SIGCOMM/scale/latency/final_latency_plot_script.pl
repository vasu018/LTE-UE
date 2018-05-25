#!/usr/bin/perl -w

`perl data_gen_latency.pl`;
`python data2_gen_nf_latency.py`;
`python latencyplot.py`;
