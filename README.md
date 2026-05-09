# Industrial Telemetry Pipeline

Projeto de engenharia de dados e analytics desenvolvido para simular um pipeline de telemetria industrial utilizando AWS e Python.

---

## Objetivo

Simular coleta, armazenamento e análise de dados operacionais de equipamentos industriais, aplicando conceitos de:

- Engenharia de Dados
- Data Lake
- Analytics Operacional
- Telemetria Industrial
- AWS Cloud

---

## Arquitetura

Python → Amazon S3 → Amazon Athena

---

## Tecnologias Utilizadas

- Python
- Pandas
- AWS S3
- Amazon Athena
- SQL
- Git/GitHub

---

## Funcionalidades

- Geração de dados simulados de telemetria
- Armazenamento em Data Lake
- Consultas analíticas com Athena
- Identificação de registros críticos
- Simulação de monitoramento operacional

---

## Estrutura do Dataset

| Coluna | Descrição |
|---|---|
| equipment_id | Identificador do equipamento |
| setor | Área operacional |
| temperatura | Temperatura operacional |
| vibracao | Nível de vibração |
| pressao | Pressão operacional |
| status | Status do equipamento |

---

## Exemplos de Análises

### Média de Temperatura

```sql
SELECT AVG(temperatura)
FROM telemetry;
```

### Equipamentos Críticos

```sql
SELECT *
FROM telemetry
WHERE temperatura > 100
OR vibracao > 4;
```

---

## Estrutura do Projeto

```text
industrial-telemetry-pipeline/
│
├── dashboards/
├── data/
├── queries/
├── scripts/
└── README.md
```

---

## Evidências do Projeto

### Consulta no Amazon Athena

![Athena Query](dashboards/01-athena-query-results.png)

### Exemplos de cálculos

![Calculo AVG](dashboards/02-avg-temperatura.png")

### Análise de Equipamentos Críticos

![Critical Analysis](dashboards/03-critical-equipment-analysis.png)

---

## Próximos Passos

- Integração com AWS Glue
- Dashboard no QuickSight
- Machine Learning para previsão de falhas
- Alertas automatizados

## Autor

Symon Costta