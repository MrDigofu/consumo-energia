# ⚡ Calculadora de Consumo Elétrico

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Projeto-black?logo=github)
![Energia](https://img.shields.io/badge/Energia-Consumo%20El%C3%A9trico-yellow)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)

## 📌 Sobre o projeto

A **Calculadora de Consumo Elétrico** é um programa desenvolvido em Python que permite estimar o consumo mensal de energia elétrica de um aparelho.

O usuário informa o nome do aparelho, sua potência em watts e o tempo médio de utilização diária. Com essas informações, o sistema calcula o consumo estimado em **kWh por mês**.

O programa também apresenta uma estimativa do custo mensal utilizando um valor fixo de **R$ 0,75 por kWh**.

## 🎯 Objetivo

O objetivo do projeto é praticar conceitos básicos de programação em Python e, ao mesmo tempo, criar uma ferramenta simples para ajudar na compreensão do consumo de energia elétrica.

## 🛠️ Tecnologias utilizadas

* 🐍 **Python**
* 💻 **Visual Studio Code** ou outro editor de código
* 🐙 **Git e GitHub**
* ⚡ Conceitos de consumo de energia elétrica

## 🧮 Fórmula utilizada

O consumo mensal é calculado utilizando a seguinte fórmula:

```text
Consumo mensal = (Potência × Horas por dia × 30) / 1000
```

Onde:

* **Potência** = potência do aparelho em watts (W)
* **Horas por dia** = tempo médio de utilização diária
* **30** = quantidade aproximada de dias no mês
* **1000** = conversão de Wh para kWh

### 💰 Cálculo do custo

O custo estimado é calculado utilizando:

```text
Custo mensal = Consumo mensal × Valor do kWh
```

Neste projeto, foi utilizado o valor de referência de **R$ 0,75 por kWh**.

> ℹ️ O valor utilizado é apenas uma referência para o exercício e não representa necessariamente a tarifa de energia da residência do usuário.

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Acesse a pasta do projeto

```bash
cd consumo-energia
```

### 3. Execute o programa

```bash
python app.py
```

Em alguns sistemas, pode ser necessário utilizar:

```bash
python3 app.py
```

## 🖥️ Exemplo de utilização

```text
⚡ CALCULADORA DE CONSUMO ELÉTRICO ⚡
----------------------------------------
Digite o nome do aparelho: Geladeira
Digite a potência do aparelho em watts (W): 100
Digite o tempo médio de uso diário (horas): 15

📊 RESULTADO
----------------------------------------
Aparelho: Geladeira
Consumo estimado: 45.00 kWh/mês
Custo estimado: R$ 33.75/mês
----------------------------------------
```

## 📁 Estrutura do projeto

```text
consumo-energia/
│
├── app.py
└── README.md
```

## 📚 Conceitos praticados

* Variáveis
* Entrada de dados com `input()`
* Conversão de tipos com `float()`
* Operações matemáticas
* Fórmulas
* Saída de dados com `print()`
* Formatação de valores
* Organização de projetos
* Git e GitHub


## 👨‍💻 Autor

Projeto desenvolvido como parte de um programa de iniciação em tecnologia.

