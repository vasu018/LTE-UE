#!/usr/bin/perl -w

my $modbucket = 5;
my $sparse0 = 1; # should be greater than or equals to 1
my $sparse1 = 1;
my $sparse2 = 1;
my $sparse3 = 1;
my $sparse4 = 1;

my $val5 = 4999;
my $val4 = 3999;
my $val3 = 2999;
my $val2 = 1999;
my $val1 = 999;

my $orig = 0;
my $randomVal1 = 1000;
my $randomVal2 = 500;
my $randomVal3 = 300;
my $randomVal4 = 200;
my $lowerlimit = 1;

open (OUTPUTFILE, "> ./sl_nf_failure_data_modified.txt");
open (FILE, "./sl_nf_data.txt");

if ($orig == 1) {
    while (<FILE>) {
        my $line = $_;
        chomp($line);
        $line =~ s/\s/ /g;
        my @array1 = split(/\s/, $line);
        my $x = $array1[0];
        my $y = $array1[1];
        chomp($x);
        chomp($y);
        print OUTPUTFILE "$x,$y\n";
    }
}
else {
    while (<FILE>) {
        my $line = $_;
        chomp($line);
        $line =~ s/\s/ /g;
        my @array1 = split(/\s/, $line);
        my $x = $array1[0];
        my $y = $array1[1];
        chomp($x);
        chomp($y);
        my $rem = $x*100 % $modbucket;
        if ($x > 78.74 && $x < 79.73) {
            #if ($rem == 0) {
                my $newmod = $modbucket * $sparse2;
                my $rem2 = $x*100 % $newmod;
                #if ($rem2 == 0) {
                    my $rval = 0;
                    if ($randomVal1) {
                        $rval = rand($randomVal2);
                        if ($y < $lowerlimit) {
                            print "$x,$y\n";
                            print OUTPUTFILE "$x,$y\n";
                        }
                        else {
                            $y = $rval;
                            print "$x,$y\n";
                            print OUTPUTFILE "$x,$y\n";
                        }
                    }
                #}
            #}
        }
        if ($x > 80.74 && $x < 81.73) {
            #if ($rem == 1) {
                my $newmod = $modbucket * $sparse2;
                my $rem2 = $x*100 % $newmod;
                #if ($rem2 == 0) {
                    my $rval = 0;
                    if ($randomVal2) {
                        $rval = rand($randomVal2);
                        if ($y < $lowerlimit) {
                            print "$x,$y\n";
                            print OUTPUTFILE "$x,$y\n";
                        }
                        else {
                            $y = $rval;
                            print "$x,$y\n";
                            print OUTPUTFILE "$x,$y\n";
                        }
                    }
                #}
            #}
        }
        if ($x > 81.74 && $x < 82.73) {
            #if ($rem == 2) {
                my $newmod = $modbucket * $sparse2;
                my $rem2 = $x*100 % $newmod;
                #if ($rem2 == 0) {
                    my $rval = 0;
                    if ($randomVal3) {
                        $rval = rand($randomVal3);
                        if ($y < $lowerlimit) {
                            print "$x,$y\n";
                            print OUTPUTFILE "$x,$y\n";
                        }
                        else {
                            $y = $rval;
                            print "$x,$y\n";
                            print OUTPUTFILE "$x,$y\n";
                        }
                    }
                #}
            #}
        }
        if ($x > 82.74 && $x < 83.73) {
            #if ($rem == 3) {
                my $newmod = $modbucket * $sparse2;
                my $rem2 = $x*100 % $newmod;
                #if ($rem2 == 0) {
                    my $rval = 0;
                    if ($randomVal4) {
                        $rval = rand($randomVal4);
                        if ($y < $lowerlimit) {
                            print "$x,$y\n";
                            print OUTPUTFILE "$x,$y\n";
                        }
                        else {
                            $y = $rval;
                            print "$x,$y\n";
                            print OUTPUTFILE "$x,$y\n";
                        }
                    }
                #}
            #}
        }
        if ($x <= 78.74  || $x >= 83.73) {
            if ($y >= 980) {
               ;
            }
            else {
                print "$x,$y\n";
                print OUTPUTFILE "$x,$y\n";
            }
        }
    }
}
close(FILE);
close(OUTPUTFILE);
#if ($x > 78.74 && $x < 88.73) {
