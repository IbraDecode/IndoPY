import re

def translate_indo(kode: str) -> str:
    hasil_lines = []
    for raw in kode.split('\n'):
        line = raw.strip()
        if line.startswith("--"):
            comment_text = line[2:].strip()
            hasil_lines.append("# " + comment_text)
            continue

        # Handle 'jika kondisi lain' before 'jika'
        line = re.sub(r"\bjika kondisi lain\b", "elif", line)
        line = re.sub(r"\bjika tidak\b", "else", line)
        line = re.sub(r"\bjika\b", "if", line)

        line = re.sub(r"\bselama\b", "while", line)
        line = re.sub(r"\buntuk\b", "for", line)
        line = re.sub(r"\bdalam\b", "in", line)

        line = re.sub(r"\bfungsi\b", "def", line)
        line = re.sub(r"\bkembali\b", "return", line)
        line = re.sub(r"\bkelas\b", "class", line)

        line = re.sub(r"\bdan\b", "and", line)
        line = re.sub(r"\batau\b", "or", line)
        line = re.sub(r"\bbukan\b", "not", line)

        line = re.sub(r"\bbenar\b", "True", line)
        line = re.sub(r"\bsalah\b", "False", line)

        line = re.sub(r"\btulis\b", "print", line)
        line = re.sub(r"\bmasukan\b", "input", line)
        line = re.sub(r"\bacak\b", "random", line)
        line = re.sub(r"\bwaktu\b", "time", line)
        line = re.sub(r"\bbuka\b", "open", line)
        line = re.sub(r"\bhapus\b", "os.remove", line)

        line = re.sub(r"\bpakai\b", "import", line)

        line = re.sub(r"\bcoba\b", "try", line)
        line = re.sub(r"\bjika error\b", "except", line)
        line = re.sub(r"\bakhir\b", "finally", line)

        # Remove 'selesai' as it's not needed in Python (indentation handles blocks)
        line = re.sub(r"\bselesai\b", "", line)

        indent = raw[:len(raw) - len(raw.lstrip(' '))]
        hasil_lines.append(indent + line)

    return "\n".join(hasil_lines)


