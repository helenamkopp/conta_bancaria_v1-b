# conta_bancaria_v3

- Pequeno projeto Orientado a Objetos construido utilizando o PyCharm de funcionalidades de uma conta bancária. 
- Contém as mesmas funcionalidades do projeto conta_bancaria_v1, porém com mais classes, métodos e testes unitários. 

#Arquivo main.py:

*class Client: possui método construtor e é deicada exclusivamente aos dados do cliente (comparada a versão v1, na v3 fazemos uso dos modificadores de acesso);

*class Historic:possui método construtor o qual declara o momento de abertura de uma conta (usando a biblioteca datetime) e guarda as transações em uma lista, criando assim
um pequeno histórico bancário; o método print tem um laço de organização para cada transição. (for t in..)

*class Account:possui método construtor exclusiva aos dados da conta bancária, declarando seu limite fixo e herda os dados da classe cliente para o titular, 
os demais métodos são de funcionalidades de uma conta como: saque, extrato, transferencia, deposito e atualização.  

*class SavingAccount:classe adicionada nessa versão, remete a uma conta poupança e é uma classe filha/ sub classe de account. O método update foi reescrito pois a conta poupança 
possui um cálculo diferente. 

*class CheckingAccount: classe adicionada nessa versão, remete a uma conta corrente e é uma classe filha/sub classe de account. O método update foi reescrito pois a conta corrente 
possui um cálculo diferente e o método deposit é apenas dessa classe, onde a cada depósito em conta corrente o banco desconta 10 centavos do saldo da conta. 

#Arquivo test_main: realiza alguns testes unitários referentes ao arquivo main.py
