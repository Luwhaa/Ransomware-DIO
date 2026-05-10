# Simulador de Ransomware em Python

## Sobre o Projeto

Este projeto foi desenvolvido com fins educacionais para demonstrar, em ambiente controlado, o funcionamento básico de um ransomware utilizando Python.

O programa simula:
- criptografia de arquivos;
- geração de chave criptográfica;
- criação de mensagem de resgate;
- recuperação dos arquivos através da descriptografia.

> ⚠️ Projeto criado apenas para estudos em ambiente controlado.

---

# Tecnologias Utilizadas

- Python 3
- Biblioteca `cryptography`
- Módulo `os`

---

# Estrutura do Projeto

```bash
.
├── app.py
├── descrip.py
├── chave.key
├── LEIA ISSO.txt
└── test_files/
    ├── dados_confidenciais.txt
    └── senhas.txt
```

---

# Funcionamento

## app.py
Responsável por:
- gerar a chave;
- localizar arquivos;
- criptografar os arquivos;
- criar a mensagem de resgate.

---

## descrip.py
Responsável por:
- carregar a chave;
- localizar arquivos criptografados;
- restaurar os arquivos originais.

---

# Como Executar

## Instalar dependência

```bash
pip install cryptography
```

---

## Executar criptografia

```bash
python app.py
```

---

## Executar descriptografia

```bash
python descrip.py
```

---

# Conceitos Aprendidos

Durante o desenvolvimento deste projeto foi possível aprender:

- manipulação de arquivos;
- criptografia e descriptografia;
- automação com Python;
- funcionamento básico de ransomware;
- práticas de segurança digital.

---

# Medidas de Proteção Contra Ransomware

- manter backups atualizados;
- utilizar antivírus;
- manter o sistema atualizado;
- evitar downloads suspeitos;
- cuidado com e-mails maliciosos.

---

# Aviso Legal

Este projeto possui finalidade exclusivamente educacional e não deve ser utilizado em ambientes reais ou sem autorização.

---

# Autor: Luana AF

Projeto desenvolvido para estudos de:
- Python;
- Segurança da Informação;
- Criptografia.
