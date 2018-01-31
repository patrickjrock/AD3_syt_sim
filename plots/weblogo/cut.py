from Bio import SeqIO
def cut_fasta(start, end, input_file, output_file):
  sequences = []
  for record in SeqIO.parse(input_file, "fasta"):
    seq = record.seq
    cut_seq = seq[start:end]
    record.seq = cut_seq
    sequences.append(record)
  output_f = open(output_file, "w")
  SeqIO.write(sequences, output_f, "fasta")
  output_f.close()

cut_fasta(351, 357, "sutton.fasta", "C2A_cut.fasta")
cut_fasta(510, 516, "sutton.fasta", "C2B_cut.fasta")
