import random

print("Source Code by Brysonliem")

# Daftar ayat-ayat Alkitab
renungan_alkitab = {
    "Kolose 3:13": "“Sabarlah kamu seorang terhadap yang lain, dan ampunilah seorang akan yang lain apabila yang seorang menaruh dendam terhadap yang lain, sama seperti Tuhan telah mengampuni kamu, kamu perbuat jugalah demikian.”",
    "Pengkhobah 7:8": "“Akhir suatu hal lebih baik daripada awalnya. Panjang sabar lebih baik daripada tinggi hati.”",
    "Yakobus 5:7-8": "“Karena itu, saudara-saudara, bersabarlah sampai kepada kedatangan Tuhan! Sesungguhnya petani menantikan hasil yang berharga dari tanahnya dan ia sabar sampai telah turun hujan musim gugur dan hujan musim semi. Kamu juga harus bersabar dan harus meneguhkan hatimu, karena kedatangan Tuhan sudah dekat!”",
    "Yakobus 1:19-20": "“Hai saudara-saudara yang kukasihi, ingatlah hal ini: setiap orang hendaklah cepat untuk mendengar, tetapi lambat untuk berkata-kata, dan juga lambat untuk marah; sebab amarah manusia tidak mengerjakan kebenaran di hadapan Allah.”",
    "Yakobus 1:12": "“Berbahagialah orang yang bertahan dalam pencobaan, sebab apabila ia sudah tahan uji, ia akan menerima mahkota kehidupan yang dijanjikan Allah kepada barangsiapa yang mengasihi Dia.”",
    "Roma 12:12": "“Bersukacitalah dalam pengharapan, sabarlah dalam kesesakan, dan bertekunlah dalam doa!”",
    "Amsal 14:17": "“Siapa lekas naik darah, berlaku bodoh, tetapi orang yang bijaksana, besabar.”",
    "Amsal 15:18": "“Si pemarah membangkitkan pertengkaran, tetapi orang yang sabar memadamkan perbantahan.”",
    "Amsal 16:32": "“Orang yang sabar melebihi seorang pahlawan, orang yang menguasai dirinya, melebihi orang yang merebut kota.”",
    "Amsal 25:15": "“Dengan kesabaran seorang penguasa dapat diyakinkan dan lidah lembut mematahkan tulang.”",
    "Efesus 4:2": "“Hendaklah kamu selalu rendah hati, lemah lembut, dan sabar. Tunjukkanlah kasihmu dalam hal saling membantu.”",
    "Ibrani 6:12": "“Agar kamu jangan menjadi lamban, tetapi menjadi penurut-penurut mereka yang oleh iman dan kesabaran mendapat bagian dalam apa yang dijanjikan Allah.”",
    "Timotius 6:10-11": "“Karena akar segala kejahatan ialah cinta uang. Sebab oleh memburu uanglah beberapa orang telah menyimpang dari iman dan menyiksa dirinya dengan berbagai-bagai duka. Tetapi engkau hai manusia Allah, jauhilah semuanya itu, kejarlah keadilan, ibadah, kesetiaan, kasih, kesabaran dan kelembutan.”",
    "Yohanes 3:36": "“Barangsiapa percaya kepada Anak, ia beroleh hidup yang kekal, tetapi barangsiapa tidak taat kepada Anak, ia tidak akan melihat hidup, melainkan murka Allah tetap ada di atasnya.”",
    "Yohanes 14:16": "“Aku akan minta kepada Bapa, dan Ia akan memberikan kepadamu seorang Penolong yang lain, supaya Ia menyertai kamu selama-lamanya.”",
    "Yohanes 14:20": "“Percayalah, Tuhan selalu menyertai kita karena kita di dalam-Nya dan dia di dalam kita.”",
    "Yesaya 46:4": "“Sampai masa tuamu Aku tetap Dia dan sampai masa putih rambutmu Aku menggendong kamu. Aku telah melakukannya dan mau menanggung kamu terus; Aku mau memikul kamu dan menyelamatkan kamu.”",
    "Yesaya 40:31": "“Tetapi orang-orang yang menanti-nantikan TUHAN mendapat kekuatan baru: mereka seumpama rajawali yang naik terbang dengan kekuatan sayapnya; mereka berlari dan tidak menjadi lesu, mereka berjalan dan tidak menjadi lelah.”",
    "Yeremia 32:40": "“Perjanjian Allah mengenai keselamatan.”",
    "Wahyu 14:12": "“Kesabaran kita berkaitan dengan kualitas hubungan antara kita dengan Allah. Ketekunan orang-orang kudus menuruti perintah Allah dan iman kepada Yesus.”",
    "Ulangan 31:8": "“Sebab Tuhan, Dia sendiri akan berjalan di depanmu, Dia sendiri akan menyertai engkau, Dia tidak akan membiarkan engkau dan tidak akan meninggalkan engkau; janganlah takut dan janganlah patah hati.”",
    "Mazmur 62:1-2": "“Untuk pemimpin biduan. Menurut: Yedutun. Mazmur Daud. Hanya dekat Allah saja aku tenang, daripada-Nyalah keselamatanku. Hanya Dialah gunung batuku dan keselamatanku, kota bentengku, aku tidak akan goyah.”",
    "Mazmur 116:7": "“Kembalilah tenang, hai jiwaku, sebab Tuhan telah berbuat baik kepadamu.”",
    "Mazmur 55:23": "“Serahkanlah kuatirmu kepada Tuhan, maka Ia akan memelihara engkau! Tidak untuk selama-lamanya dibiarkan-Nya orang benar itu goyah.”",
    "Amsal 14:30": "“Hati yang tenang menyegarkan tubuh, tetapi iri hati membusukkan tulang.”",
    "Pengkhotbah 4:6": "“Segenggam ketenangan lebih baik daripada dua genggam jerih payah dan usaha menjaring angin.”",
    "Matius 6:26": "“Pandanglah burung-burung di langit, yang tidak menabur dan tidak menuai dan tidak mengumpulkan bekal dalam lumbung, namun diberi makan oleh Bapamu yang di sorga. Bukankah kamu jauh melebihi burung-burung itu?”",
    "Matius 6:34": "“Sebab itu janganlah kamu kuatir akan hari besok, karena hari besok mempunyai kesusahannya sendiri. Kesusahan sehari cukuplah untuk sehari.”",
    "Matius 11:28-29": "“Marilah kepada-Ku, semua yang letih lesu dan berbeban berat, Aku akan memberi kelegaan kepadamu. Pikullah kuk yang Ku pasang dan belajarlah pada-Ku, karena Aku lemah lembut dan rendah hati dan jiwamu akan mendapat ketenangan.”",
    "Matius 14:27": "“Tetapi segera Yesus berkata kepada mereka: 'Tenanglah! Aku ini, jangan takut!'\"",
    "Petrus 4:7": "“Kesudahan segala sesuatu sudah dekat. Karena itu kuasailah dirimu dan jadilah tenang, supaya kamu dapat berdoa.”",
    "Filipi 4:6-7": "“Janganlah hendaknya kamu kuatir tentang apa pun juga, tetapi nyatakanlah dalam segala hal keinginanmu kepada Allah dalam doa dan permohonan dengan ucapan syukur. Damai sejahtera Allah, yang melampaui segala akal, akan memelihara hati dan pikiranmu dalam Kristus Yesus.”"
}

