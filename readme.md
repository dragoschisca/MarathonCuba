# 🧹 Text Cleaner — Remove "Sigmoid" and Stopwords

## Storyline

Te plimbi pe o stradă aglomerată și observi ceva ciudat — semnele de oprire sunt peste tot, dar par inutile.
Un bilet misterios cade din cer:

> „I hate stop signs, I wish I never had them.”

Privind mai atent, îți dai seama că indiciul nu vorbește despre semne rutiere, ci despre **stopwords** — acele cuvinte comune care nu adaugă sens real textului.
Adevărata sarcină? Eliminarea „opriri(lor)” din text — adică a cuvintelor **inutile** și a termenului **Sigmoid**, ascuns peste tot.

---

## 🎯 Obiectiv

Primești un fișier text care conține mai multe propoziții.
Scopul tău este să **curăți textul**, eliminând:

* toate aparițiile cuvântului **“Sigmoid”** (indiferent de formă: *Sigmoid NGO, Sigmoid NGOs*, etc.);
* toate **stopwords-urile comune în limba engleză** (precum *and, the, to, of*, etc.).

Rezultatul trebuie salvat într-un fișier text curat, cu aceeași structură de linii ca fișierul original.

---

## 🧩 Analiza Task-ului

Task-ul combină două cerințe principale:

1. **Eliminarea oricărei referințe la “Sigmoid”** din text;
2. **Eliminarea stopwords-urilor**, menținând totodată **punctuația și formatul inițial**.

Pentru aceasta, scriptul:

* citește fișierul de intrare `participant_input/input.txt`;
* procesează fiecare linie individual;
* scrie rezultatul în `output/output.txt`, păstrând newline-urile originale.

---

## ⚙️ Soluția Implementată

### 🔧 Structura fișierelor

```
.
├── participant_input/
│   ├── input.txt
│   └── hint.jpg
├── output/
│   └── output.txt
├── utils/
│   └── cleaner.py
└── main.py
```

### 🧠 Logica principală

* `remove_sigmoid_then_stopwords(line)`
  → Elimină mențiunile „Sigmoid” și aplică filtrarea stopwords.
* `remove_stopwords_from_line(line)`
  → Tokenizează textul, verifică fiecare cuvânt și reconstruiește linia păstrând semnele de punctuație.

### 🧩 Regex-uri folosite

* `WORD_RE`: identifică cuvinte;
* `TOKEN_RE`: separă cuvintele și semnele de punctuație;
* `PUNCT_RE`: recunoaște doar semnele de punctuație.

---

## ▶️ Cum se rulează

1. Asigură-te că structura de directoare este corectă.
2. Rulează scriptul principal:

   ```bash
   python main.py
   ```
3. Scriptul va genera automat fișierul curățat:

   ```
   output/output.txt
   ```
4. În consolă va apărea mesajul:

   ```
   ✅ Fișierul curățat a fost salvat în: output/output.txt
   ```

---

## 📂 Input & Output

### Input

* **Fișier:** `participant_input/input.txt`
* **Conținut:** Text brut cu mențiuni despre *Sigmoid* și cuvinte comune (stopwords).

### Output

* **Fișier:** `output/output.txt`
* **Format:** Text curățat, fără „Sigmoid” și fără stopwords.
* **Cerințe:**

  * Păstrează structura originală (un rând per propoziție);
  * Spațiile între cuvinte trebuie să fie simple;
  * Fișierul trebuie salvat în format UTF-8.

---

## 🏁 Exemplu

### Input:

```
Sigmoid NGOs are the best in the world.
They work in many countries and help people.
```

### Output:

```
NGOs best world.
work many countries help people.
```

---

## 🏆 Scoring Criteria

Performanța este evaluată prin compararea textului curățat cu soluția așteptată:

| Criteriu        | Punctaj             |
| --------------- | ------------------- |
| 100% potrivire  | ✅ 100 puncte (PASS) |
| ≥ 90% potrivire | ✅ 90+ puncte (PASS) |
| < 90% potrivire | ❌ FAIL              |

