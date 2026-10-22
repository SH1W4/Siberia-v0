# SIBERIA

**Sistema Integrado de Boletim de Enfermagem Reconhecido por IA Adaptativa**

O SIBERIA investiga como reduzir o retrabalho de transcrever boletins manuscritos de enfermagem para sistemas digitais. A proposta é transformar documentos autorizados em dados estruturados, preservando a origem dos campos, a incerteza da extração, a revisão humana e a rastreabilidade.

> **Objetivo inicial:** avaliar se a extração assistida pode reduzir o esforço de redigitação em um fluxo delimitado, sem comprometer a exatidão ou a proteção dos dados.

## Problema investigado

Em processos que combinam formulários em papel e sistemas digitais, a transcrição manual pode gerar trabalho duplicado e oportunidades para inconsistências. A frequência e o impacto precisam ser verificados em cada contexto; não presumimos que todos os hospitais operem da mesma forma.

## Fluxo-alvo

**Documento autorizado → verificação de qualidade → extração de campos candidatos → revisão humana → validação → exportação aprovada → auditoria**

1. Receber documento de teste ou material cujo uso tenha sido autorizado.
2. Verificar formato, integridade e legibilidade.
3. Extrair campos candidatos por OCR e/ou IA, sem tratar a saída como verdade garantida.
4. Permitir que uma pessoa autorizada confirme, corrija, rejeite ou marque campos como ausentes ou ilegíveis.
5. Aplicar regras documentadas e versionadas.
6. Exportar somente registros aprovados.
7. Preservar o histórico necessário à rastreabilidade, minimizando dados nos logs.

Este é o fluxo-alvo, não uma declaração de que todas as etapas já estejam implementadas. Cada capacidade será considerada implementada quando houver código, testes e instruções reproduzíveis.

## Princípios

- **Revisão humana:** automação não aprova registros clínicos por conta própria.
- **Sem preenchimento inventado:** valores ausentes, ilegíveis ou incertos permanecem sinalizados.
- **Proveniência:** manter a relação entre o campo extraído e sua origem quando tecnicamente disponível.
- **Versionamento:** distinguir extrações, correções humanas e registros aprovados.
- **Privacidade por padrão:** utilizar dados sintéticos no desenvolvimento público.
- **Segurança por projeto:** autenticação, autorização, minimização e isolamento institucional antes de qualquer uso com dados reais.
- **Interoperabilidade responsável:** integrações dependem de requisitos, autorização e testes.
- **Evidência antes de alegações:** publicar métricas somente com método, condições de teste e limitações explícitas.

## Escopo e limites

O foco inicial é um fluxo de boletim de enfermagem, com entrada por foto ou PDF como objetivo de desenvolvimento. A qualidade do OCR manuscrito em português, a usabilidade e a redução de tempo precisam ser avaliadas; não são resultados presumidos.

O SIBERIA **não é declarado pronto para produção clínica**. Este repositório não afirma implantação hospitalar, validação clínica, certificação regulatória ou integração com AGHUse ou qualquer outro prontuário. O protótipo não substitui profissionais e não deve orientar decisões assistenciais sem governança, validação e autorizações aplicáveis.

## Estado do projeto

O repositório está na fase de estruturação da documentação e evolução incremental da aplicação. A arquitetura e o roadmap registram propostas e trabalho pendente; sua presença não significa que as capacidades estejam implementadas.

| Área | Estado declarado |
|---|---|
| Problema e escopo inicial | Documentados como hipótese de produto |
| Arquitetura e fluxo-alvo | Propostos |
| Aplicação funcional ponta a ponta | Não demonstrada por esta documentação |
| OCR manuscrito avaliado | Não demonstrado |
| Testes e métricas de desempenho | A definir e executar |
| Piloto com dados reais | Não declarado; depende de autorização e controles prévios |
| Integração com sistemas de produção | Fora do escopo inicial |

## Documentação

- [Visão da arquitetura](docs/architecture/overview.md) — fluxo, componentes e decisões em aberto.
- [Roadmap público](docs/roadmap.md) — etapas planejadas e critérios de saída.
- [Posicionamento de mercado e visão de plataforma](docs/market-and-platform-vision.md) — tese e hipóteses de evolução.
- [Análise competitiva preliminar](docs/competitive-landscape.md) — soluções relacionadas e limites das fontes.
- [Segurança e privacidade](SECURITY.md) — limites para dados, segredos e relato de vulnerabilidades.

## Mercado e divulgação

O SIBERIA não se posiciona como o primeiro OCR médico nem declara superioridade sobre soluções existentes. A hipótese de diferenciação está na adequação a um fluxo específico de boletins de enfermagem, revisão por campo, proveniência e rastreabilidade — pontos que precisam ser avaliados na prática.

Este repositório contém somente código e documentação apropriados à divulgação pública. Pesquisa restrita e planejamento confidencial permanecem fora desta superfície. Antes de publicar materiais, revise privacidade, confidencialidade, propriedade intelectual e sustentação factual das afirmações.

## Segurança e uso de dados

Não publique dados pessoais ou de saúde identificáveis, imagens reais de prontuários, assinaturas, credenciais, tokens, chaves, segredos ou documentos confidenciais. Repositórios privados também exigem controles de acesso e minimização de dados.

Use dados sintéticos em exemplos e testes públicos. O uso futuro de dados reais exige avaliação específica de finalidade, autorização, base legal, segurança, retenção e governança institucional.

---

**Estado geral:** pesquisa aplicada e desenvolvimento inicial.  
**Licença:** ainda não definida.
