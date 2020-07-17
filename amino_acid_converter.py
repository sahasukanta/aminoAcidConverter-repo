from tkinter import *

# for converting list to string
def listToString(lis):
    str1 = ""
    # traverse in the string
    for c in lis:
        str1 = str1 + c
    str1 = str1.replace("\n", "")
    return str1

# for reading string formatted genome into codons and matching with the corresponding protein
def codonToProtein(seq):

    # for converting large genome into codon entries into list format
    codon_list = [(seq[i:i+3]) for i in range(0, len(seq), 3)]

    # for reading codons into corresponding protein and creating a new list with protein letters
    # list 1 to return as a str for direct output
    # list 2 to return for further operations to create amino acid counter dict.
    protein_list1 = []
    protein_list2 = []

    for c in codon_list:

        if c == 'UUU' or c == 'UUC':
            protein_list1.append('F')
            protein_list2.append('F')

        elif c == 'UUA' or c == 'UUG' or c == 'CUU' or c == 'CUC' or c == 'CUA' or c == 'CUG':
            protein_list1.append('L')
            protein_list2.append('L')

        elif c == 'UCU' or c == 'UCC' or c == 'UCA' or c == 'UCG' or c == 'AGU' or c == 'AGC':
            protein_list1.append('S')
            protein_list2.append('S')

        elif c == 'UAU' or c == 'UAC':
            protein_list1.append('Y')
            protein_list2.append('Y')

        elif c == 'UGU' or c == 'UGC':
            protein_list1.append('C')
            protein_list2.append('C')

        elif c == 'UGG':
            protein_list1.append('W')
            protein_list2.append('W')

        elif c == 'CCU' or c == 'CCC' or c == 'CCA' or c == 'CCG':
            protein_list1.append('P')
            protein_list2.append('P')

        elif c == 'CAU' or c == 'CAC':
            protein_list1.append('H')
            protein_list2.append('H')

        elif c == 'CAA' or c == 'CAG':
            protein_list1.append('Q')
            protein_list2.append('Q')

        elif c == 'AGA' or c == 'AGG' or c == 'CGU' or c == 'CGC' or c == 'CGA' or c == 'CGG':
            protein_list1.append('R')
            protein_list2.append('R')

        elif c == 'AUU' or c == 'AUC' or c == 'AUA':
            protein_list1.append('I')
            protein_list2.append('I')

        elif c == 'AUG':
            protein_list1.append('M')
            protein_list2.append('M')

        elif c == 'ACU' or c == 'ACC' or c == 'ACA' or c == 'ACG':
            protein_list1.append('T')
            protein_list2.append('T')

        elif c == 'AAU' or c == 'AAC':
            protein_list1.append('N')
            protein_list2.append('N')

        elif c == 'AAA' or c == 'AAG':
            protein_list1.append('K')
            protein_list2.append('K')

        elif c == 'GUU' or c == 'GUC' or c == 'GUA' or c == 'GUG':
            protein_list1.append('V')
            protein_list2.append('V')

        elif c == 'GCU' or c == 'GCC' or c == 'GCA' or c == 'GCG':
            protein_list1.append('A')
            protein_list2.append('A')

        elif c == 'GAU' or c == 'GAC':
            protein_list1.append('D')
            protein_list2.append('D')

        elif c == 'GAA' or c == 'GAG':
            protein_list1.append('E')
            protein_list2.append('E')

        elif c == 'GGU' or c == 'GGC' or c == 'GGA' or c == 'GGG':
            protein_list1.append('G')
            protein_list2.append('G')

        elif c == 'UAA' or c == 'UAG' or c == 'UGA':
            protein_list1.append('~')
            protein_list2.append('~')

        else:
            protein_list1.append('--Stray_Nucleotide(s)--')
    # using created func. to convert protien list into str format
    final_answer = listToString(protein_list1)
    # returning list2 and amino acid sequence (str format)
    return protein_list2, final_answer