# Menampilkan pertanyaan tentang mood
print("Bagaimana Mood Kamu hari ini?")
print("1. Biasa saja")
print("2. Senang")
print("3. Sedih")
print("4. Marah")

# Meminta input mood dari pengguna
mood_choice = input("Masukkan Nomor sesuai mood Kamu (1/2/3/4): ")

# Memeriksa pilihan mood pengguna dan memberikan respons sesuai
if mood_choice == "1":
    mood = "biasa saja"
elif mood_choice == "2":
    mood = "senang"
elif mood_choice == "3":
    mood = "sedih"
elif mood_choice == "4":
    mood = "marah"
else:
    mood = "tidak valid"

# Menampilkan pertanyaan tentang renungan Alkitab
print("Apakah Kamu perlu renungan hari ini?")
print("1. Ya")
print("2. Tidak")

# Meminta input apakah pengguna membutuhkan renungan Alkitab
renungan_choice = input("Masukkan nomor pilihan Anda (1/2): ")

# Memeriksa apakah pengguna membutuhkan renungan Alkitab
if renungan_choice == "1":
    if mood != "tidak valid":
        # Memilih satu ayat Alkitab secara acak
        random_verse = random.choice(list(renungan_alkitab.keys()))
        print(f"Ini adalah renungan Alkitab untuk hari ini:\n{random_verse}: {renungan_alkitab[random_verse]}")
    else:
        print("Mohon masukkan mood yang valid.")
else:
    print("Terima kasih, semoga harimu menyenangkan!")
