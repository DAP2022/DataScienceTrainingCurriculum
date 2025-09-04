def ORFadvisor(DNA):
    if len(DNA)%3==0:
        #print("The DNA sequence is divisible by 3!")
        if DNA[0]=="A" and DNA[1] =="T" and DNA[2]=="G":
            print("The DNA sequence is divisible by 3 AND the start codon is here!")
            #if DNA[-3=="T"] and DNA[-2=="G|A"] and DNA[-1=="A|G"]:
            if DNA[-3:] in {"TAA", "TAG", "TGA"}:
                print("Hurray - this is a possible ORF")
            else:
                print("It is divisible by three, and has a start codon, but there is no Stop codon" )
        else:
            print("Divisible by 3, but no start codon.")
    else:
        print("The string is not even divisible by 3")