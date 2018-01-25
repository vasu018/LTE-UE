#!/usr/bin/perl -w

`perl data_gen_tx_rate.pl`;
`python data2_gen_nf_scale_latency.py`;
`python scaleplot.py`;
`python latencyplot.py`;
