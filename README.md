## Zakres:
- Python OOP
- Python zaawansowany
- Testy jednostkowe
- Zasady czystego kodu
- Bazy danych

## Cele:
### Zadanie ma na celu odświeżenie wiedzy nabytej przez ostatnie miesiące pracy z tematami.


## Wymagania niefunkcjonalne:
- Kod staramy utrzymać się w czystej strukturze projektu
- Kod piszemy po angielsku
- Docstringi mile widziane
- Rozwiązanie dostarczamy w formie Pull Requesta na GitHubie
- Wymagania niżej zostały celowo spisane dość ogólnikowo, aby dać Tobie możliwość własnej kreatywności i utworzenia odpowiedniej ilości klas.


# Wymagania ogólne:
## Modelowanie i zarządzanie pojazdami
- System musi posiadać możliwość przechowywania informacji o różnych typach pojazdów dostępnych w wypożyczalni. Mogą to być różne typy pojazdów, takie jak samochody, motocykle, ciężarówki itp. Zastanów się, jak te obiekty mogą być powiązane, jakie mają wspólne cechy, a co je odróżnia.
- Powinna istnieć możliwość dodawania nowych pojazdów, aktualizowania ich stanu (np. dostępny, wypożyczony) oraz przechowywania informacji na temat każdego pojazdu.
## Obsługa procesu wypożyczenia pojazdu
- System musi zapewniać funkcjonalność rezerwacji pojazdu przez klienta. Zastanów się, jakie informacje musisz przechowywać, aby rezerwacja była możliwa, i jak obsłużyć sytuację, gdy pojazd jest niedostępny.
- Wypożyczenie powinno uwzględniać daty rozpoczęcia i zakończenia oraz dane klienta. Pomyśl, jakie klasy i struktury mogą być przydatne do obsługi takiego procesu.
## Wzorce projektowe
- W systemie musi zostać zaimplementowany wzorzec projektowy, który uprości zarządzanie dostępnością pojazdów i procesem wypożyczenia, tak aby użytkownik (klient) miał uproszczony interfejs korzystania z systemu. Przemyśl, jak można ukryć skomplikowane procesy wewnętrzne (np. poprzez wzorzec fasady) i jakie elementy systemu powinny być dostępne bezpośrednio, a które lepiej obsłużyć "w tle".
## Integracja zaawansowanych funkcji Pythona
- W systemie muszą być użyte dekoratory do dodatkowego rozszerzenia funkcjonalności (np. do logowania operacji, autoryzacji lub rejestracji błędów; możesz wybrać dowolną). Wybierz odpowiednie momenty, w których użycie dekoratora przyniosłoby korzyści.
- System powinien wykorzystywać generatory do zarządzania listą dostępnych pojazdów, np. do efektywnego przechodzenia przez wszystkie pojazdy określonego typu.
- Obsłuż wyjątki, które mogą wystąpić podczas procesu wypożyczenia, płatności, czy dodawania pojazdu (np. pojazd niedostępny, niepoprawne dane).
## Testy jednostkowe
- System powinien być dobrze przetestowany. Zdefiniuj kluczowe funkcjonalności, które będą wymagały testów (np. rezerwacja pojazdu, sprawdzanie dostępności, obliczanie kosztów).
- Użyj pytest do napisania testów jednostkowych. Pamiętaj, aby obejmowały zarówno przypadki poprawne, jak i sytuacje wyjątkowe.
## Obsługa danych (SQLite)
- Dane o pojazdach, klientach i rezerwacjach powinny być przechowywane w bazie danych. Wykorzystaj do tego SQLite.
- Przemyśl, jakich operacji potrzebujesz w bazie danych, aby umożliwić pełen cykl zarządzania pojazdami (dodawanie, modyfikowanie, usuwanie, wyszukiwanie).
- Zastanów się, jak najlepiej przechowywać informacje o wypożyczeniach i ich relacji do klientów oraz pojazdów.
## Formatowanie i analiza kodu
- Kod powinien być zgodny ze standardami PEP8. Zaplanuj wykorzystanie narzędzi, które pomogą Ci utrzymać czysty kod (np. black do automatycznego formatowania oraz flake8 do analizy kodu).
- Zastanów się, jak zapewnić, że cały zespół pracujący nad projektem (w tym Ty!) będzie przestrzegać ustalonych standardów jakości kodu.



# Wskazówki
## Modelowanie Pojazdów i Klientów:
- Zidentyfikuj wspólne cechy pojazdów, aby określić, które elementy można przenieść do klasy bazowej, a co powinno zostać w klasach dziedziczących.
- Określ, jakie dane o kliencie będą potrzebne w celu zarejestrowania wypożyczenia.
## Proces Wypożyczenia:
- Zastanów się, jakie kroki są potrzebne, aby wypożyczyć pojazd – od sprawdzenia dostępności, przez zapisanie informacji o kliencie, po finalizację wypożyczenia.
- Uprość proces z perspektywy klienta (np. jeden punkt kontaktu, który obsłuży wszystkie skomplikowane operacje w tle). W jaki sposób można to osiągnąć za pomocą odpowiedniego wzorca projektowego?
## Płatności:
- Zaprojektuj moduł do obsługi płatności, który pozwoli na przyszłe rozszerzenie o różne metody płatności (np. karta kredytowa, przelew bankowy). Jakie klasy mogą pomóc w realizacji tej elastyczności?
## Dekoratory i Generatory:
- Zidentyfikuj, które operacje w systemie mogą być logowane lub monitorowane za pomocą dekoratorów.
- W których momentach generator ułatwiłby przechodzenie przez dostępne pojazdy, szczególnie gdy dane mogą być duże?
## Testowanie:
- Przemyśl, które aspekty Twojego systemu są najważniejsze z punktu widzenia użytkownika i jak je przetestować, aby zapewnić ich poprawność.
- Jakie nietypowe sytuacje mogą się pojawić (np. brak pojazdów, niepoprawne daty) i jak powinny zostać obsłużone?
## Baza Danych:
- Przemyśl struktury tabel potrzebne do przechowywania informacji o pojazdach, klientach i wypożyczeniach.
- Jakie relacje powinny być stworzone, aby system mógł sprawnie obsługiwać wszystkie operacje?

