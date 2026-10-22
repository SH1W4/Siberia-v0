# Mercado e alternativas — análise competitiva preliminar

**Estado:** síntese de fontes públicas; não é benchmark independente nem prova de superioridade do SIBERIA.

## Soluções relacionadas

| Referência | Caso publicado | Implicação para o SIBERIA |
|---|---|---|
| [Dasa + Google Cloud](https://cloud.google.com/customers/dasa?hl=pt-BR) | OCR de pedidos médicos digitados/manuscritos para agendamento no Nav | Leitura de manuscrito clínico já existe no Brasil; o SIBERIA precisa provar valor no fluxo de boletins de enfermagem |
| [Upstage Healthcare](https://www.upstage.ai/solutions/healthcare) | Extração de registros clínicos manuscritos, tabelas e documentos, com paper-to-EHR descrito pelo fornecedor | OCR genérico e integração não bastam como diferencial |
| [Saúde iD + Google Cloud](https://cloud.google.com/customers/saude-id) | OCR de guias e pedidos de saúde | Existem casos adjacentes de automação documental |
| [NHS England — ambient scribing](https://www.england.nhs.uk/publication/guidance-on-the-use-of-ai-enabled-ambient-scribing-products/) | Orientação para adoção de documentação clínica assistida por voz | IA clínica exige avaliação, governança e supervisão |

Os casos Dasa/Saúde iD são relatos de fornecedores sobre clientes; os números não são comparações independentes nem podem ser transferidos para o SIBERIA. A orientação NHS aplica-se à Inglaterra e à documentação por voz, não diretamente à regulamentação brasileira nem ao OCR de papel.

## Hipótese de diferenciação
O SIBERIA investiga o fluxo **boletim manuscrito de enfermagem → extração por campo → revisão humana → versão auditável → exportação autorizada**.

Possíveis diferenciais a validar:
- especialização no formulário/vocabulário alvo;
- tratamento explícito de campo ausente, ilegível ou incerto;
- proveniência por campo e preservação do original;
- correções, aprovações e versões rastreáveis;
- avaliação por campo, erros críticos e tempo total;
- compatibilidade com governança e infraestrutura aprovadas pelo hospital.

São objetivos de projeto, não capacidades implementadas sem código, testes e avaliação.

## Estratégia
Não competir inicialmente como OCR genérico ou substituto de prontuário. Validar um formulário, uma unidade e um fluxo. Se um fornecedor existente resolver OCR com menor custo e risco, considerar integrar essa capacidade. O valor pode estar no workflow, revisão, rastreabilidade e adequação local.

## Perguntas de diligência
Verificar suporte a português brasileiro e cursiva; corpus avaliado; confiança e proveniência por campo; tratamento de ausências; revisão humana; localização/retenção dos dados; uso para treinamento; implantação cloud/on-prem; integração autorizada; custo total; métricas reproduzíveis.

## Fontes
- Google Cloud — Dasa: https://cloud.google.com/customers/dasa?hl=pt-BR
- Upstage Healthcare: https://www.upstage.ai/solutions/healthcare
- Google Cloud — Saúde iD: https://cloud.google.com/customers/saude-id
- NHS England, orientação publicada em 27/04/2025 e atualizada em 29/07/2026: https://www.england.nhs.uk/publication/guidance-on-the-use-of-ai-enabled-ambient-scribing-products/
