# Client_Program
This is a Python script for managing a list of clients, stored in a text file. The script provides a menu with different options to add, edit, delete, list and search for clients.

The script opens a file called "clientes.txt" in write mode with the option to read as well (w+). It then defines several functions to handle different operations on the list of clients.

The salvar_clientes function takes a file and a dictionary with client data, converts it to JSON format and writes it to the file.

The abrir_clientes function reads the file and loads each line (which is in JSON format) into a list of dictionaries, which is passed as an argument.

The adicionar_cliente function prompts the user for the client's name, email, and phone number, and creates a new dictionary with this information, as well as a unique client number, which is calculated based on the number of clients already in the list. It then calls salvar_clientes to save the new client to the file.

The editar_cliente function prompts the user for the name of the client they want to edit, as well as the new email and phone number. It then iterates through the list of clients, and if it finds a client with the same name, it updates the email and phone number, and saves the modified client to the file using salvar_clientes.

The excluir_cliente function prompts the user for the name of the client they want to delete. It then iterates through the list of clients, and if it finds a client with the same name, it removes that client from the list and saves the modified list to the file using salvar_clientes.

The lista_cliente function simply prints out all the clients in the list, along with their information.

The buscar_cliente function prompts the user for the name of the client they want to search for. It then iterates through the list of clients, and if it finds a client with the same name, it prints out that client's information.

Finally, the script enters a loop that displays a menu of options and prompts the user to choose one. It then calls the appropriate function based on the user's choice. If the user chooses to exit, the loop is broken and the file is closed.

Note that this script assumes that the file "clientes.txt" already exists and is formatted correctly (one JSON object per line). If the file does not exist or is empty, the script will still work, but the client numbers will start from 1.