# defining the click function: what happens if you click the button
def transcribe_translate():
    global Entry1
    # calling the entry you type into the entry box
    FilePath = Entry1.get()
    # accessing the data in the file from the given path
    fHandle = open(FilePath)
    data_in_list_format = fHandle.readlines()
    # converting to string for operations
    data_in_string = listToString(data_in_list_format)

    # covnerting from DNA to mRNA if required
    if 'T' in data_in_string:
        data_in_string = data_in_string.replace('T', 'U')
    else:
        data_in_string = data_in_string

    # converting to amino acid seq, output is a tuple [0]=a list of all the amino acids, [1]=a string of all amino acids
    protein_seq = codonToProtein(data_in_string)

    # measuring all length parameters
    amino_acid_seq = protein_seq[1]
    len_of_pseq = len(amino_acid_seq)
    len_of_nucleotides = len(data_in_string)

    # correcting measurements
    if amino_acid_seq[-1] == '-' and '~' in amino_acid_seq:
        len_of_pseq = len_of_pseq - 23                         # correcting '--Stray nucleotide(s)--'
        for x in amino_acid_seq:                               # correcting '~' stop codon
            if x == '~':
                len_of_pseq = len_of_pseq - 1
    elif '~' in amino_acid_seq:
        for x in amino_acid_seq:
            if x == '~':
                len_of_pseq = len_of_pseq - 1
    elif amino_acid_seq[-1] == '-':
        len_of_pseq = len_of_pseq - 23
    else:
        len_of_pseq = len_of_pseq

    # creating dict. for counting all the amino acids
    amino_acids = protein_seq[0]
    amino_acid_count = {}
    for amino_acid in amino_acids:
        if amino_acid not in amino_acid_count:
            amino_acid_count[amino_acid] = 1
        else:
            amino_acid_count[amino_acid] = amino_acid_count[amino_acid] + 1

    global a
    a = a + 1
    # variable assignment for all outputs
    output_all = "Run " + str(a) + " done!\n" + "Length of Inserted Nucleotides: " + str(len_of_nucleotides) + "\nLength of Amino Acids: " + str(len_of_pseq) + "\nAmino Acid Count: " + str(amino_acid_count) + "\nConverted Protein Sequence: " + str(amino_acid_seq) + "\n" + "\n"

    # output
    global OutBox
    OutBox.insert(END, output_all)
    fHandle.close()
    # OutBox.config(state=DISABLED)

# clear all button function
def clear_all():
    global Entry1
    global OutBox
    Entry1.delete(0, END)
    Entry1.insert(0, "Enter File Path Here...")
    OutBox.delete(1.0, END)

# initialising GUI
root = Tk()
root.title("Amino Acid Converter")
root["bg"] = "LightBlue1"
root.geometry("583x275")
a = 0

# labels
welcome_label = Label(root, text="Welcome to Amino Acid Converter\n Easily convert your DNA or RNA dataset into amino acid sequence", bg="LightBlue1")
welcome_label.grid(column=2, row=0, columnspan=4, pady=10)

status_label = Label(root, text="...Ready to convert...   (c) by Sukanta Saha", relief=SUNKEN, bd=1, anchor=E, bg="white")
status_label.grid(row=3, column=2, columnspan=4, pady=2, sticky=W+E)

# input box
Entry1 = Entry(root, width=60, borderwidth=3)
Entry1.grid(row=1, column=2, sticky=NSEW)
Entry1.insert(0, "Enter File Path Here...")

# output box
Scrollbar = Scrollbar(root)
OutBox = Text(root, height=10, width=60, borderwidth=4)
Scrollbar.grid(row=2, column=3, sticky=NSEW)
OutBox.grid(row=2, column=2, sticky=E)
Scrollbar.config(command=OutBox.yview)
OutBox.config(yscrollcommand=Scrollbar.set)

# button config.
button1 = Button(root, text="Transcribe\nTranslate", bg="PaleGreen1", command=transcribe_translate)
button1.grid(row=2, column=4, padx=5, pady=5, sticky=NSEW)

button2 = Button(root, text="Clear Data", bg="PaleGreen1", command=clear_all)
button2.grid(row=1, column=3, columnspan=2, sticky=W+E)

# main loop to keep the execution running
root.mainloop()
