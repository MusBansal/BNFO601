__author__ = 'YOUR NAME HERE'
import re

class Fragment(object):

    """ I am providing for you here a user-defined type that will keep track of all of the information for a restriction
    fragment.  The instance variables and the methods tell (or should) the whole story.  Study the code, there's at
    least one nice trick here worth knowing.
    """

    def __init__(self, fragment_name_or_number, fragment_length, begin_position, end_position, fragment_sequence):

        self.fragment_name_or_number = fragment_name_or_number
        self.fragment_length = fragment_length
        self.begin_position = begin_position
        self.end_position = end_position
        self.fragment_sequence = fragment_sequence

    def __str__(self): # Special method attribute so that Fragment objects know how to print themselves

        return ('>Fragment ' + str(self.fragment_name_or_number) + ' of ' + str(self.fragment_length) + ' NT '
                + '(' + str(self.begin_position) + '..' + str(self.end_position) + ')\n' + self.fragment_sequence)

    def __lt__(self, other):        # This method implements a "less than" comparison between two Fragment objects
                                    # Amazingly, this is the only comparison operator you need to implement to make
                                    # a user-defined type sortable using the built-in sort functionality.

        return self.fragment_length < other.fragment_length  # Fragment length is being used as the basis for sorting

class DNAdigest(object):

    """
    PURPOSE: Open a file with a single DNA sequence in FastA format
             Analyze the DNA sequence for restriction endonuclease cut sites
             and do various other things specified in the exam materials.
    INPUT FILES:
             sequence_file: input file containing a single sequence in FA format

    OUTPUT FILE:
                output file of DNA fragments produced by the digestions
                Annotation is fragment number, length, fragment begin, and fragment end positions
    """


    def __init__(self, sequence_file=None, recognition_sequence=r'GAATTC', bond_position=1):

        """
        PURPOSE: The only jobs of the initializer will be to:
            1.  Compile a regular expression corresponding to the restriction enzyme recognition sequence, and save this
                as an instance variable self.RE_RE (for Restriction Enzyme Regular Expression... cute, right?)
            2.  Create an instance variable self.bond_position that keeps track of the position within the recognition
                sequence where the phosphodiester bond is actually cut.
            3.  Create an instance variable self.cut_positions that for now is an empty list.  Later we will populate it
                with positions in the sequence we have read in where cut sites were found.
            4. Open the input sequence file, ignore the annotation line, and populate an instance variable self.sequence
               for use elsewhere in the program
        """

        self.RE_RE = # something here, see docstring comment
        self.bond_position = bond_position
        self.sequence = ''
        self.cut_positions = []
        self.fragment_info = []

        if sequence_file:

            # Do a bunch of stuff to read in the sequence file into a variable self.sequence.
            # Make sure to ignore the header / annotation line

        else:

            self.sequence = 'BNNNGAATTCNNNNNNNNNNNNNNNNNNNNGAATTCCNNNNNNNNNNNNNNNNNNNNNNNNNNNNNE'
            # a sequence containing a couple of EcoRI cut sites, just for testing.

        print ('Total length of sequence was', len(self.sequence), 'base pairs')

        #print (self.sequence)

    def search_for_cuts(self):

        """
        This method will populate the instance variable list self.cut_positions with the locations of the cut sites

        Clue 1:  Consider using the finditer method to search your sequence.
        Clue 2:  There are useful methods associated with match objects, one of which is ideal for reporting cut sites
        Clue 3:  Don't forget to account for the bond position where the cut actually occurs
        Clue 4:  It's OK to track cut positions internally "pythonically" (i.e. zero indexing) instead of biologically
                 (i.e. first residue is numbered 1).  Don't forget to add one though later when you finally report!
        """

        #  some stuff here. See clues above.

        return self.cut_positions

    def report_cuts(self, output_file=None, sort_by_length=True):

        """
        This method should do three things.

        First, it should figure out the actual DNA sequence of the fragments
        produced.
        We are going to simplify here in two ways... first, we assume that the DNA we are cutting is linear,
        so we don't have to worry about a fragment that spans position 0.  The second simplifying assumption is to
        ignore the sticky ends issue.  So the cut site position should correspond just to the position in the DNA where
        the phosphodiester bond was cut (so for a G/AATTC cutter, we would just have a first fragment 5'...NNNNG - 3',
        and a second fragment 5' - AATTCNNN... - 3'  etc.).

        Second, it should populate a list self.fragment_info with Fragment objects that summarize each fragment.
         Fragments should known their fragment number (start from 1), fragment length,
         start position in original sequence (this should be the BIOLOGICAL position), the end position in the
         original sequence (again, biological sequence coordinates), and finally a string with the actual DNA sequence.

        Third, it should either print (if argument output_file=None) or send to a file (if argument output_file is any
        other string) in fastA format the fragments.  If argument sort_by_length=True, these should be sorted by
        fragment length, otherwise, just the default ordering by fragment number.

        """

        if not self.cut_positions:   # Check and see if the cut position array has been populated.

            self.search_for_cuts()   # If not, go ahead and do so by invoking the search_for_cuts method

        last_begin = 0
        last_end = len(self.sequence)

        i = 0

        # some kind of loop to instantiate fragment objects

        # Don't forget to append the fragment created by the last cut until the end of the sequence

        #  Code to optionally sort the list fragements by fragment length depending on sort_by_length boolean

        if output_file:

            pass # something actally meaningful here to write things to an output file

        else:

            for frag in self.fragment_info:

                print (frag)


    def observed_and_expected(self):

        """ You'll need to provide some code here mostly on your own. On the "observed" side, using this method
        presupposes that the genome has already been searched for fragments.
        The "expected" side of things is a bit more open ended with respect to possible approaches.  At a minumum,
        you'll probably also need to do some other type of analysis of the input file, and perhaps of the recognition
        sequence you searched for.
        """

        print ('We observed', number_of_observed_fragments,'of average length', average_length_of_observed_fragments)
        print ("We expected", expected_number_of_fragments, 'of average length', average_length_of_expected_fragements)

        print ('Observed over Expected fragment number', number_of_observed_fragments/expected_number_of_fragments)
        print ('Observed over Expected average fragment length', average_length_of_observed_fragments/
                                                                 average_length_of_expected_fragements)


    def __calculate_GC(self, sequence):

        """
        It may turn out to be handy to have a method that calculates the GC percentage.
        This private method should take a sequence string as an argument and returns a float corresponding to
        GC percentage.
        """

        # do something with sequence

        return GC_percent

def main():

    #myDigest = DNAdigest('mystery_genome.fasta', 'AAGCTT', 1)  ## version for the actual mystery sequence
    myDigest = DNAdigest()  # Use the default arguments for quick testing

    print ('Cuts occurred at nucleotides', ', '.join(map(str, myDigest.search_for_cuts())))
    # if you have properly implemented search for cuts, it returns a list of cut positions.
    # The map function here is a handy way to take the numeric values of cut positions and convert them to strings
    # for printing here.


    myDigest.report_cuts() #  Version for testing that will just print to the screen
    #myDigest.report_cuts('YOURNAME_digest_output.txt', False)  # version for producing actual output file


if __name__ == '__main__':
    main()