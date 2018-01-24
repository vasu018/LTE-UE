#!/usr/bin/perl -w

my $serial = 0;
my $data1 = 0;
open (OUTPUTFILE, "> ./scale_data.txt");
my $i =0;
my $totalrange = 1200;
for ($i =0; $i <1200; $i++) {

    if ($i >= $totalrange/2) {
        if ($i % 5 eq 0) {
            $data1 = $data1 - 100;
        }
    }
    else {
        if ($i % 5 eq 0) {
            $data1 = $data1 + 100;
        }
    }

    print OUTPUTFILE "$serial, $data1\n";
    print "$serial,$data1\n";
    $serial = $serial +1;
}
close(OUTPUTFILE);
