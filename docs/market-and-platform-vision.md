# SIBERIA — posicionamento de mercado e visão de plataforma

**Status:** visão de produto em investigação; não é declaração de superioridade, implantação ou validação clínica.

## Problema investigado

O SIBERIA nasceu para investigar como reduzir o retrabalho de transcrever boletins manuscritos de enfermagem para sistemas digitais. O primeiro produto proposto recebe foto ou PDF, extrai campos candidatos, oferece revisão humana, mantém proveniência e histórico e exporta somente registros aprovados.

A necessidade e o benefício devem ser medidos em cada contexto; não presumimos que todos os hospitais operem da mesma forma.

## O mercado já tem soluções

OCR médico e processamento de documentos clínicos não são ideias novas. Exemplos públicos:

- **Dasa + Google Cloud:** leitura de pedidos médicos digitados e manuscritos para apoiar agendamento: https://cloud.google.com/customers/dasa?hl=pt-BR
- **Upstage Healthcare:** oferta de extração de registros clínicos manuscritos e documentos hospitalares: https://www.upstage.ai/solutions/healthcare
- **Saúde iD + Google Cloud:** OCR de guias e pedidos de saúde: https://cloud.google.com/customers/saude-id?hl=pt-br

Esses exemplos demonstram atividade de mercado em tarefas relacionadas; não são comparação independente nem provam que atendam a todo fluxo de enfermagem.

## Hipótese de diferenciação

O SIBERIA não se posiciona como “o primeiro OCR médico”. A hipótese a testar é uma solução especializada no fluxo de boletins de enfermagem, com:

1. Extração organizada pelo formulário e por campo.
2. Incerteza explícita, sem completar valores ausentes.
3. Revisão e aprovação humanas.
4. Vínculo entre cada campo e sua origem no documento quando disponível.
5. Histórico de processamento, correções e aprovações.
6. Avaliação de tempo, taxa de correção, falhas e erros por campo.
7. Integração com sistemas existentes apenas quando viável e formalmente autorizada.

São objetivos de projeto, não capacidades implementadas sem código, testes e avaliação.

## Visão de longo prazo: plataforma de soluções hospitalares

O SIBERIA Operacional pode vir a ser o primeiro produto de uma família de soluções para fluxos hospitalares. A plataforma é uma hipótese estratégica, não um produto atualmente disponível.

A evolução deve seguir: **problema específico → produto inicial → piloto controlado → resultados medidos → capacidades reutilizáveis → novos produtos priorizados.**

O repositório público abriga aplicação e documentação publicável. Pesquisa restrita, notas de descoberta, análise interna, riscos e decisões detalhadas ficam no Vault privado.

## Princípios

- A IA propõe; profissionais autorizados revisam e aprovam.
- Não inferir campos ausentes nem corrigir silenciosamente conteúdo clínico.
- Não usar dados clínicos reais sem autorização e governança.
- Não presumir integração com prontuários, AGHUse ou outros sistemas.
- Não publicar métricas sem protocolo e resultados reproduzíveis.
- Não declarar implantação, conformidade certificada ou validação clínica sem evidências.

## Referências iniciais

- Google Cloud — Dasa: https://cloud.google.com/customers/dasa?hl=pt-BR
- Upstage Healthcare: https://www.upstage.ai/solutions/healthcare
- Google Cloud — Saúde iD: https://cloud.google.com/customers/saude-id?hl=pt-br
- NHS England — orientação para adoção de ambient scribing com IA: https://www.england.nhs.uk/publication/guidance-on-the-use-of-ai-enabled-ambient-scribing-products/

Os casos de fornecedores são descrições de soluções e clientes, não estudos comparativos independentes.
