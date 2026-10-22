# SIBERIA

**Superfície pública do produto e aplicação operacional do SIBERIA.**

SIBERIA é um projeto de pesquisa aplicada e desenvolvimento voltado à melhoria de fluxos documentais e à estruturação de dados em contextos hospitalares. Esta repository é a casa pública da aplicação, da sua documentação técnica voltada ao produto e das demonstrações que possam ser compartilhadas com segurança.

> **Estado atual:** repositório em fase de estruturação. A presença desta documentação não significa que as funcionalidades descritas já estejam implementadas, validadas clinicamente ou integradas a sistemas hospitalares.

## Objetivo do produto

Investigar e prototipar um fluxo assistido para transformar documentos em dados estruturados, mantendo revisão humana, rastreabilidade e tratamento explícito de incertezas.

Fluxo-alvo do protótipo:

1. Receber um documento de teste.
2. Extrair campos candidatos com técnicas de OCR/IA.
3. Apresentar os resultados para revisão humana.
4. Validar os campos e sinalizar ausências ou incertezas.
5. Exportar dados estruturados de forma controlada.
6. Registrar eventos técnicos relevantes para auditoria.

## Princípios

- **Human-in-the-loop:** extrações automatizadas são sugestões até serem revisadas.
- **Privacidade por padrão:** utilizar dados sintéticos ou autorizados e devidamente protegidos.
- **Rastreabilidade:** documentar correções, versões e decisões técnicas relevantes.
- **Validação mensurável:** publicar métricas somente quando forem obtidas por experimentos reproduzíveis.
- **Interoperabilidade responsável:** integrações com sistemas hospitalares dependem de documentação, autorização, mapeamento e testes específicos.
- **Segurança clínica:** o protótipo não substitui profissionais, não realiza diagnóstico e não deve ser usado para decisões assistenciais sem validação e governança apropriadas.

## Estrutura de documentação

- [Visão da arquitetura](docs/architecture/overview.md)
- [Roadmap público](docs/roadmap.md)
- [Segurança e privacidade](SECURITY.md)

## Limites da versão pública

Este repositório não deve conter dados pessoais ou clínicos identificáveis, credenciais, tokens, segredos, documentos internos confidenciais ou detalhes operacionais que possam comprometer pessoas ou instituições. Evidências internas, notas de pesquisa sensíveis e materiais de trabalho permanecem no Vault privado; apenas informações revisadas e apropriadas para divulgação são publicadas aqui.

## Desenvolvimento

As instruções de instalação e execução serão adicionadas quando a aplicação e sua stack estiverem confirmadas neste repositório. Não presuma que exista uma versão executável até que esses passos sejam documentados e testados.

## Status

**Fase:** estruturação da superfície pública e definição do produto.  
**Uso:** pesquisa e demonstração controlada; não destinado a uso clínico em produção.
