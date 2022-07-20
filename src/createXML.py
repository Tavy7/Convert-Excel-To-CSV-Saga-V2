from client import Client
from factura import Factura
import readAndParseExcel as xpa
import var

# To move function to main file
def selectClient():
    clients = var.clients
    print("Select the client.")
    for index in range(0, len(clients)):
        print(f"{index + 1}. {clients[index].Nume}")

    # TO DO Input

def main():
    selectClient()

if __name__ == "__main__":
    main()