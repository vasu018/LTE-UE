#!/usr/bin/perl -w
  
my $filename = $ARGV[0];

my $outputfile = "./sort_latency1.txt";
my $count = 0;
my $total = 0;

my @filearray = ();
open(INPUTFILE, $filename);
#while (<INPUTFILE>) {
#    my $currentLine = $_;
#    print "$currentLine";
#    push @filearray, $_;
#
#}
#print @filearray;

while (<INPUTFILE>) {
    my $line = $_;
    chomp($line);
    #$line =~ s/,/ /g;
    my @array = split(/,/, $line);
    my @sorted_array = sort { $a <=> $b } @array;
    for my $val (@sorted_array) {
        chomp($val);
        #print "vasu\n";
        if ($val > 0) {
            #print OUTPUTFILE "$val\n";
            print "$count: $val, $total\n";
            $total = $total + $val;
            $count = $count +1;
        }
    }
}
close(INPUTFILE);

my $average = $total/$count;

print "Average for $filename: $average\n";

