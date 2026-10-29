# Cópia do Cortex Lab

Original: https://cortex-lab-eduardo.jaunty-toad-7038.chatgpt.site (baixado em 29/10/2026).
Licença: GPL-2.0-or-later (ver `THIRD_PARTY.md` e `vendor/*-LICENSE`).
Online (Artifact privado): https://claude.ai/artifact/Au8M1n31Hx3i5tYTFuNRGz

## Pastas

- `original/`: o site como foi baixado, sem alterações (só sem o script que o Cloudflare injeta).
- Raiz: a versão com as nossas mudanças:
  - botão **↓ .bin + .hex** ao lado do Build (faz o Build e gera os dois arquivos);
  - aba **Startup** com o startup de cada um dos 5 micros, em GNU (GCC) e Keil (ARMASM);
  - downloads que funcionam dentro do Artifact (lá `.s`, `.bin`, `.hex` e `.vcd` vêm dentro de um `.zip`);
  - simulador aceita escrita no SYSCTL (Tiva: PRx acompanha RCGCx) e no RCC (STM32), para o mesmo
    programa ligar os clocks como na placa real;
  - `placa-imagem.js`: imagem para a Flash da placa (vetores em `flashBase`, `b .` em +0x3FC,
    programa em +0x400); exemplo **08 · Placa EK-TM4C1294XL** (TM4C1294NCPDT).
- `startups/`: os 10 arquivos de startup.
  - ST (F411, F407, F103): arquivos oficiais do CMSIS da ST, sem alteração (licença Apache-2.0 junto).
  - TI (TM4C123GH6PM, TM4C1294NCPDT): escritos a partir das tabelas do TivaWare 2.2.0.295 (`inc/hw_ints.h`).
- `startups.js`: gerado a partir de `startups/` por `tools/gerar_startups_js.py`.
- `artifact/`: só o que muda para publicar como Artifact, gerado por `tools/montar_artifact.py`
  (`index.html` sem o esqueleto HTML; `vendor/unicorn_arm.js` com os bytes de controle escapados).

## Depois de mexer em algo

```bash
python3 tools/gerar_startups_js.py
python3 tools/montar_artifact.py
```

Depois peça ao Claude para republicar o Artifact (mesmo arquivo `artifact/index.html`).

## Rodar localmente

```bash
python3 -m http.server 8765 --directory /Users/l.prust/Documents/Embarcados/cortex-lab-copia
```

Depois abra http://localhost:8765. Abrir o `index.html` direto pelo Finder não funciona porque o navegador bloqueia os `.wasm` via `file://`.
