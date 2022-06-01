import wmi

# Carregar informações do sistema
c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

# Mostrar informações do sistema
print("Nome do computador:", my_system.Name)
print("Nome do sistema:", my_system.SystemType)
print("Nome do usuário:", my_system.UserName)
print("Modelo do computador:", my_system.Model)
print("Número de processadores:", my_system.NumberOfProcessors)