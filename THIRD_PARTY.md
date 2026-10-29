# Cortex Lab — licenças e fontes

Código da interface e periféricos virtuais: GPL-2.0-or-later. Sem garantia. O texto da GPLv2 está em `vendor/unicorn-LICENSE`.

## Unicorn.js / Unicorn

- Wrapper: Alexandro Sanchez Bach; motor: Nguyen Anh Quynh, Dang Hoang Vu e demais contribuidores.
- Pacote: `@alexaltea/unicorn-js@2.1.4`, GPL-2.0, licença incluída em `vendor/unicorn-LICENSE`.
- Fonte do wrapper: https://github.com/AlexAltea/unicorn.js/tree/560284c59c11c8d6c94d537f4354339f069ddcdf
- Fonte do motor: https://github.com/unicorn-engine/unicorn/tree/2.1.4
- Pacote original: https://registry.npmjs.org/@alexaltea/unicorn-js/-/unicorn-js-2.1.4.tgz
- Modificação Cortex Lab, 22/10/2026: seletor WASM do modelo MCLASS exportado como global `lab_model` (8=M3, 9=M4), em vez de fixo em M33; wrapper aceita `wasmBinary` e expõe essa global. A lógica de execução das instruções não foi reimplementada. Receita reproduzível e wrapper upstream incluídos no repositório: `tools/build-cpu.cjs`, `tools/unicorn_arm.upstream.cjs`.

## Keystone.js / Keystone

- `@alexaltea/keystone-js@0.9.2`, GPL-2.0. Sem modificações.
- Licença: `vendor/keystone-LICENSE`.
- Wrapper e receita: https://github.com/AlexAltea/keystone.js/tree/7693b038edb6b3352937daeab39321a784fa9075
- Motor: https://github.com/keystone-engine/keystone
- Pacote: https://registry.npmjs.org/@alexaltea/keystone-js/-/keystone-js-0.9.2.tgz

## Capstone.js / Capstone

- `@alexaltea/capstone-js@5.0.9`, BSD-3-Clause. Sem modificações.
- Licença: `vendor/capstone-LICENSE`.
- Wrapper e receita: https://github.com/AlexAltea/capstone.js/tree/52da0b9c931a9f40255461250310cc96cb45c945
- Motor: https://github.com/capstone-engine/capstone
- Pacote: https://registry.npmjs.org/@alexaltea/capstone-js/-/capstone-js-5.0.9.tgz

As receitas upstream identificam os submódulos correspondentes dos motores. Créditos e licenças dos componentes internos permanecem aplicáveis. Todos os scripts da interface são servidos em código-fonte legível. As bibliotecas são servidas localmente, sem CDN.

## Modificações nesta cópia (29/10/2026)

Cópia de https://cortex-lab-eduardo.jaunty-toad-7038.chatgpt.site. O original sem alterações está em `original/`.

- `index.html`, `app.js`: botão "↓ .bin + .hex", aba Startup, aviso de cópia no rodapé e downloads compatíveis com o Artifact do Claude.
- Novos: `zip.js`, `startup-ui.js`, `startup.css`, `startups.js` (gerado de `startups/`).
- Startups da ST (`startups/startup_stm32*.s`): arquivos oficiais de STMicroelectronics/cmsis-device-f4 e cmsis-device-f1, sem alteração, Apache-2.0 (`startups/LICENSE-ST-*.md`).
- Startups da TI (`startups/startup_tm4c*.s`): escritos para esta cópia; posições e nomes dos vetores tirados de `inc/hw_ints.h` do TivaWare 2.2.0.295.
