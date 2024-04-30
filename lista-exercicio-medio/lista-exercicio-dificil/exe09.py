def receberSenha():
    while True:
        try:
            senha = input('Informe a senha: ').strip()
            if isSenhaValid(senha.lower()):
                return list(senha)
            print('Senha inválida.')   
        except Exception:
            print('Ocorreu um erro ao processar a senha.')
        
def isSenhaValid(senha):
    if senha == '':
        return False
    caracteres_validos = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?'
    return all(caractere in caracteres_validos for caractere in senha)

def verificarForcaDaSenha(senha):
    """
    Verifica a força de uma senha com base em critérios específicos.

    Args:
        senha (str): A senha a ser verificada.

    Returns:
        str: Uma string indicando a força da senha. Pode ser 'forte', 'média' ou 'fraca'.
    """
    forca = 0
    if sum(caractere.islower() for caractere in senha) >=2 and sum(caractere.isupper() for caractere in senha) >=2:
        forca += 1
        
    if sum(caractere.isdigit() for caractere in senha) >= 2:
        forca += 1
    if sum(caractere in '!@#$%^&*()_+-=[]{}|;:,.<>?' for caractere in senha) >= 2:
        forca += 1
    if len(senha) >= 8:
        forca += 1
    if forca >=4:
        return 'forte'
    if forca == 2:
        return 'média'
    return 'fraca'

def main():
    senha = receberSenha()
    forca_senha = verificarForcaDaSenha(senha)
    senha = ''.join(senha)
    print(f'Senha: {senha}\nGrau de força: {forca_senha}')

main()
