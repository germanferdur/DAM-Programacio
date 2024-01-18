import subprocess

def run_test(test_file):
    result = subprocess.run(['python', test_file], capture_output=True, text=True)
    print(f"Running {test_file}:\n")
    print(result.stdout)  # Sortida estàndard (incloent resultats de test)
    print(result.stderr)  # Errors, si n'hi ha
    print('-' * 60)
test_files = ['17b Test entrenament examen 3 - e0.py',
              '17b Test entrenament examen 3 - e1.py',
              '17b Test entrenament examen 3 - e2.py',
              '17b Test entrenament examen 3 - e3.py']

for file in test_files:
    run_test(file)
