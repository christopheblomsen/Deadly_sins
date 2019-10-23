import matplotlib.pyplot as plt
import numpy as np

def extract_error(filename):
    #a function to extract_data from a file of information that I have called lnsum_output.txt
    with open(filename, "r") as infile: #opens and reads the file as infile

        epsilon = [] #creates empty lists for the values, just like my life
        exactError = []
        n = []

        for line in infile: #runs through the lines in the file

            if line.startswith("epsilon"): #observed in file that I was only interested in the lines starting with this

                stripper = line.strip() #strips away at both side of the line
                splitter = stripper.split(",") #splits up the family over some left over supper
                #seriously thou, I really wanted that chicken
                #ohh the variable, that makes a new list and splits it at ","

                for i in range(len(splitter)): #runs through the new list

                    if splitter[i].startswith(" "): #checks if the string starts with whitespace
                        hooters = splitter[i].lstrip() #goes down to nearest hooters and removes the emptiness inside you, and all whitespace

                        if hooters.startswith("exact error"): #checks if hooters started with exact error
                            playboy = hooters.split(":") #splits up the family a bit more with that :

                            exactError.append(float(playboy[1])) #adds playboy to the exactError you just made,
                            #wife will use this against you in the future

                        elif hooters.startswith("n"): #checks if there was any n(ude) people at hooters
                            lotus = hooters.split("=") #splits at =, this ain't hooters this is lotus

                            n.append(float(lotus[1])) #adds lotus to n(umber of times you f'ed uped)

                    elif splitter[i].startswith("epsilon"): #checke if the string starts with epsilon
                        divorce = splitter[i].split(":") #wife finally had enough, splits list at :

                        epsilon.append(float(divorce[1])) #adds divorce to epsilon list

        epsilon = np.array(epsilon); exactError = np.array(exactError); n = np.array(n) #turns all list to array

        return epsilon, exactError, n #returns the arrays


epsilon, exactError, n = extract_error("lnsum_output.txt") #gets the arrays from lnsum_output.txt

plt.title("Ln sum errors") #a title for your failures
plt.semilogy(epsilon, n, label="epsilon") #plots with a logarithmic y axis
plt.semilogy(exactError, n, label="exact error")
plt.legend() #Barny stinson box
plt.show() #shows the plot
