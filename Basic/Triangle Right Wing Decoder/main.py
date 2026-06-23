def decode(message_file):
    with open(message_file, 'r') as f:
        content = f.readlines()
    dic = {int(line.split()[0]):line.split()[1] for line in content}
    right_wing = [i*(i+1)/2 for i in range(1,len(dic)+1)]
    output = ' '.join([dic[num] for num in right_wing if num in dic])
    return output

print(decode('coding_qual_input.txt'))

