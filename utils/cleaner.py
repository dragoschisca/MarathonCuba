import re

# ===================== STOPWORDS =====================
# Set de stopwords comune în engleză care vor fi eliminate din text
ENGLISH_STOPWORDS = {
    "a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at",
    "be","because","been","before","being","below","between","both","but","by",
    "could","couldn't",
    "did","didn't","do","does","doesn't","doing","don't","down","during",
    "each",
    "few","for","from","further",
    "had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's",
    "i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself",
    "let's",
    "me","more","most","mustn't","my","myself",
    "no","nor","not",
    "of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own",
    "same","she","she'd","she'll","she's","should","shouldn't","so","some","such",
    "than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too",
    "under","until","up",
    "very",
    "was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't",
    "you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"
}

# ===================== REGEX DEFINITIONS =====================
WORD_RE = re.compile(r"\b[\w'-]+\b", flags=re.UNICODE)   # detectează cuvinte cu apostrof sau cratimă
TOKEN_RE = re.compile(r"(\b[\w'-]+\b|[^\w\s])", flags=re.UNICODE)  # împarte textul în cuvinte și semne de punctuație
PUNCT_RE = re.compile(r"^[^\w\s]+$", flags=re.UNICODE)  # detectează doar punctuația

# ===================== FUNCȚII AUXILIARE =====================
def _reconstruct_from_tokens(tokens):
    """
    Reconstruiește linia originală din tokens, păstrând spațiile și punctuația corespunzător.
    - Tokens care sunt doar punctuație se lipesc de cuvântul anterior.
    - Restul cuvintelor se separă printr-un spațiu.
    """
    out = ""
    for tok in tokens:
        if tok == "":
            continue
        if PUNCT_RE.match(tok):
            out = out.rstrip() + tok
        else:
            if out and not out.endswith(" "):
                out += " "
            out += tok
    return out

# ===================== FUNCȚIA PRINCIPALĂ =====================
def remove_stopwords_from_line(line: str) -> str:
    """
    Elimină stopwords dintr-o linie de text.
    - Păstrează punctuația și spațiile corecte.
    - Returnează linia procesată cu stopwords eliminate.
    """
    has_newline = line.endswith("\n")  # păstrăm newline-ul dacă există
    tokens = TOKEN_RE.findall(line)   # sparge linia în tokens (cuvinte și semne)
    kept = []
    for tok in tokens:
        if WORD_RE.fullmatch(tok):  # dacă e cuvânt
            if tok.lower() not in ENGLISH_STOPWORDS:
                kept.append(tok)
        else:  # dacă e punctuație
            kept.append(tok)
    reconstructed = _reconstruct_from_tokens(kept).strip()
    if has_newline:
        reconstructed += "\n"
    return reconstructed

def remove_sigmoid_then_stopwords(line: str) -> str:
    """
    Elimină mențiunile 'Sigmoid' sau 'Sigmoid NGO(s)' din text (case-insensitive),
    apoi aplică filtrarea stopwords.
    - Această funcție este utilă când se curăță textul de referințe la termenul Sigmoid
      și se elimină cuvintele comune.
    """
    t = re.sub(r"\bSigmoid\s*NGO'?s?\b", "", line, flags=re.IGNORECASE)
    t = re.sub(r"\bSigmoid\b", "", t, flags=re.IGNORECASE)
    return remove_stopwords_from_line(t)
