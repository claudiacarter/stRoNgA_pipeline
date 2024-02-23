with open(r"C:\Users\clauc\PycharmProjects\pythonProject\results.fa", "r") as fasta:
    total_fasta = fasta.readlines()
    lines_per_file = 50
    new_file_num = 0
    current_file = []
    count = 0
    while bool(total_fasta):
        for line in total_fasta:
            current_file.append(line)
            count += 1
            if count >= lines_per_file:
                break
        with open(f"fastasplit_{new_file_num}.fa", "w") as file:
             for line in current_file:
                 file.write(line)
             new_file_num += 1
        total_fasta = [line for line in total_fasta if line not in current_file]
        current_file = []
        count = 0

print(f"Split input FASTA to create {new_file_num + 1} FASTA files each containing {lines_per_file/2} sequences.")