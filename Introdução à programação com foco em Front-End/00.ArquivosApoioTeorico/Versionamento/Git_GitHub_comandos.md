# GIT COMANDOS SINTAXES

No site do Git encontramos as referências completas de todos os comandos.  
[Git Docs - Acesse](https://git-scm.com/docs)  
Aqui iremos expor os mais comuns e usados.  

*(Para melhor leitura deste arquivo, utilize um leitor de markdown)*

_______________

## Git estágios 
| Working Directory | Stage Area      | Local Repository | Remote Repository |
|   -----           |  -----          |  -----           |              -----| 
| *Local*           |    *Local*      |          *Local* |          *Remote* |
|                   |                 |         x        | *<-- Git Pull*    |
|  Git Add -->      |           x     |                  |                   |
|                   |  Git Commit --> |       x          |                   |
|    x <------------|-----------------|---- Git Checkout |                   |
|    x <------------|-----------------|---- Git Merge    |                   |
|                   |                 |     Git Push --> |        x          |

    

## Atalhos 

### Versão
- git -v

### Configuração 
- git config --global user.name Fulano de Tal
- git config --global user.email fulanodetal@exemplo.br  

  - git config --list  
  *Testando as configurações. conforme exemplo do usuário acima, saída será igual abaixo:*  
      user.name = Fulano de Tal  
      user.email = fulanodetal@exemplo.br  
      color.status = auto  
      color.branch = auto  
      color.interactive = auto  
      color.diff = auto

### Clonando repositório
- git clone  link-do-repositorio
*Cria um repositório local a partir de um repositório remoto*

### Status
- git status  
*Informa o status do git*

### Commit
- git add . 
- git add -A  
*Adiciona todas as mudanças ao próximo commit.*
- git commit -m "Mensagem do commit": Realiza um commit com a mensagem fornecida. 

### Atualizar repositório remoto
- git push  
*Envia os commits do nosso repositório local ao repositório remoto*
- git remote add upstream link-do-github  


### Atualizar repositório local
|Comando                  | Opções / Argumentosunção                                                                              |
|----                     |                       -----------------------------                                 |
| git remote show origin  | *Verifica se nosso repositório local está atualizado com o repositório remoto*      |
| git pull                | *Atualiza nosso repositório local com as últimas informações no repositório remoto* |


#### Como atualizar um repositório forcado (forked) com o rebase:
| Comando                    | Opções / Argumentos             | Função                                       |
| -----                      |                   ------------  |                         -----------          |
| git remote add upstream    | link-do-github                  | *Adiciona o repositório remoto (repositório original que foi forcado)* |
| git fetch upstream         |                                 | *Busca (fetch) todas as ramificações do fluxo ascentende (upstream) remoto* |
| git rebase upstream        | /master                         | *Reescreve suas master com o fluxo ascendente (upstream) da master git rebase* |
| git push --set-upstream    | origin nome-da-branch           |  *Empurra as atualizações para a **para branch***|
| git push origin            | master --force                  | *Empurra as atualizações **para a master** de forma forçada* |

### Log
- git log  
*Exibe o histórico de commits*

- git log --oneline  
*Exibe o histórico de commits em uma linha por commit*

### Comandos de navegação
| Comando             | Significado               |                                                             Usado para |
| -----               |               ------------|                                                             -----------|
| pwd                 | *Print Working Directory* | Imprime a rota ou caminho da pasta atual                               |
| cd                  | *Change Directory*        | Acessa uma pasta / desce um nível (volta à pasta de início por padrão) | 
| cd ..               |                           | Volta uma pasta / sobe um nível                                        |
| ls                  |       *List files*        | Mostra todas as pastas e arquivos da pasta atual                       |
| mrdir "NOME"        |   *Make Directory*        | Cria uma pasta                                                         | 
| rmdir "NOME"        | *Remove Directory*        | Remove, deleta, uma pasta                                              |
| code .              |                           | Abre a pasta atual no VSCode                                           | 


### Comandos de Branches
| Comando         | Opções / Argumentos | Função                                                         |
|-----            | -----               | -----                                                          |
| git branch      |                     | Exibe a lista de branches disponíveis e destaca a branch atual |
| git branch      | nome-branch         | Cria uma nova branch                                           | 
| git checkout    | nome-branch         | Troca o HEAD, ou ponteiro, para a branch indicada              |
| git checkout    | -b nome-branch      | Cria e muda para uma nova branch em um único comando           |
| git branch      | -d nome-branch      | Excluir um branch no local                                     |
| git push origin | --delete nome-branch| Excluir um branch remoto                                       


### Comandos para Merge
| Comando   | Opções / Argumentos  | Função                                                                |
| --------  | ------               | ------                                                                |
| git merge | nome-da-branch       | Trazer os elementos da branch indicada no comando para a branch atual | 
| git merge | --abort              | Aborta o processo de merge em casos em que o Git identifica um conflito, retornando o projeto ao seu estado anterior à tentativa de merge |


#### Análise de merge
- **Accept current change (”Aceitar mudança atual”):**  
Ao clicar nesta opção mantemos a linha escrita na branch atual, neste caso a main. Ou seja, ficariamos com a frase “Linha escrita na main”
- **Accept incoming change (”Aceitar mudança recebida”):**  
Ao clicar nesta opção escolhemos “aceitar” a linha vindo da branch com as “novas informações”, neste caso a outra-branch. Ou seja, ficariamos com a frase “Linha escrita na outra branch"
- **Accept both changes (”Aceitar ambas as mudanças”):**  
Ao clicar nesta opção escolhemos manter no arquivo tanto a linha escrita na main quanto a linha vindo da outra branch. Ou seja, teriamos a “Linha escrita na main” na linha dois, e o VSCode adicionaria uma linha três com a frase “Linha escrita na outra branch”
- **Compare changes (”Comparar mudanças”):**  
 Ao clicar neste link abrimos um novo “arquivo temporário”, onde podemos ver do lado esquerdo a linha da branch atual destacada em vermelho e, à direita, a linha da branch com as “novas informações” destacada em verde. Este arquivo não resolve o conflito de forma alguma. Sua única função é facilitar a visualização do(s) conflito(s), mas não aceita nenhum tipo de edição. Após verificar os conflitos, sem risco algum de alteração, podemos fechar este "arquivo temporário" clicando no ‘X’ ao lado do nome do arquivo.

----------

*O conteúdo abaixo é uma sistematização resumida do **tutorial público** da WoMakersCode Publicado no DEV.to*  
 [Acesse aqui o conteúdo na íntegra](https://dev.to/womakerscode/git-e-github-guia-rapido-e-comandos-basicos-para-iniciantes-4ile)

## Criando repositório local:
Na pasta/diretório que você deseja versionar, digite: 
- git init

## Ver estado do Git:
- git status

Use esse comando sem moderação.

## Adicionando seus arquivos ao Git: 
- git add nome_do_arquivo

ou para adicionar todos os arquivos de uma só vez:

- git add .

## Atualizando commit de arquivo modificado:
- git commit -am 'digite sua mensagem aqui'

## Ligando seu repositório local a sua nuvem:
- git remote add origin ink_para_o_repositório_do_seu_projeto

## Enviando suas alterações pela primeira vez:
- git push -u origin master

Nas próximas vezes basta:

- git push

## Copiando um repostório:
- git clone link_para_o_repositório_que_deseja_copiar

## Criando branches:
- git checkout -b nome_do_branch 

## Para voltar ao branch master:
- git checkout master
 
## Fazer a troca entre os branches:
- git checkout nome_do_branch

Seus branches locais não estarão na nuvem a menos que você os envie.

## Enviar para nuvem (servidor remoto):
- git push origin nome_do_branch

## Unindo branches
- git merge nome_do_branch

## Atualizando seu repositório local:

Pega as modificações que foram feitas no repositório remoto.
- git pull

## Desfazendo commits:
- git revert chave_do_commit

## Encontrar chave do commit: 
- git log
  
_____________________
  ***Final** do conteúdo do tutorial público da WoMakersCode Publicado no DEV.to* 
______________________


# Referências
- [Git e Github](https://www.youtube.com/watch?v=kB5e-gTAl_s&t=1s)

- [JUSTEN, Willian. 06. Configurando o Git - Git e Github para Iniciantes](https://www.youtube.com/watch?v=QF0Cdd8ApRk&ab_channel=WillianJusten) Acesso em 18 de out. de 2022

- LinnuxConfig.Org - Linux commands cheat sheet. Disponível em: https://linuxconfig.org/linux-commands-cheat-sheet. Acesso em 18 de out. de 2022

- Atlassian Bitbucket. What is version control?. Disponível em: https://www.atlassian.com/git/tutorials/what-is-version-control. Acesso em 19 de out. de 2022

- Receitas de Código. Git - O que é uma branch. Disponível em: https://receitasdecodigo.com.br/devops/git-o-que-e-um-branch. Acesso em 20 de out. de 2022

- Documentação oficial do Git. Disponível em: https://git-scm.com/docs/git. Acesso em 20 de out. de 2022

- Tutoriais WoMakersCode. Disponível em: https://dev.to/womakerscode. Acesso em: 14 de jan. de 2024.
  https://dev.to/womakerscode/tutorial-git-fork-como-colaborar-com-projetos-de-codigo-aberto-1lkm

  https://dev.to/womakerscode/tutorial-git-copiando-um-repositorio-existente-git-clone-1bfe

  https://dev.to/womakerscode/tutorial-git-verificando-commits-remotos-56f3