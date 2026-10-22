# Visão inicial da arquitetura

## Finalidade

Definir os limites e as responsabilidades do protótipo público antes de consolidar decisões de implementação.

## Fluxo lógico proposto

`Documento de entrada → pré-processamento → OCR/extração → normalização → revisão humana → validação → exportação → trilha de auditoria`

Este é um fluxo-alvo, não uma declaração de que todos os componentes já estão implementados.

## Componentes conceituais

### 1. Captura e entrada
Recebe imagens ou documentos de teste e verifica formato, legibilidade e condições básicas de processamento.

### 2. Extração assistida
Produz candidatos a campos estruturados. Quando disponível, cada campo deve manter referência à origem e uma indicação de incerteza apropriada ao método utilizado.

### 3. Revisão humana
Permite que uma pessoa autorizada confirme, corrija ou rejeite os valores extraídos antes da exportação.

### 4. Validação
Aplica regras explícitas de formato, obrigatoriedade e consistência. Regras clínicas não devem ser introduzidas sem validação profissional e governança adequadas.

### 5. Exportação
Gera formatos documentados, como JSON ou CSV, conforme o esquema aprovado. Integrações com EHR/ERP ou padrões como HL7 FHIR são possibilidades futuras, condicionadas à análise de requisitos e autorização do sistema receptor.

### 6. Auditoria técnica
Registra eventos mínimos necessários para rastrear o processamento e as correções, com controle de acesso e proteção contra exposição desnecessária de dados.

## Restrições de segurança

- Usar dados sintéticos no desenvolvimento público sempre que possível.
- Não armazenar segredos no código ou no histórico Git.
- Não publicar informações identificáveis de pacientes ou funcionários.
- Não enviar dados clínicos a provedores externos sem avaliação de privacidade, segurança, base legal e autorização.
- Não conectar o protótipo a sistemas assistenciais de produção sem avaliação formal, testes e autorização institucional.

## Decisões ainda abertas

- Stack da interface e do backend.
- Modelo de execução local/offline e sincronização.
- Estratégia de OCR e tratamento de escrita manual.
- Esquemas de dados e versionamento.
- Autenticação, autorização, retenção e política de logs.
- Formatos de exportação e requisitos de interoperabilidade.

As decisões devem ser registradas em documentos específicos quando houver evidência suficiente para justificá-las.
