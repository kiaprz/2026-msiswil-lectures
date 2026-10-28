# Analiza danych i uczenie maszynowe w Pythonie

Przykłady dydaktyczne w notebookach Jupyter i skryptach Pythona opracowywane i prezentowane podczas wykładów z przedmiotu "Metody sztucznej inteligencji w systemach wytwarzania i intralogistyki" (edycja 2026/27). 

## Uruchomienie w VS Code

1. Otwórz główny folder projektu przez **File → Open Folder**.
2. Zainstaluj rozszerzenia **Python** i **Jupyter** firmy Microsoft.
3. W terminalu VS Code, w głównym folderze projektu, utwórz lokalne środowisko i zainstaluj zależności.

   macOS / Linux:

   ```bash
   python3 -m venv .venv
   .venv/bin/python -m pip install -r requirements.txt
   ```

   Windows (PowerShell):

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

4. W poleceniu **Python: Select Interpreter** wybierz interpreter z `.venv`.
5. W notebooku kliknij **Select Kernel** i wybierz środowisko `.venv`.
6. Uruchamiaj komórki notebooka od początku (najlepiej całość opcją 'Run All'). Skrypty `.py` uruchamiaj przez **Python: Run Python File in Terminal**, pozostawiając terminal w głównym folderze projektu.

Plik `.vscode/settings.json` zawiera ustawienia projektu: wskazuje lokalne środowisko `.venv`, ustawia katalog roboczy notebooków na główny folder projektu i wyłącza przechodzenie do folderu skryptu przy uruchamianiu plików `.py`. Po zmianie ustawień zrestartuj uruchomiony kernel notebooka.

## Pliki z danymi

Wspólne zbiory danych przechowujemy w folderze `datasets/`. Ścieżki w notebookach i skryptach podajemy względem głównego folderu projektu:

```python
import pandas as pd

df = pd.read_csv("datasets/ai4i2020.csv")
df.head()
```

Przy uruchamianiu z terminala również pozostań w głównym folderze projektu, np. na macOS / Linux:

```bash
.venv/bin/python classification/single_prompt_naive_classifier.py
```

Środowisko `.venv` tworzy każdy użytkownik lokalnie; jest pomijane przez Git. Ustawienia `.vscode/settings.json` należy przechowywać w repozytorium razem z kodem i danymi.
