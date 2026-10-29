# Monta artifact/ a partir da raiz para publicar como Artifact do Claude.
# Uso: python3 tools/montar_artifact.py
# - artifact/index.html: sem <!doctype>/<html>/<head>/<body> (o Artifact coloca o esqueleto)
# - artifact/vendor/unicorn_arm.js: bytes de controle do WASM embutido viram \xHH
#   (o Artifact recusa texto com byte ESC); a string resultante é a mesma.
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "artifact"
(OUT / "vendor").mkdir(parents=True, exist_ok=True)

html = (ROOT / "index.html").read_text(encoding="utf-8")
head = re.match(r"\s*<!doctype html>\s*<html[^>]*>\s*<head>(.*?)</head>\s*<body>", html, re.S | re.I)
assert head, "cabeçalho inesperado no index.html"
keep = [l for l in head.group(1).strip().splitlines()
        if not re.search(r'<meta (charset|content="width|content="#)', l)]
body = html[head.end():]
body = re.sub(r"\s*</body>\s*</html>\s*$", "\n", body, flags=re.I)
page = (
    "<!-- Cópia do Cortex Lab (GPL-2.0-or-later). Gerado por tools/montar_artifact.py a partir de index.html. -->\n"
    + "\n".join(l.strip() for l in keep)
    + '\n<script>document.documentElement.lang = "pt-BR";</script>\n'
    + body.lstrip("\n")
)
(OUT / "index.html").write_text(page, encoding="utf-8")

src = (ROOT / "vendor" / "unicorn_arm.js").read_bytes()
start = src.index(b"binaryDecode('") + len(b"binaryDecode('")
out = bytearray(src[:start])
i = start
while src[i] != 0x27:
    b = src[i]
    if b in (0x0A, 0x0D):
        raise SystemExit(f"quebra de linha dentro da string em {i}")
    if b == 0x5C:
        nxt = src[i + 1]
        out += b"\\x%02x" % nxt if nxt < 32 and nxt not in (9, 10, 13) else src[i:i + 2]
        i += 2
        continue
    out += b"\\x%02x" % b if b < 32 and b != 9 else bytes([b])
    i += 1
out += src[i:]
assert not any(c < 32 and c not in (9, 10, 13) for c in out)
(OUT / "vendor" / "unicorn_arm.js").write_bytes(out)
print("artifact/index.html e artifact/vendor/unicorn_arm.js prontos")
