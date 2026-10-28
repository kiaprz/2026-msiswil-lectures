# Instrukcje dla agenta

## Cel

Twórz materiały dla początkującego data scientista. Priorytetem jest prosty, zwięzły kod, który łatwo przeczytać i samodzielnie zmodyfikować.

## Środowisko i biblioteki

- Pisz kod w notebookach Jupyter (`.ipynb`).
- Używaj Pythona z lokalnego środowiska `.venv` i wybieraj je jako kernel notebooka.
- Uruchamiaj polecenia przez `.venv/bin/python`, a instalację pakietów przez `.venv/bin/python -m pip`.
- Używaj `pandas` do wczytywania i analizy danych, `seaborn` do wykresów oraz `scikit-learn` do uczenia maszynowego.
- Importuj tylko potrzebne biblioteki. Stosuj standardowe aliasy: `pd` dla `pandas`, `sns` dla `seaborn`.
- Nowe wymagane pakiety dopisuj do `requirements.txt`. Pakiet `scikit-learn` importuje się jako `sklearn`.

## Prostota kodu

- Każdy przykład ma pokazywać jedno konkretne zastosowanie, np. wczytanie pliku, obliczenie średniej lub wygenerowanie pojedynczego wykresu.
- Pisz krótkie komórki z bezpośrednimi wywołaniami instrukcji i metod.
- Wybieraj najprostsze rozwiązanie wystarczające do zadania. Unikaj nadmiernie uniwersalnych funkcji, klas, konfiguracji i dodatkowych warstw abstrakcji.
- Nie twórz pętli generujących wiele wykresów ani rozbudowanych zestawów modeli, jeśli zadanie dotyczy pojedynczego przykładu.
- Nie dodawaj zbędnej obsługi wyjątków, sprawdzania wszystkich możliwych przypadków ani infrastruktury produkcyjnej.
- Używaj czytelnych nazw zmiennych i jawnych kroków. Unikaj skomplikowanych wyrażeń oraz długich łańcuchów metod.
- Dodawaj krótkie wyjaśnienia po polsku w komórkach Markdown. Komentarze w kodzie stosuj tylko wtedy, gdy pomagają zrozumieć operację.

## Organizacja notebooków

- Zachowuj logiczną kolejność: importy, wczytanie danych, podgląd, analiza, a następnie modelowanie, jeśli jest potrzebne.
- Korzystaj ze ścieżek względnych do plików projektu.
- Wyświetlaj wyniki bezpośrednio w notebooku, np. przez `df.head()` lub wynik ostatniego wyrażenia w komórce.
- Twórz pojedyncze, czytelne wykresy z opisanymi osiami. Używaj `matplotlib` pomocniczo, gdy wymaga tego formatowanie wykresu.
- Dostosowuj zakres pracy do polecenia: prosty wykres nie wymaga pełnego procesu analizy ani modelu.
- Przy edycji istniejącego notebooka zachowuj treści niezwiązane z zadaniem.

## Podstawy modelowania

- Pokazuj jeden prosty model i odpowiednią do zadania metrykę, chyba że użytkownik prosi o porównanie.
- Dziel dane na zbiór treningowy i testowy przed dopasowaniem modelu oraz przekształceń uczących się z danych.
- Dopasowuj przekształcenia wyłącznie na danych treningowych i stosuj je do danych testowych.
- Ustawiaj `random_state=42` w operacjach losowych, które udostępniają ten parametr.
- Nie dodawaj strojenia hiperparametrów ani rozbudowanych pipeline'ów bez wyraźnej potrzeby.

## Weryfikacja

- Sprawdzaj, czy zmieniony kod działa przy wykonywaniu komórek od początku, bez polegania na ukrytym stanie kernela.
- Nie przedstawiaj kodu jako sprawdzonego, jeśli nie został uruchomiony. Krótko wskaż ewentualne ograniczenia weryfikacji.
- Nie twórz rozbudowanych testów do prostych przykładów dydaktycznych; sprawdź wykonanie komórek i sensowność wyników.
- przy dobieraniu hiperparametrów i porównywaniu algorytmów stosuj wskaźnik f1
