#!/usr/bin/perl -w
  
my $filename = $ARGV[0];

open(INPUTFILE, $filename);
while (<INPUTFILE>) {
    my $currentLine = $_;
    print "$currentLine";
}
close(INPUTFILE);
exit;

open (OUTPUTFILE, "> ./.txt");
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


