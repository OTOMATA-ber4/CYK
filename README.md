Cocke–Younger–Kasami (CYK) algorithm

Algoritma CYK menentukan apakah string dapat dihasilkan oleh context-free grammar tertentu. Algoritma ini bekerja dengan:

1. **Tabel Pemrograman Dinamis**: Membangun tabel n×n di mana n adalah panjang string
2. **Penguraian Bottom-up**: Mengisi tabel dari substring yang lebih pendek ke yang lebih panjang
3. **Persyaratan CNF**: Tata bahasa harus dalam Bentuk Normal Chomsky:

- Produksi harus berupa:
- A → BC (dua non-terminal)
- A → a (terminal tunggal)

Contoh:
Diberikan sebuah grammar

grammar = {
        "S": ["AB", "BC"],
        "A": ["BA", "a"],
        "B": ["CC", "b"],
        "C": ["AB", "a"]
    }

dengan start_symbol = "S" dan input_string = "baaba"

Program akan mengecek apakah string 'baaba' bisa di parsing ke CYK tabel? Dalam kasus ini bisa dengan tabelnya sebagai berikut

['B', 'A,C', 'A,C', 'B', 'A,C']
['A,S', 'B', 'C,S', 'A,S', '-']
['-', 'B', 'B', '-', '-']
['-', 'A,C,S', '-', '-', '-']
['A,C,S', '-', '-', '-', '-']

Baris 1 -> Setiap 1 kata dari 'baaba' akan dibuat simbol, kata pertama 'b' dengan simbol "B", kata kedua 'a' dengan kemungkinan simbol "A" atau "C" sampai seterusnya
Baris 2 -> Setiap 2 kata, kata pertama 'ba' dengan simbol "A" ("BA") atau "S" ("B" dengan "C", dalam hal ini termasuk di simbol "S")
Seterusnya hingga panjang kata terakhir yaitu baris ke-5. Untuk melihat kesimpulan apakah input dapat diparsing, cukup lihat pada barise ke-5, apakah dalam tabel tersebut terdapat start_symbol? Jika ada maka bisa, jika tidak ada maka tidak bisa.


