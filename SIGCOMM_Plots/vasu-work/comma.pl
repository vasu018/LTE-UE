#!/usr/bin/perl




    open( my $fh, '<', "./dropcam_2.txt" ) or die "Can't open $filename: $!";
    while ( my $line = <$fh> ) {
        my @arr = split(/,/, $line);
            print $arr[2];
    }
    close $fh;
