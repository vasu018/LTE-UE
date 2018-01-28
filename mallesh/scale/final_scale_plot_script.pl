#!/usr/bin/perl -w

`perl data_gen_tx_rate.pl`;
`python data2_gen_nf_scale.py`;
`python scaleplot.py`;
#`python latency/data2_gen_nf_latency.py`;
#`python latency/latencyplot.py`;
