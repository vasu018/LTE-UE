#!/usr/bin/perl -w


open (OUTPUTFILE, "> ./handoverDecomp_manipulated.txt");
open (FILE, "./handover-niave-decomp.txt");

while (<FILE>) {
    my $line = $_;
    chomp($line);
    $line =~ s/,/ /g;
    my @array = split(/\s/, $line);
    my @sorted_array = sort { $a <=> $b } @array;
    for my $val (@sorted_array) { 
        chomp($val);
        #if ($val > 0) {
            print OUTPUTFILE "$val\n";
            #print "$val\n";
        #}
    }
}
close(FILE);
close(OUTPUTFILE);


open (OUTPUTFILE, "> ./handoverMixed_manipulated.txt");
open (FILE, "./handover-mixed.txt");

while (<FILE>) {
    my $line = $_;
    chomp($line);
    $line =~ s/,/ /g;
    my @array = split(/\s/, $line);
    my @sorted_array = sort { $a <=> $b } @array;
    for my $val (@sorted_array) { 
        chomp($val);
        #if ($val > 0) {
            print OUTPUTFILE "$val\n";
            #print "$val\n";
        #}
        #print "$val\n";
    }
}
close(FILE);
close(OUTPUTFILE);


open (OUTPUTFILE, "> ./serviceMixed_manipulated.txt");
open (FILE, "./service-mixed.txt");

while (<FILE>) {
    my $line = $_;
    chomp($line);
    $line =~ s/,/ /g;
    my @array = split(/\s/, $line);
    my @sorted_array = sort { $a <=> $b } @array;
    for my $val (@sorted_array) { 
        chomp($val);
        #if ($val > 0) {
            print OUTPUTFILE "$val\n";
            #print "$val\n";
        #}
        #print "$val\n";
    }
}
close(FILE);
close(OUTPUTFILE);

open (OUTPUTFILE, "> ./serviceDecomp_manipulated.txt");
open (FILE, "./service-niave-decomp.txt");

while (<FILE>) {
    my $line = $_;
    chomp($line);
    $line =~ s/,/ /g;
    my @array = split(/\s/, $line);
    my @sorted_array = sort { $a <=> $b } @array;
    for my $val (@sorted_array) { 
        chomp($val);
        #if ($val > 0) {
            print OUTPUTFILE "$val\n";
            #print "$val\n";
        #}
        #print "$val\n";
    }
}
close(FILE);
close(OUTPUTFILE);
