from filesystem import FileSystem

def interface():
    fs = FileSystem()
    current_path = "/root"
    user = "admin"

    def normalize_path(path):
        if path.startswith("/"):
            return path
        if current_path.endswith("/"):
            return current_path + path
        return current_path + "/" + path

    print("Simulador de Sistema de Arquivos - Digite 'help' para ajuda.")

    while True:
        cmd = input(f"{user}@simulador:{current_path}$ ").strip()
        if not cmd:
            continue

        parts = cmd.split()
        comando = parts[0].lower()
        args = parts[1:]

        if comando == "exit":
            print("Saindo do simulador...")
            break

        elif comando == "help":
            print("""Comandos disponíveis:
mkdir <nome_dir>         - Cria um diretório no caminho atual
cd <caminho>            - Navega para outro diretório
ls                      - Lista arquivos e pastas no diretório atual
create <nome_arquivo>    - Cria um arquivo vazio no diretório atual
read <nome_arquivo>      - Mostra o conteúdo do arquivo
write <nome_arquivo>     - Escreve conteúdo no arquivo
delete <nome_arquivo>    - Deleta o arquivo
chmod <arquivo> <usuario> <perm> - Ajusta permissões no arquivo
help                    - Mostra esta ajuda
exit                    - Sai do simulador
            """)

        elif comando == "mkdir":
            if len(args) != 1:
                print("Uso: mkdir <nome_dir>")
                continue
            dir_path = normalize_path(args[0])
            fs.create_directory(dir_path)

        elif comando == "cd":
            if len(args) != 1:
                print("Uso: cd <caminho>")
                continue
            target_path = normalize_path(args[0])
            if fs.directory_exists(target_path):
                current_path = target_path
            else:
                print(f"Diretório '{args[0]}' não encontrado.")

        elif comando == "ls":
            fs.list_directory(current_path)

        elif comando == "create":
            if len(args) != 1:
                print("Uso: create <nome_arquivo>")
                continue
            file_path = normalize_path(args[0])
            fs.create_file(file_path, content="", user=user)

        elif comando == "read":
            if len(args) != 1:
                print("Uso: read <nome_arquivo>")
                continue
            file_path = normalize_path(args[0])
            fs.read_file(file_path, user=user)

        elif comando == "write":
            if len(args) != 1:
                print("Uso: write <nome_arquivo>")
                continue
            file_path = normalize_path(args[0])
            new_content = input("Novo conteúdo: ")
            fs.write_file(file_path, new_content, user=user)

        elif comando == "delete":
            if len(args) != 1:
                print("Uso: delete <nome_arquivo>")
                continue
            file_path = normalize_path(args[0])
            fs.delete_file(file_path, user=user)

        elif comando == "chmod":
            if len(args) != 3:
                print("Uso: chmod <arquivo> <usuario> <perm>")
                continue
            file_path = normalize_path(args[0])
            fs.set_file_permission(file_path, args[1], args[2], admin=user)

        else:
            print(f"Comando desconhecido: {comando}. Digite 'help' para ajuda.")

if __name__ == "__main__":
    interface()
