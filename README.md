# SIBERIA

**Sistema Integrado de Boletim de Enfermagem Reconhecido por IA Adaptativa**

O nome **SIBERIA** expressa a concepção original do projeto: aplicar inteligência artificial ao reconhecimento e à estruturação de informações presentes em boletins e documentos de enfermagem, transformando registros manuais em dados computáveis, verificáveis e úteis ao trabalho operacional.

## Tese fundadora

> Reduzir o retrabalho das técnicas de enfermagem na reescrita de boletins clínicos manuais para o sistema digital, liberando tempo para cuidado direto ao paciente e minimizando erros de digitação.

Essa tese define o motivo de existência do SIBERIA. O problema não é simplesmente digitalizar papel ou inserir IA em um fluxo existente: é investigar como reduzir a duplicação de trabalho na passagem entre o registro clínico e o sistema digital, sem perder contexto, controle humano, rastreabilidade ou confiabilidade dos dados.

A partir dessa origem, a investigação evolui para uma questão técnica mais ampla: **como transformar documentos heterogêneos em dados estruturados e operacionalmente utilizáveis, tornando explícitas a incerteza da extração, a validação humana e a proveniência de cada informação?**

**Pesquisa aplicada e desenvolvimento de uma camada operacional para fluxos documentais em saúde.**

O SIBERIA é uma iniciativa de pesquisa aplicada e desenvolvimento orientada à investigação de formas de transformar documentos e informações hospitalares em dados estruturados, verificáveis e úteis aos fluxos de trabalho, preservando a revisão humana, a rastreabilidade e a proteção de dados.

O trabalho de investigação, formulação do problema e concepção da solução vem sendo desenvolvido de forma iterativa ao longo do tempo. **A abertura deste repositório marca a disponibilização da camada pública do projeto**: um espaço para documentar a direção técnica, compartilhar a evolução da aplicação e tornar verificáveis os artefatos que forem efetivamente publicados. A abertura pública não representa o início da pesquisa, nem implica que todas as hipóteses já tenham sido comprovadas ou que exista uma solução implantada em ambiente clínico.

## Contexto e problema investigado

Em fluxos hospitalares que combinam formulários em papel e sistemas digitais, a transcrição manual pode criar retrabalho e oportunidades para inconsistências. O SIBERIA investiga como apoiar esse processo por meio de captura documental, extração assistida por OCR e IA, validação explícita, revisão humana e exportação estruturada.

Esse problema constitui o ponto de partida da investigação, não uma afirmação de que todos os hospitais ou unidades operam da mesma maneira. As observações devem ser contextualizadas e complementadas por evidências verificáveis antes de sustentar conclusões gerais.

## Objetivo

Projetar, implementar e avaliar um fluxo assistido que permita transformar documentos de teste em dados estruturados, deixando explícitas a origem dos valores, as incertezas, as correções humanas e as limitações do processamento automatizado.

### Fluxo operacional em investigação

1. Receber um documento de teste ou de uso autorizado.
2. Verificar condições básicas de legibilidade e qualidade.
3. Extrair campos candidatos por técnicas de OCR e/ou IA.
4. Apresentar os campos para revisão humana, destacando ausências e incertezas.
5. Validar os valores segundo regras documentadas.
6. Exportar os dados revisados em formato estruturado.
7. Registrar os eventos técnicos necessários à rastreabilidade.

Este fluxo descreve o objetivo de desenvolvimento. Cada etapa será considerada implementada somente quando houver código, testes e instruções reproduzíveis correspondentes.

## Abordagem de pesquisa

O projeto adota uma abordagem incremental, orientada por evidências:

- **Problema e contexto:** documentar observações, fontes, limitações e perguntas em aberto.
- **Hipóteses:** explicitar o que precisa ser investigado, sem tratar suposições como fatos.
- **Experimentação:** avaliar técnicas com protocolos, conjuntos de dados e critérios definidos.
- **Revisão humana:** tratar a saída automatizada como candidata a validação, não como verdade garantida.
- **Avaliação:** publicar métricas somente com metodologia, condições de teste, resultados e limitações.
- **Evolução técnica:** registrar decisões relevantes e separar funcionalidades propostas, em desenvolvimento, testadas e validadas.

## Princípios de engenharia e responsabilidade

- **Supervisão humana:** extrações automatizadas precisam de revisão adequada antes de serem utilizadas em processos relevantes.
- **Privacidade por padrão:** priorizar dados sintéticos; qualquer dado real exige autorização e avaliação apropriada.
- **Rastreabilidade:** documentar versões, correções, regras e eventos relevantes, minimizando a coleta de dados.
- **Reprodutibilidade:** tornar os experimentos verificáveis sempre que possível.
- **Interoperabilidade responsável:** integrações dependem de requisitos, autorização, mapeamento e testes específicos; não se presume acesso a APIs hospitalares.
- **Acessibilidade operacional:** investigar interfaces claras, com poucos passos e adequadas a diferentes níveis de familiaridade digital.
- **Limites clínicos:** o protótipo não substitui profissionais, não realiza diagnóstico e não deve orientar decisões assistenciais sem validação, governança e autorizações apropriadas.

## Escopo desta superfície pública

Este repositório é a casa pública da aplicação operacional, do código publicável, da documentação técnica do produto e das demonstrações seguras. O conhecimento interno, as notas de pesquisa restritas e o planejamento detalhado permanecem no Vault privado. A publicação de um documento ou artefato deve ocorrer após revisão de privacidade, confidencialidade, segurança e sustentação das afirmações.

- [Visão da arquitetura](docs/architecture/overview.md)
- [Roadmap público](docs/roadmap.md)
- [Segurança e privacidade](SECURITY.md)

## Posicionamento e visão de plataforma

- [Posicionamento de mercado e visão de plataforma](docs/market-and-platform-vision.md)
- [Análise competitiva preliminar](docs/competitive-landscape.md)

O SIBERIA Operacional é o primeiro produto proposto. Uma plataforma hospitalar mais ampla é uma visão de longo prazo a validar, não uma capacidade atualmente disponível. O documento público registra soluções relacionadas e explicita hipóteses, sem alegar pioneirismo ou superioridade não demonstrados.

## Estado do projeto

**Fase pública:** estruturação da superfície pública e evolução incremental da aplicação.  
**Histórico de pesquisa:** investigação e concepção vêm sendo desenvolvidas iterativamente antes desta abertura pública; detalhes específicos devem ser sustentados por registros e artefatos datados quando forem apresentados.  
**Implementação:** não se deve inferir que o fluxo descrito esteja integralmente implementado apenas pela presença desta documentação.  
**Validação:** não são declaradas validação clínica, implantação hospitalar, conformidade certificada ou integração com sistemas de produção sem evidências específicas.

## Limitações e segurança

Não publique aqui dados pessoais ou de saúde identificáveis, imagens identificáveis de prontuários, assinaturas, credenciais, tokens, segredos ou documentos internos confidenciais. Repositórios privados também exigem controles de acesso e minimização de dados. Para demonstrações públicas, utilize dados sintéticos ou materiais cuja divulgação esteja autorizada.

O SIBERIA está em desenvolvimento e não se destina, neste estágio, ao uso clínico em produção.
