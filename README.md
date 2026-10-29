# Cortex Lab (cópia)

IDE web de Assembly ARM Cortex-M com simulador de STM32 e Tiva C (Unicorn + Keystone + Capstone em WebAssembly).

Site: https://prustt.github.io/cortex-lab

Cópia de https://cortex-lab-eduardo.jaunty-toad-7038.chatgpt.site, com:

- botão **↓ .bin + .hex**;
- aba **Startup** com os arquivos de inicialização dos 5 micros (GNU e Keil);
- aba **Placa real**: grava e monitora a EK-TM4C1294XL (e a EK-TM4C123GXL) pelo depurador ICDI da placa, direto do navegador (WebUSB), com terminal serial (Web Serial). Precisa de Chrome ou Edge no computador.

Detalhes em [LEIA-ME.md](LEIA-ME.md). Licenças em [THIRD_PARTY.md](THIRD_PARTY.md) (GPL-2.0-or-later; startups da ST em Apache-2.0).
