import os
from utils.cleaner import remove_sigmoid_then_stopwords

INPUT_DIR = "participant_input"
OUTPUT_DIR = "output"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines(keepends=True)  # păstrăm newline-urile


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    input_path = os.path.join(INPUT_DIR, INPUT_FILE)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

    # Citim toate liniile din input
    lines = read_lines(input_path)

    # Aplicăm funcția care elimină "Sigmoid" + stopwords
    cleaned_lines = [remove_sigmoid_then_stopwords(line) for line in lines]

    # Scriem totul într-un singur fișier
    write_lines(output_path, cleaned_lines)

    print(f"✅ Fișierul curățat a fost salvat în: {output_path}")


if __name__ == "__main__":
    main()
