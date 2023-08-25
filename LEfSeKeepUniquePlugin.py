import sys

class LEfSeKeepUniquePlugin:
 def input(self, inputfile):
   self.infile = open(inputfile, 'r')
 def run(self):
   pass
 def output(self, outputfile):
   outfile = open(outputfile, 'w')

   taxa = []
   for line in self.infile:
    contents = line.split('\t')
    taxon = contents[0]
    if (taxon not in taxa):
        taxa.append(taxon)
        outfile.write(line)
