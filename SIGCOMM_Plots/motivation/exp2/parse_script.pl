#!/usr/bin/perl -w

open(FILE_SF, ">./data_sf.txt");
open(FILE_SL, ">./data_sl.txt");

open(FILE, "./service_10000_sf.txt");
while(<FILE>) {
    my @arr = split(/,/,$_);
    foreach my $entry (@arr) {
        chomp($entry);
        if ($entry) {
            print FILE_SF "$entry\n",
        }
    }
}
close(FILE);

open(FILE, "./service_10000_sl.txt");
while(<FILE>) {
    my @arr = split(/,/,$_);
    foreach my $entry (@arr) {
        chomp($entry);
        if ($entry) {
            print FILE_SL "$entry\n",
        }
    }
}
close(FILE);


close(FILE_SF);
close(FILE_SL);
