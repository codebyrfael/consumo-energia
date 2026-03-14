# ⚡ Calculadora Inteligente de Consumo de Energia

![Python](https://img.shields.io/badge/Python-3.x-blue)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black)
![Energy](https://img.shields.io/badge/Energy-Calculator-green)

Projeto desenvolvido em Python para estimar o consumo mensal de energia elétrica de aparelhos domésticos.

---

## 📌 Objetivo

Este projeto tem como objetivo ajudar usuários a calcular o consumo mensal de energia elétrica de um aparelho utilizando informações simples de uso.

O programa solicita ao usuário:

- Nome do aparelho
- Potência do aparelho em watts (W)
- Tempo médio de uso diário em horas

Com essas informações, o sistema calcula automaticamente o consumo mensal em kWh.

---

## 🧮 Fórmula utilizada

consumoMensal = (potencia * horasDia * 30) / 1000

Onde:

- **potencia** → potência do aparelho em watts  
- **horasDia** → tempo médio de uso diário  
- **30** → média de dias no mês  
- **1000** → conversão de Wh para kWh  

---

## 💰 Cálculo de custo estimado

O programa também calcula um custo aproximado de energia utilizando um valor médio de:

R$ 0,75 por kWh

---

## 🚀 Como executar o programa

1. Baixe ou clone este repositório
2. Execute o arquivo `app.py`
3. Informe os dados solicitados pelo programa

---

## 💡 Exemplo de uso

Digite o nome do aparelho: Geladeira  
Digite a potência do aparelho (W): 300  
Digite o tempo médio de uso diário (horas): 5  

Resultado:

Aparelho: Geladeira  
Consumo estimado: 45 kWh/mês  
Custo estimado: R$ 33.75  

---

## 🛠 Tecnologias utilizadas

- Python
- GitHub

---

## 📚 Projeto educacional

Projeto desenvolvido como parte de um exercício de iniciação em tecnologia e programação, com o objetivo de praticar lógica de programação e organização de projetos em repositórios. by Rafael Camargo Gomes

