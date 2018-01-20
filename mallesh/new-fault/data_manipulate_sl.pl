#!/usr/bin/perl -w

my $modbucket = 5;
my $sparse0 = 2; # should be greater than or equals to 1
my $sparse1 = 2;
my $sparse2 = 3;
my $sparse3 = 3;
my $sparse4 = 4;

my $val5 = 4999;
my $val4 = 3999;
my $val3 = 2999;
my $val2 = 1999;
my $val1 = 999;

my $orig = 0;
# For no random effect keep lower_limit > randomVal
my $randomVal = 2;
my $lowerlimit = 3;

open (OUTPUTFILE, "> ./sl_host_failure_data.txt");
open (FILE, "./normal.txt");

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
        if ($x > 78.74 && $x < 80.33) {
            # 0, 5
            if ($rem == 0) {
                my $newmod = $modbucket * $sparse0;
                my $rem2 = $x*100 % $newmod;
                if ($rem2 == 0) {
                    $y = $val5;
                    print "Bucket0: $x $y\n";
                    print OUTPUTFILE "$x,$y\n";
                }
                else {
                    my $rval = 0;
                    if ($randomVal) {
                        $rval = rand($randomVal);
                        if ($rval > $lowerlimit) {
                            $y = $rval;
                        }
                    }
                    print "$x,$y\n";
                    print OUTPUTFILE "$x,$y\n";
                }
            }
        }
        if ($x > 79.74 && $x < 80.73) {
            # 1, 6
            if ($rem == 1) {
                my $newmod = $modbucket * $sparse1;
                my $rem2 = $x*100 % $newmod;
                if ($rem2 == 1) {
                    $y = $val4;
                    print "Bucket1: $x $y\n";
                    print OUTPUTFILE "$x,$y\n";
                }
                else {
                    my $rval = 0;
                    if ($randomVal) {
                        $rval = rand($randomVal);
                        if ($rval > $lowerlimit) {
                            $y = $rval;
                        }
                    }
                    print "$x,$y\n";
                    print OUTPUTFILE "$x,$y\n";
                }
            }
        }
        if ($x > 80.74 && $x < 81.73) {
            # 2, 7
            if ($rem == 2) {
                my $newmod = $modbucket * $sparse2;
                my $rem2 = $x*100 % $newmod;
                if ($rem2 == 2) {
                    $y = $val3;
                    print "Bucket2: $x $y\n";
                    print OUTPUTFILE "$x,$y\n";
                }
                else {
                    my $rval = 0;
                    if ($randomVal) {
                        $rval = rand($randomVal);
                        if ($rval > $lowerlimit) {
                            $y = $rval;
                        }
                    }
                    print "$x,$y\n";
                    print OUTPUTFILE "$x,$y\n";
                }
            }
        }
        if ($x > 81.74 && $x < 82.73) {
            # 3, 8
            if ($rem == 3) {
                my $newmod = $modbucket * $sparse3;
                my $rem2 = $x*100 % $newmod;
                if ($rem2 == 3) {
                    $y = $val2;
                    print "Bucket3: $x $y\n";
                    print OUTPUTFILE "$x,$y\n";
                }
                else {
                    my $rval = 0;
                    if ($randomVal) {
                        $rval = rand($randomVal);
                        if ($rval > $lowerlimit) {
                            $y = $rval;
                        }
                    }
                    print "$x,$y\n";
                    print OUTPUTFILE "$x,$y\n";
                }
            }
        }
        if ($x > 82.74 && $x < 83.73) {
            # 4, 9
            if ($rem == 4) {
                my $newmod = $modbucket * $sparse4;
                my $rem2 = $x*100 % $newmod;
                if ($rem2 == 4) {
                    $y = $val1;
                    print "Bucket4: $x $y\n";
                    print OUTPUTFILE "$x,$y\n";
                }
                else {
                    my $rval = 0;
                    if ($randomVal) {
                        $rval = rand($randomVal);
                        if ($rval > $lowerlimit) {
                            $y = $rval;
                        }
                    }
                    print "$x,$y\n";
                    print OUTPUTFILE "$x,$y\n";
                }
            }
        }
        if ($x <= 78.74  || $x >= 83.73) {
            #print "$x,$y\n";
            #print OUTPUTFILE "$x,$y\n";
            if ($y >= 980) {
                ;
            }
            else {
                print "$x,$y\n";
                print OUTPUTFILE "$x,$y\n";
            }
        }
        
        #if ($x < 100) {
        #    if ($y >= 980) {
        #        ;
        #    }
        #    else {
        #        print "$x,$y\n";
        #        print OUTPUTFILE "$x,$y\n";
        #    }
        #} 
    }
}
    close(FILE);
    close(OUTPUTFILE);
#if ($x > 78.74 && $x < 88.73) {
