import time,sys,math
from tabulate import tabulate
from colorama import Fore
from tabulate import tabulate
BWhite='\033[1;37m' 
arg = sys.argv[1]
def banner():
    print(BWhite + Fore.GREEN + """
╔═╗┬─┐┌─┐┌┐ ┌─┐┌┐ ┬┬  ┬┌┬┐┬ ┬  ╔╦╗┬┌─┐┌┬┐┬─┐┬┌┐ ┬ ┬┌┬┐┬┌─┐┌┐┌
╠═╝├┬┘│ │├┴┐├─┤├┴┐││  │ │ └┬┘───║║│└─┐ │ ├┬┘│├┴┐│ │ │ ││ ││││
╩  ┴└─└─┘└─┘┴ ┴└─┘┴┴─┘┴ ┴  ┴   ═╩╝┴└─┘ ┴ ┴└─┴└─┘└─┘ ┴ ┴└─┘┘└┘
                  ╔╦╗┬┌─┐┌─┐┬─┐┌─┐┌┬┐┌─┐
                   ║║│└─┐│  ├┬┘├┤  │ ├┤
                  ═╩╝┴└─┘└─┘┴└─└─┘ ┴ └─┘                                                      """ + Fore.WHITE)
    print("─" * 43)
    print(Fore.GREEN  + "Github:" + Fore.WHITE + " https://github.com/Stem-O")
    print("─" * 43)
    time.sleep(1)

dataname = []
data = []
pofx_data = []
gathered_pofx = []
global_mean = []
squared_values = []
tovariance_values = []
global_variance = []
global_standard_deviation = []
def probability_distribution(x):
    name = input(Fore.GREEN + "Name of data" + Fore.WHITE + ": ")
    dataname.append(name)
    for i in range(int(x)):
        var = input("Data" + "[" + Fore.GREEN + str(i) + Fore.WHITE + "]: ")
        data.append(var)

def get_mean():
    print("─" * 43)
    try:
        for i in range(int(arg)):
            pofx_input = input(Fore.WHITE + "Pofx_Data[" + Fore.GREEN + str(i) + Fore.WHITE + "]: ")
            pofx_data.append(pofx_input)
        for i,j in zip(data,pofx_data):
            gathered_pofx.append(float(i) * float(j))
        mean = sum(gathered_pofx)
        global_mean.append(mean)
        print(global_mean[0])
    except ValueError:
        print("─" * 43)
        print(Fore.WHITE + "[" + Fore.RED + "-" + Fore.WHITE + "]Values cannot be empty.")
        print("─" * 43)

def get_variance():
    print(data)
    print(pofx_data)
    for i,j in zip(data,pofx_data):
        squared_values.append(math.pow(float(i) - float(global_mean[0]),2))
    for i,j in zip(squared_values,pofx_data):
        tovariance_values.append(float(i) * float(j))
    variance = sum(tovariance_values)
    global_variance.append(variance)
    standard_deviation = math.sqrt(variance)
    global_standard_deviation.append(standard_deviation)

def answers():
    table = zip(data, pofx_data, gathered_pofx, squared_values, tovariance_values)
    headers = [dataname, "P(X)", "X = P(X)", "(X - μ)2","(X-μ)2 * P(X)"]
    print(tabulate(table,headers,tablefmt="fancy_grid"))
    print(f"{Fore.GREEN}Interpretation: {Fore.WHITE}Therefore, the variance of a probability distribution is equal to {math.ceil(global_variance[0] * 100) / 100}  while the standard deviation is equal to {math.ceil(global_standard_deviation[0] * 100) / 100}.")
banner()
probability_distribution(arg)
get_mean()
get_variance()
answers()


