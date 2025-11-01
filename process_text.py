import re
import os

def remove_stop_signs(text):

    cleaned_text = re.sub(r'\bSTOP\b', '', text, flags=re.IGNORECASE)

    cleaned_text = re.sub(r' +', ' ', cleaned_text)

    lines = cleaned_text.split('\n')
    cleaned_lines = [line.strip() for line in lines]

    cleaned_lines = [line for line in cleaned_lines if line]

    return '\n'.join(cleaned_lines)


def process_file(input_path, output_path):
    try:
        # Read input file
        with open(input_path, 'r', encoding='utf-8') as f:
            input_text = f.read()

        print(f"✓ Read input file: {input_path}")
        print(f"  Original text length: {len(input_text)} characters")

        # Process the text
        cleaned_text = remove_stop_signs(input_text)

        print(f"✓ Processed text")
        print(f"  Cleaned text length: {len(cleaned_text)} characters")

        # Write output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)

        print(f"✓ Written output file: {output_path}")
        print("\n✅ Task completed successfully!")

    except FileNotFoundError:
        print(f"❌ Error: Input file not found at {input_path}")
        print("   Please ensure the file exists in the participant_input folder.")
    except Exception as e:
        print(f"❌ Error processing file: {str(e)}")


def main():
    # Define file paths
    input_file = os.path.join('participant_input', 'input.txt')
    output_file = 'output.txt'

    print("=" * 60)
    print("LMML Task: Stop Sign Removal")
    print("=" * 60)
    print()

    # Process the file
    process_file(input_file, output_file)


if __name__ == "__main__":
    main()