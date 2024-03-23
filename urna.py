def inicio():
     opcao = str(input(
        '''
        Escolha uma opção:

        [V] Votar
        [B] Buscar Voto
        [Q] Quantidade de votos
        [N] Registrar Novo Candidato
        [L] Listar Candidatos

        [R] Resultado

        '''))
     return opcao


def main():
     votos = {}
     quantidade = 0
     candidatos = []

     while True:
    
        opcao = inicio().upper()

        if opcao == "V":
             quantidade, votos = votar(quantidade, votos, candidatos)
             print("-"*80)

        elif opcao == "B":
             buscar_voto(votos)
             print("-"*80)

        elif opcao == "Q":
             buscar_quantidade(quantidade)
             print("-"*80)

        elif opcao == "N":
             candidatos = registrar_candidato(candidatos)
             print("-"*80)

        elif opcao == "R":
             calculo_resultado(candidatos, votos)
             print("-"*80)

        elif opcao == "L":
             listar_candidatos(candidatos)
             print("-"*80)
                        
        else:
             print("Opção inválida!")
             print("-"*80)


def votar(quantidade, votos, candidatos):
        nome = input("\nNome: ").title()
        voto = input("\nSeu voto será em: ").title()
        if voto in candidatos:
               print("\nVoto computado!")
               votos[f"{nome}"] = f"{voto}"
               quantidade = quantidade + 1
        else:
               print("\nCandidato não encontrado!")
               
        return quantidade, votos
    

def buscar_voto(votos):
    chave = input("\nBuscar voto de: ").title()
    if chave in votos.keys():
        print(f"\n{chave} votou em",votos[f"{chave}"])

    else:
        print(f"\n{chave} não votou.")

    return None


def buscar_quantidade(quantidade): 
     print(f"\nForam computados {quantidade} votos até o momento.")


def registrar_candidato(candidatos):
     candidato = input("Nome do candidato: ").title()
     if candidato in candidatos:
          print(f"\n{candidato} já está registrado como candidato.")

     else:
          candidatos.append(candidato)
          print("\nCandidato registrado com sucesso!")
     
     return candidatos

def calculo_resultado(candidatos, votos):
     if not candidatos:
          print("Não há votos computados!")

     else:
          print(" Resulatado ".center(50, "="))     
          for candidato in candidatos:
               contagem = 0
               for chave, valor in votos.items():
                    if valor == f"{candidato}":
                         contagem += 1

               print(f"\n{candidato} recebeu {contagem} votos válidos.")

     return None


def listar_candidatos(candidatos):
     if not candidatos:
          print("\nNão há candidatos registrados!")

     else:
          print(" Candidatos ".center(50, "="))
          for candidato in candidatos:
               print(candidato)
     

main()
