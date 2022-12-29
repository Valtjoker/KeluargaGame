
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Ruth")
define k = Character("Nathan")
define i = Character("Rachel")
define a = Character("Anton")
define ke = Character ("Kevin")
define n = Character("Narrator")

default rachelgood = False
default nathangood = False
default antongood = False
default ruthgood = False

default surfsuccess = False
default mapsuccess = False
default escapesuccess = False

default qtecount = 1
default qtepoint= 0

transform fullsize:
        size (1920,1080)
        on show:
            yalign 0.5 xalign 0.5

image rrumah = "dragon_afro.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene rumah

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    n "Di suatu hari yang cerah, hiduplah satu keluarga kecil."

    n "keluarga itu terdiri dari 4 orang yaitu ayah, ibu dan kedua anaknya."

    show anton happy

    n "Anton merupakan kepala rumah tangga dari keluarga tersebut."

    n "Ayah berumur 49 tahun ini memiliki kepribadan yang rajin dan juga memiliki semangat yang tinggi untuk menafkahi keluarganya."

    n "Akan tetapi,"

    n "Anton memiliki sifat buruk yang selalu ada disaat ia mengerjakan sesuatu"

    n "Sifat buruk itu adalah..."

    n "T E L E D O R."

    n "Sifat buruk ini juga menurun ke salah satu anaknya."

    n "terlepas dari itu, sifat teledornya dengan mudah tertutupi oleh sifat baik yang dimiliki Anton"

    hide anton happy

    show rachel happy

    n "Rachel, sang ibu, pengayom dan penyayang keluarganya."

    n "Sama seperti suaminya, Rachel juga memiliki semangat yang tinggi untuk membahagiakan keluarganya."

    n "Meskipun sudah menginjak usia 50 tahun, Rachel masih memiliki tekad yang kuat dalam beraktivitas sehari-hari."

    n "Rachel cenderung lebih mengutamakan orang lain dibanding dirinya."

    n "Dari sifat tersebut, Rachel selalu memaksa dirinya untuk selalu kelihatan tangguh."

    n "Hal tersebut dilakukan agar tidak mengkhawatirkan keluarganya."

    hide rachel happy

    show nathan happy

    n "Nathan, anak pertama dari Anton dan Rachel."

    n "Ia memiliki minat dalam dunia otomotif serta bakat dalam memperbaiki kendaraan seperti motor dan mobil di umur 21 tahun."

    n "Dibalik minat dan bakatnya, Nathan merupakan orang yang teledor seperti ayahnya."

    n "Terlebih lagi saat dia lelah."

    n "Nathan cenderung melupakan hal yang sangat penting saat dia lelah."

    hide nathan happy

    show ruth happy

    n "Ruth merupakan anak bungsu di keluarga tersebut."

    n "Anak berumur 18 tahun ini memiliki semangat dan ambisi yang tinggi untuk meraih prestasi di sekolahnya."

    n "Ruth selalu mengerjakan tugas dan belajar untuk ujian agar memperoleh nilai tinggi."

    n "Tetapi karena ambisinya itu juga, ruth sering melakukan begadang yang merusak jam tidurnya."

    hide ruth happy

    n "Keluarga kecil tersebut akan bertamasya ke pulau bali."

    n "Hari ini merupakan 1 hari sebelum mereka berangkat ke bali."


    scene kamar ruth

    show Ruth ngantuk

    r "Hoaaammm...."

    r "Sekarang jam berapa ya...?"

    scene jam

    r "Whoa masih jam 6"

    r "Mau balik tidur lagi deh."

    scene kamar ruth

    show ruth ngantuk

    scene merem

    with fade

    r "Hmmmmmmm..."

    r "Susah banget balik tidur.."

    scene kamar ruth

    show ruth ngantuk

    with fade

    r "Ambil minum dulu dibawah kali ya..."

    scene ruang makan

    show ruth ngantuk

    n "Saat hendak mengambil minum, ruth melihat ibunya sedang memasak di pagi hari."

    scene dapur

    show ibu serius

    i "hm.."

    i "Oh... pakai bumbu ini..."

    i "Nanti direbus..."

    scene ruang makan

    label cookingstart:

    show ruth bingung

    with fade

    menu:

        "Membantu ibu memasak." :
            scene dapur
            show rachel kesusahan
            show ruth happy at right with moveinright
            r "Ibu! sini aku bantu masaknya!"
            hide rachel kesusahan
            show rachel happy
            i "Ruth, udah nggak apa-apa."
            i "Ibu bisa sendiri kok!"
            r "Gapapa kok, aku juga mau belajar masak hehehe"
            hide ruth happy
            hide rachel happy
            scene masakan
            with fade
            i "Kali ini kamu buat nasi goreng seafood ya.."
            r "He? nasi goreng bu?"
            show resepNG
            i "Ini resepnya, diingat baik-baik"
            hide resepNG
            r "Okay... Pertama aku harus.."
            menu:
                "Potong margarin":
                    r "Ini kali ya..."
                    i "Ruth.. bukan begitu... itu nggak ada di resep tadi..."
                    r "He..? tidaaak! maaf bu!"
                    "Masak gagal"
                    jump cookingstart

                "Potong bawang merah beserta sosis dan bakso":
                    r "Ini kali ya..."
                    i "Ruth.. bukan begitu... itu nggak ada di resep tadi..."
                    r "He..? tidaaak! maaf bu!"
                    "Masak gagal"
                    jump cookingstart

                "Potong bawang bombay beserta udang dan cumi":
                    r "Okay, sudah dipotong yang diperlukan..."
                    menu:
                        "Masukkan margarin dan nyalakan api kecil":
                            r "Hmmmm.... okay.. sudah cukup apinya..."
                            menu:
                                "Masukkan nasi, kecap dan garam":
                                    r "Ini dulu ya..."
                                    i "Ruth... bukan itu dulu yang dimasukkan..."
                                    r "Yah... gimana bu...?"
                                    i "Yasudah... ibu saja yang masak sisanya..."
                                    "Masak gagal"
                                    jump cookingstart

                                "Masukkan bawang bombay, udang dan cumi":
                                    r "Okay... waktunya ditumis..."
                                    r "Wah... baunya sudah berasa..."
                                    menu:
                                        "Masukkan nasi, kecap dan garam":
                                            r "Nah masukkin nasi deh..."
                                            i "Hayo.. Ruth... masih ada yang kurang..."
                                            r "Yah ibu...."
                                            i "Ibu bisa masukin sendiri kok.."
                                            "Masak gagal"
                                            jump cookingstart

                                        "Masukkan daun bawang dan telur":
                                            r "Duh jadi laper deh hehe..."
                                            scene dapur
                                            show ruth happy at left
                                            r "Nah, masukin nasi deh!"
                                            show rachel happy
                                            i "Wah, kelihatannya enak ruth..."
                                            i "Jangan lupa ya, ini kecap sama garamnya.."
                                            r "Ohiya bu!"
                                            i "Pintar masak anak ibu!"
                                            r "Hehe aku gitu lho"
                                            $ rachelgood = True

                                "Masukkan udang, cumi dan daun bawang":
                                    r "Ini dulu ya..."
                                    i "Ruth... bukan itu dulu yang dimasukkan..."
                                    r "Yah... gimana bu...?"
                                    i "Yasudah... ibu saja yang masak sisanya..."
                                    "Masak gagal"
                                    jump cookingstart

                        "Masukkan margarin dan nyalakan api sedang":
                            r "Nah.. ini pasti benar"
                            i "Hayo.. Ruth.. coba dilihat lagi resepnya tadi gimana..."
                            r "Begini kok bu!"
                            i "Hmmm yaudah sini ibu aja yang masak mulai sekarang"
                            "Masak gagal"
                            jump cookingstart

                        "Masukkan margarin dan nyalakan api besar":
                            r "Nah.. ini pasti benar"
                            i "Hayo.. Ruth.. coba dilihat lagi resepnya tadi gimana..."
                            r "Begini kok bu!"
                            i "Hmmm yaudah sini ibu aja yang masak mulai sekarang"
                            "Masak gagal"
                            jump cookingstart

        "Mengambil air, lalu membantu ibu memasak sebentar." :
            scene ruang makan
            show ruth ngantuk
            r "Hmmm... nanti dulu deh masih capek.."
            n "Ruth meminum air, kemudian ia hendak membantu ibunya sedikit."
            scene dapur
            show ruth ngantuk at right with moveinright
            show rachel kesusahan
            r "Bu, aku bantu-bantu dikit gapapa ya."
            i "Ah iya gapapa kok."
            i "Ibu udah susah motong-motong sekarang.."
            r "Iya, Aku aja yang motong."


        "Menyapa ibu, mengambil air dan kembali tidur." :
            scene ruang makan
            show ruth happy
            r "Selamat pagi ibu!"
            i "Iya selamat pagi Ruth!"



    scene ruang makan

    n "waktu menunjukkan pukul 8."

    n "Keluarga kecil itu menyantap sarapan yang telah dihidangkan sambil bersenda gurau."

    scene ruang keluarga
    with fade

    show nathan bingung

    k "Hm... apa nanti aku lulus jadi pembalap aja ya.."

    k "Gajinya gede sih.. resikonya tinggi juga.."

    hide nathan bingung

    show nathan sombong

    k "Tapi tetep gajinya gede!"

    i "Nathan."

    hide nathan sombong

    show nathan malu

    k "He... iya bu?!"

    show nathan malu at left with move
    show ibu happy at right with moveinright

    show nathan happy at left

    i "Kamu mulai tata barang-barang kamu dulu.."

    i "Besok kan kita mau berangkat, nanti kalo mepet-mepet, celananya ketinggalan."

    hide ibu happy
    show ibu sombong at right

    hide nathan happy
    show nathan malu at left

    i "Kayak tahun lalu~"

    i "Ibu inget banget kamu turun gunung pakai sarungnya ayah, abis it-"

    k "IYA BU IYAA!"

    hide nathan malu with moveoutleft

    scene kamar nathan

    show nathan serius

    k "Hmm..."

    k "Butuh apa aja ya...?"

    hide nathan serius
    show nathan kesusahan

    k "Duh sakit kepala lagi gara-gara main hp kelamaan.."

    hide nathan kesusahan
    show nathan sombong

    k "Oh iya!"

    k "Hehehehe"

    scene kamar ruth

    show ruth happy

    with fade

    r "Ini loncat kesini.."

    r "Ayo!"

    r "Yes! akhirnya bisa santai-santai setelah sekian lama-"

    hide ruth happy
    show ruth bingung

    k "RUUUUUUTTHHHHHHHHH!"

    show ruth bingung at right with move
    show nathan happy at left with moveinleft

    r "Apa- apa- kenapa?!"

    k "Ruth, bantuin aku beres-beres yaaaa"

    hide ruth bingung
    show ruth marah at right


    r "Iiiih kakak lagian gak beres-beres dari kemarin disuruh ibu!"

    hide nathan happy
    show nathan sedih at left
    k "Ya kan kakak kuliah..."

    k "Banyak tugas..."

    k "Trus kegiatan juga banyak..."

    k "Bantuin ya..."

    menu:

        "Meninggalkan game dan langsung menolong kakak dalam menyusun perlengkapan barang." :
            hide ruth bingung
            show ruth happy at right
            r "Ayo kak kita susun sekarang!"
            hide nathan sedih
            show nathan happy at left
            k "Yeeeeyyy ayooo!"
            scene kamar nathan
            show ruth serius at right
            show nathan happy at left
            r "Oh... okeokee bisa kok ini!"
            k "Makasih banget ya adekku yang cantik~"
            scene kamar nathan
            show ruth serius at right
            show nathan happy at left
            r "Kak jangan lupa lho ini inhaler."
            hide nathan happy
            show nathan malu at left
            k "Ohiya hehe aku lupa..."
            $ nathangood = True


        "Menolong kakak setelah selesai bermain game." :
            hide ruth bingung
            show ruth serius at right
            r "Kakak duluan aja nanti aku nyusul."
            hide nathan sedih
            show nathan happy at left
            k "Oh iyaa? okee aku tunggu yaaaa!"
            hide nathan happy with moveoutleft
            scene kamar ruth
            "*10 menit berlalu*"
            show ruth happy
            r "Oke waktunya bantu kakak."
            scene kamar nathan
            show nathan kesusahan at left
            show ruth happy at right with moveinright
            r "Ayo kak sini aku bantuin!"
            hide nathan kesusahan
            show nathan happy at left
            k "Akhirnya dateng juga!"

        "Lanjut bermain game dan membiarkan kakak menyusun perlengkapan sendiri." :
            hide ruth bingung
            show ruth marah at right

            r "Kakak Beresin sendiri aja ihhhhh"
            r "Aku lagi santai-santai ini udah lama gak main game!"
            k "Hmmm yaudah deh..."

    n "Kemudian barang-barang Nathan berhasil tersusun."

    scene kamar nathan

    n "Langit yang berwarna jingga menunjukkan sore hari."

    show nathan ngantuk

    n "Nathan hendak tidur setelah menyusun barang-barangnya untuk berpergian besok."

    "*KRINGGGGG*"

    k "Hm.?"

    "*KRINGGGGGG*"

    k "Halo?"

    a "Kakak."

    k "Ah iya kenapa yah?"

    a "Bisa tolong bantu ayah?"

    hide nathan ngantuk
    show nathan bingung

    a "Jadi mobil lagi rusak..."

    a "Besok kan mau dibawa buat jalan-jalan."

    a "Bisa tolong bantu ayah merbaikin nggak?"

    menu:
        "Bergegas menolong ayah." :
            k "Oke ayah.. aku ke garasi ya!"
            scene garasi
            show anton happy
            show nathan happy at right with moveinright
            k "Ayoo ayah! kita perbaikin bareng-bareng!"
            a "Oke nak, Makasih banyak ya!"
            $ qtepoint = 10
            jump qte
            label goodqte:
            $ antongood = True

        "Berbaring sebentar untuk mengumpulkan nyawa, baru menolong ayah" :
            k "Sebentar ya ayah... aku tiduran dulu..."
            a "Baik nak, ayah di garasi ya nanti."
            "*20 menit berlalu*"
            scene garasi
            show ayah kesusahan
            show nathan serius at right with moveinright
            k "Yang kurang dimana ayah?"
            a "Oh ini tinggal bagian bawah mesin aja.."
            k "Oke sini aku bantu."
            $ qtepoint = 5
            jump qte
            label badqte:

        "Kembali tidur karena masih mengantuk." :
            k "Aku masih capek yah.. gabisa fokus nanti..."
            a "Ooh oke deh nak, maaf ya ganggu tidurnya..."

    scene kamar nathan

    n "Setelah mobil sudah diperbaiki, tidak terasa hari sudah menuju malam."

    n "Sudah saatnya keluarga kecil itu untuk beristirahat."

    n "Akan tetapi..."

    show nathan happy

    k "Eh nanti aja diomongin di kampus biar semua pada ngumpul"

    k "Gaenak kalo disini masi-"

    hide nathan happy
    show nathan bingung

    r "TIDAAAAAAAKKKKK!!"

    k "Duh kenapa si Ruth teriak-teriak, udah malem juga"

    scene kamar ruth

    show ruth kesusahan

    show nathan bingung at left with moveinleft

    k "Kamu kenapa teriak-teriak sih udah malem juga."

    k "untung bukan ayah yang kesini."

    r "Duhh kakkkkkk!"

    r "Aku lupa hari ini ujian online..."

    r "Mana susah banget lagi ini.."
    label homeworkhelp:
    menu:

        "Inisiatif membantu adiknya dan berhenti mengobrol dengan teman online" :
            hide nathan bingung
            show nathan serius at left
            k "Oke sini kakak bantuin kamu"
            hide ruth kesusahan
            show ruth happy
            r "WIIII BENERAN YA KAK?!"
            k "Iyaa"
            $ hangmanGame("asean","asosiasi negara asia tenggara", 1)
            $ hangmanGame("manila","ibukota filipina", 1)
            $ hangmanGame("vietnam","Negeri naga biru", 1)
            $ hangmanGame("brunei","Letak istana negara terbesar di dunia", 1)
            $ hangmanGame("indonesia","Negara terbesar di asean", 1)
            scene kamar ruth
            show nathan serius at left
            show ruth serius
            k "Terus jawab yang ini... selesai!"
            hide ruth serius
            show ruth happy
            r "YEEEEYYY SELESAIII!"
            r "Makasih banyak kakkk! hihihi"
            r "Nanti aku traktir deh di balii~"
            hide nathan serius
            show nathan happy at left
            k "Bener ya? hehehe"
            $ ruthgood = True

        "Membantunya nanti karena masih mengobrol dengan teman online." :
            hide nathan bingung
            show nathan serius at left
            k "Yaudah aku bantu, tapi nanti aku mau ngobrol sebentar."
            r "Ah iya kak?!"
            k "Iya tapi kamu kerjain sendiri dulu sebentar"
            hide nathan serius with moveoutleft
            r "Iya iya.. makasih ya kak!"
            "*30 menit telah berlalu*"
            scene kamar ruth
            show ruth kesusahan at right
            show nathan sombong at left with moveinleft
            k "Sini sini sini aku bantu."
            hide ruth kesusahan
            show ruth happy
            r "Yeaaayyy!"
            $ hangmanGame("bintang","Lambang sila pertama pancasila", 1)
            $ hangmanGame("yogyakarta","Ibukota Indonesia tahun 1949", 1)
            $ hangmanGame("habibie","Presiden ke-3 indonesia", 1)
            $ hangmanGame("kalimantan","pulau terbesar ke-2 di indonesia", 1)
            $ hangmanGame("borobudur","candi terbesar di indonesia", 1)



        "Kembali mengobrol dengan teman." :
            hide nathan bingung
            show nathan serius at left
            k "Yaudah jangan berisik ya aku lagi sama temen-temen."
            hide ruth kesusahan
            show ruth sedih
            r "Iya... maaf ya kak..."


    scene rumah
    n "Saatnya keluarga kecil itu hendak berangkat di hari yang cerah ini."

    n "Semua sudah disiapkan satu persatu untuk berlibur di pulau bali nanti."

    #################ENDING FOR CH 1#################

    label ending:
    if rachelgood == True and nathangood == True and antongood == True and ruthgood == True:
        jump goodend
    elif rachelgood == False:
        jump rachelbad
    elif nathangood == False:
        jump nathanbad
    elif antongood == False:
        jump antonbad
    elif ruthgood == False:
        jump ruthbad


    label goodend:
    scene mobil
    n "Keluarga kecil itupun hendak berangkat ke dermaga agar bisa ke Bali."
    scene goodend
    "*KRINGGGGG*"
    show anton bingung at center
    a "Huh? siapa ini?"
    Character("???") "Halo, apakah ini dengan bapak Anton?"
    a "Iya, dengan saya sendiri.. ini siapa ya?"
    Character("Rudy?") "Perkenalkan, nama saya Rudy. saya ingin menginformasikan bahwa perjalanan anda ke Bali akan dialokasikan ke pulau Kala!"
    a "Pulau.. apa?"
    Character("Rudy?") "Pulau Kala pak!"
    a "Maaf, saya tidak pernah mendengar adanya pulau Kala."
    show ruth happy at right
    show nathan happy at left
    Character("Ruth dan Nathan") "APA?! PULAU KALA?! KITA MAU KE PULAU KALAAA!"
    hide ruth happy
    hide nathan happy
    hide anton bingung
    scene pulau
    n "Pulau Kala merupakan sebuah pulau kecil yang baru ditemukan 2 tahun yang lalu dan tiba-tiba menjadi destinasi liburan turis nasional maupun turis internasional"
    n "Pulau Kala terkenal dengan pantainya dengan ombak yang cocok untuk berselancar, hutannya yang sejuk, beserta warga lokalnya yang ramah."
    n "Tidak jauh dari pantainya, di dalam hutan, terdapat sebuah hotel bintang 5 bernama Kala Resort yang juga merupakan satu-satunya hotel di Pulau Kala."
    n "Keluarga kecil itupun berangkat menuju dermaga untuk ke pulau Kala."
    scene mobil
    show anton happy
    a "Baik, pak Rudy, akan saya terima tawaranya."
    hide anton happy
    show ruth happy at right
    show nathan happy at left
    Character("Ruth dan Nathan") "YAAAAYYYYYYY!"
    hide ruth happy
    hide nathan happy
    scene mobil
    n "Keluarga kecil itu beranjak ke dermaga menuju destinasi liburan barunya yaitu pulau kala"
    "BERSAMBUNG..."
    scene blackscreen
    with fade
    ################CHAPTER 2#################
    scene hotel
    n "2 hari berlalu di pulau Kala..."
    show nathan happy at left
    k "Ibu! aku pergi berselancar lagi ya!"
    show ibu happy at right
    i "Iya nak, hati-hati ya.."
    i "Ohiya, Ruth!"
    show ruth ngantuk
    r "Iya bu..?"
    i "Ibu minta tolong temani kakakmu berjalan ke pantai ya"
    r "Ibuuuuuuu! tapi aku baru mau-"
    i "Ruth.. kakak kamu kasian nanti kalo kesasar... dibantu ya.."
    r "Iya iya.. aku siap-siap dulu ya.."
    hide nathan happy
    show nathan sombong at left
    k "Cepet yaa! hehe"
    hide nathan sombong
    hide ibu happy
    hide ruth ngantuk
    scene ombak
    with fade
    show nathan happy
    k "YEAAAAAAAAHHHHHH"
    hide nathan happy
    scene pantai
    show ruth ngantuk
    r "Hmmmm.... males banget nungguin kakak kalo selancar lama...."
    r "Mana lagi panas banget..."
    r "Lagian aneh... udah 2 hari masih nggak hafal jalan ke pantai..."
    r "Sama aja ayah sama kakak..."
    show kevin happy at right
    Character("???") "Hai"
    hide ruth ngantuk
    show ruth bingung
    r "Eh? aku?.. Oh iya, kenapa??"
    Character("???") "Boleh duduk disini?"
    hide ruth bingung
    show ruth happy
    r "Oh? boleh silahkan!"
    ke "Ah.. maaf aku kelihatan tidak sopan"
    ke "namaku Kevin aku warga asli pulau kala."
    r "Ohhh haii Kevin, namaku Ruth"
    ke "Kamu pasti turis dalam negeri"
    r "Hahaha kamu tau dari mana?"
    ke "Aku belum pernah melihat wajahmu di pulau ini"
    r "*Ganteng bangetttt*"
    ke "Ohiya, kamu sedang apa disini, hanya sendirian di bawah pohon"
    r "Aku menunggu kakakku sedang berselancar... Dia nggak bisa sendiri jalan dari hotel ke sini"
    ke "Menunggu saja ya.. hmmm sepertinya membosankan"
    ke "Kalau begitu, apa kamu mau jalan bersamaku ke karnaval yang baru buka di pulau kala?"
    r "Oh? ada karnaval? aku mau!"
    ke "Ayo sini, letaknya tidak jauh dari pantai"
    hide kevin happy
    hide ruth happy
    scene ombak
    k "WOHOOOOOO"
    k "Eh, sepertinya Ruth mempunyai teman baru disitu"
    k "eh-eh-EHHHHH untung nggak jatuh... aku harus menjaga keseimbanganku dulu..."
    $ qtecount = 1
    $ qtepoint = 20
    jump qtech2

    if surfsuccess:
        jump safesurf
    else:
        jump drowned

    label safesurf:
        k "YEAAAAAHHHH"
        scene pantai
        with fade
        n "Hari semakin sore, saat ini, Nathan baru saja selesai berselancar"
        show nathan happy
        k "Berselancar pokoknya hal paling seru deh disini, jadi pengen terus!"
        hide nathan happy
        show nathan bingung
        k "Ohiya"
        k "Ruth daritadi dimana ya... belum kembali..."
        k "Sepertinya aku harus jalan kearah tempat dia terakhir jalan tadi..."


    label drowned:
        k "EH EHHHHH AAAAAAAAAAAA!"
        scene pantai
        with fade
        n "Nathan tenggelam ditengah-tengah ia berselancar."
        n "Ia diselamatkan oleh penjaga pantai dan kemudian dibawa ke pos terdekat."

    scene hotel with fade
    show rachel bingung
    i "Aduh... Dimana ya anak-anak yah?"
    show anton serius at right
    a "Iya... semakin sore lagi ya..."
    hide rachel bingung
    show rachel sedih
    i "Mereka juga nggak bisa ditelfon...."
    a "Ayah jalan ke mereka aja ya, ibu jaga diri sebentar disini."
    i "Kamu yakin mau ke mereka? Nanti kalo kamu nyasar gimana?"
    hide anton serius
    show anton happy at right
    a "Tenang saja, ada gulge maps!"
    a "Nanti ayah juga berkabar kalo udah ketemu"
    i "Jangan nyasar ya..."
    a "Tenang, ayah tidak akan nyasar!"
    a "Ayah berangkat dulu ya!"
    i "Hati-hati..."
    hide anton happy
    hide rachel sedih
    scene hutan
    with fade
    show anton serius
    a "Hmm kayaknya petanya aneh..."
    a "Disini aku belum jalan dari tempat awal masuk hutan...."
    a "Padahal kan aku udah jalan lumayan Lama"
    "*DRINGGGGGGGGGGGG*"
    a "Apa itu?"
    show arahan at right
    hide anton serius
    show anton bingung
    #KIRI, KANAN, LURUS, KANAN, LURUS
    a "Panah-panah?"
    "JANGAN."
    "SAMPAI."
    "SALAH."
    "TERUS."
    "LIHAT."
    "DEPAN."
    a "Suara apa itu?!"
    "JANGAN."
    "LIHAT."
    "BELAKANG."
    hide arahan
    a "Okay.... ini mulai aneh"
    a "Tapi sepertinya arahan ini akan berguna untuk menyusuri hutan ini"
    a "Hm... oke... pertama-tama menurut arahannya ke.."
    menu:
        "kiri":
            a "Okay..."
            a "Hmm.. kalo ini ke...."
            menu:
                "kiri":
                    a "Kalau tidak salah kesini..."
                    a "Eh? jalan buntu?"
                    hide anton bingung
                    "Sepertinya kau salah arah....."
                    a "Siapa disitu?!"
                    show siluet
                    "Akan ku arahkan kau ke jalan keluarnya..."

                "lurus":
                    a "Kalau tidak salah kesini..."
                    a "Eh? jalan buntu?"
                    hide anton bingung
                    "Sepertinya kau salah arah....."
                    a "Siapa disitu?!"
                    show siluet
                    "Akan ku arahkan kau ke jalan keluarnya..."

                "kanan":
                    a "Ini..."
                    a "Kalau tidak salah tadi ke..."
                    menu:
                        "kiri":
                            a "Kalau tidak salah kesini..."
                            a "Eh? jalan buntu?"
                            hide anton bingung
                            "Sepertinya kau salah arah....."
                            a "Siapa disitu?!"
                            show siluet
                            "Akan ku arahkan kau ke jalan keluarnya..."
                        "lurus":
                            a "okay... cukup panjang ya jalannya..."
                            a "Yang ini ke...."
                            menu:
                                "kiri":
                                    a "Kalau tidak salah kesini..."
                                    a "Eh? jalan buntu?"
                                    hide anton bingung
                                    "Sepertinya kau salah arah....."
                                    a "Siapa disitu?!"
                                    show siluet
                                    "Akan ku arahkan kau ke jalan keluarnya..."
                                "lurus":
                                    a "Kalau tidak salah kesini..."
                                    a "Eh? jalan buntu?"
                                    hide anton bingung
                                    "Sepertinya kau salah arah....."
                                    a "Siapa disitu?!"
                                    show siluet
                                    "Akan ku arahkan kau ke jalan keluarnya..."
                                "kanan":
                                    a "Sepertinya aku semakin dekat..."
                                    a "Nah yang ini ke..."
                                    menu:
                                        "kiri":
                                            a "Kalau tidak salah kesini..."
                                            a "Eh? jalan buntu?"
                                            hide anton bingung
                                            "Sepertinya kau salah arah....."
                                            a "Siapa disitu?!"
                                            show siluet
                                            "Akan ku arahkan kau ke jalan keluarnya..."
                                        "lurus":
                                            hide anton bingung
                                            show anton happy
                                            a "Oh kelihatan jalan keluarnya!"
                                            hide anton happy
                                            scene pantai
                                            with fade
                                            show anton bingung
                                            a "Hmm.... aneh..."
                                            a "Aku tidak bisa melihat Nathan dan Ruth.."
                                            a "Dan pantainya terlihat sepi.."
                                            hide anton bingung
                                            show anton serius
                                            a "RUTH! NATHAN!"
                                            hide anton serius
                                            show anton bingung
                                            a "Dimana mereka ya..."
                                            show siluet at right
                                            a "Maaf pak, apakah bapak pernah melihat 2 orang ini di pantai?"
                                            "Hmmm...?"
                                        "kanan":
                                            a "Kalau tidak salah kesini..."
                                            a "Eh? jalan buntu?"
                                            hide anton bingung
                                            "Sepertinya kau salah arah....."
                                            a "Siapa disitu?!"
                                            show siluet at right
                                            "Akan ku arahkan kau ke jalan keluarnya..."
                                            hide siluet
                                            hide anton bingung
                        "kanan":
                            a "Kalau tidak salah kesini..."
                            a "Eh? jalan buntu?"
                            hide anton bingung
                            "Sepertinya kau salah arah....."
                            a "Siapa disitu?!"
                            show siluet
                            "Akan ku arahkan kau ke jalan keluarnya..."
        "lurus":
            a "Kalau tidak salah kesini..."
            a "Eh? jalan buntu?"
            hide anton bingung
            "Sepertinya kau salah arah....."
            a "Siapa disitu?!"
            show siluet
            "Akan ku arahkan kau ke jalan keluarnya..."

        "kanan":
            a "Kalau tidak salah kesini..."
            a "Eh? jalan buntu?"
            hide anton bingung
            "Sepertinya kau salah arah....."
            a "Siapa disitu?!"
            show siluet
            "Akan ku arahkan kau ke jalan keluarnya..."

    scene karnaval
    with fade
    show ruth happy
    show kevin happy at right
    r "Ohiya aku harus kembali ke pantai"
    ke "Sebentar dulu! kita belum masuk ke rumah hantu"
    r "He? ada rumah hantu?"
    ke "Wah kamu harus coba deh"
    r "Sebentar aja gapapa yaa"
    hide ruth happy
    hide kevin happy
    scene rumah hantu
    with fade
    show ruth sedih
    show kevin happy
    r "Kamu yakin kesini jalannya..."
    ke "Tenang aja aku deket kamu kok"
    r "Takut...."
    ke "Kamu lurus terus.. abis itu turun ke tangga, masuk ke lubang di sampingnya"
    ke "Disitu ada pintu rahasia"
    r "Oke... tapi kamu ikut aku ya"
    ke "Tenang aja..."
    hide kevin happy
    n "Ruth mengikuti arahan Kevin, disitu ia masuk ke ruangan yang sangat gelap, tidak melihat jalan masuk maupun keluar."
    scene blackscreen
    r "Kev? Kevin?!"
    r "Duh... ini kemana..."
    "APA YANG KAMU TAU TENTANG KELUARGA"
    r "HIII?!"
    "KAMU HARUS MENJAWAB PERTANYAAN INI ATAU KAMU TIDAK AKAN BISA KELUAR..."
    r "M-menjawab apa..?"
    hide ruth sedih
    $ hangmanGame("rachel","Nama Ibu", 2)
    $ hangmanGame("anton","Nama Ayah", 2)
    $ hangmanGame("nathan","Nama Kakak", 2)
    $ hangmanGame("ruth","Nama Adik", 2)
    label trapped:
        r "Oh aku menemukan jalan keluar!"
        r "He..? INI DIMANA?!"
    label free:
        scene tunnelOut
        r "Ada cahaya!"
    scene hotel
    with fade
    show rachel sedih
    i "Aduh... tadi anak-anakku... sekarang suamiku masih belum kunjung pulang..."
    i "Mereka kemana ya..."
    "*TokTok*"
    hide rachel sedih
    show rachel bingung
    i "Yaaa? siapa ya?"
    Character("???") "Ibu...? bisa tolong bukakan pintunya.."
    i "Ruth? itu kamu?"
    Character("Ruth?") "Ibu... Tolong bukakan pintunya.."
    i "Iya nak, akan ibu bukakan"
    i "*Tunggu... bukannya Ruth punya kunci kamar..?*"
    i "*Mungkin ketinggalan...*"
    hide rachel bingung
    scene pintu
    Character("Ruth?") "Ibu... Aku masih tidak bisa membuka pintunya..."
    i "Iya nak sebentar akan aku bukakan pintunya..."
    "*KLIK*"
    "Terimakasih banyak bu..."
    "BERSAMBUNG...."
    return

#################BAD ENDINGS#################
    label rachelbad:
        scene rachel bad
    n "Rachel terbaring sakit karena demam."

    n "Hal ini disebabkan oleh Rachel yang memaksakan dirinya untuk memasak di pagi buta."

    show rachel sedih at left
    i "Maafin ibu ya nak.. jadinya liburan kita diundur..."
    show ruth sedih at center
    show nathan sedih at right

    k "Udah bu gapapa... bukan salah ibu juga.."

    r "Iya bu.. maafin ruth ya... harusnya aku bantu ibu kemarin..."

    hide rachel sedih
    hide ruth sedih
    hide nathan sedih
    show anton sedih

    a "Udah nak.. kita masih bisa pergi, tapi diundur aja."

    scene blackscreen
    "BAD END."

    return

    label nathanbad:
        scene mobil jalan

        n "Keluarga kecil itu di tengah jalan ke dermaga untuk menaiki kapal feri ke bali."

        n "namun di tengah perjalanan..."

        scene nathan bad
        show nathan kesusahan
        k "*uhuk**uhuk*"
        k "*uhuk**uhuk**uhuk**uhuk*"
        k "*uhuk**uhuk**uhuk*"
        show ruth bingung at right
        r "Kakak kenapa kak"
        k "*uhuk**uhuk*"
        show rachel bingung at left
        i "Ruth tolong ambilkan inhaler kakak ada di tasnya."
        r "Gaada bu!"
        k "*uhuk**uhuk**uhuk**uhuk*"
        hide ruth bingung
        show ruth sedih at right
        r "Aduuuhhhh gimana ini"
        i "Ayah kita cari apotek dulu ya."
        k "*uhuk**uhuk**uhuk**uhuk*"
        hide nathan kesusahan
        show anton sedih
        a "Hm.. gaada yang deket kalo disini apoteknya..."
        a "Terpaksa kita harus pulang dulu.."
        a "Kita tunda dulu aja perginya... biarkan nathan istirahat dulu."
        scene blackscreen
        "BAD END"
        return
    label antonbad:

        scene mobil
        n "Keluarga kecil itu siap berangkat ke dermaga menggunakan mobil."

        n "Namun, Anton merasakan ada hal yang aneh saat ia membawa mobil itu."

        "*krkrkrkrk*"

        show anton bingung

        a "hm?"

        hide anton bingung

        "*BRRR KRKRKRK BRRRRK*"

        "*CSSSSSSS*"

        show rachel bingung at left

        i "Ayah, kenapa mobilnya?"

        show anton bingung

        a "Aduhhh"

        show nathan sedih at right

        k "Yah mogok ya...."

        a "Ah... iya mogok..."

        show anton serius

        hide anton bingung

        a "Coba ayah liat dulu."

        show nathan serius at right

        k "Aku ikut ayah."

        scene anton bad

        show anton sedih
        show nathan sedih at left

        k "Yah.... ini harus dibawa ke bengkel..."

        a "Iya... ayah juga gabawa perlengkapan buat merbaikin disini..."

        a "Yaudah deh nak gapapa, kita cari bengkel dulu aja."

        a "Sementara kita tunda aja dulu liburannya."

        a "Masih ada hari lain kok."
        scene blackscreen
        "BAD END"
        return


    label ruthbad:

        scene kamar ruth
        show ruth kesusahan
        r "Aduh... masih belom selesai ujiannya..."
        a "Ruth! ayo turun! kita mau jalan lho!"
        scene ruth bad
        r "Ayah maaf, aku gabisa ikut deh kayaknya...."
        a "Lah kenapa?"
        r "Aku masih harus ngejar ujianku..."
        r "Ruth jaga rumah aja gapapa ya.."
        r "Soalnya beneran harus selesai ini..."
        a "Yaudah, kita perginya ke rumah sodara aja besok.."
        a "Biar semua bisa pergi bareng-bareng."
        scene blackscreen
        "BAD END"
        return

    ########MINIGAME#########

        label qte:
            scene mesin at fullsize

    $ cont = 0 #variabel continue

    call qte_setup(1.0, 1.0, 0.01, renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
    # Memanggil Fungsi qte_setup

    while cont == 1 and qtecount < qtepoint: # Fungsi pengulangan
        call qte_setup(1.0, 1.0, 0.01, renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
        $ qtecount += 1 #increment

    if qtecount == 10 and qtepoint == 10: #Jika mencapai 10 ronde
        "COMPLETED"
        jump goodqte

    elif qtecount == 5 and qtepoint == 5: #Jika mencapai 5 ronde
        "COMPLETED"
        jump badqte

    else:   #jika player salah klik/waktu habis
        play sound "sounds/miss.mp3"
        "{b}GAME OVER{/b}"
        $ qtecount = 1
        jump qte

label qtech2:
        scene ombak at fullsize
$ cont = 0 #variabel continue

call qte_setup(1.0, 1.0, 0.01, renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
# Memanggil Fungsi qte_setup

while cont == 1 and qtecount < qtepoint: # Fungsi pengulangan
    call qte_setup(1.0, 1.0, 0.01, renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
    $ qtecount += 1 #increment

if qtecount == 20 and qtepoint == 20: #Jika mencapai 10 ronde
    "COMPLETED"
    jump safesurf

else:   #jika player salah klik/waktu habis
    play sound "sounds/miss.mp3"
    "{b}GAME OVER{/b}"
    $ qtecount = 1
    jump drowned

label qte_setup(time_start, time_max, interval, x_align, y_align):  #fungsi game QTE

    $ time_start = time_start   #Waktu
    $ time_max = time_max       #waktu max
    $ interval = interval       #Jarak pengurangan waktu
    $ x_align = x_align         #koordinat lokasi X
    $ y_align = y_align         #Koordinat lokasi Y

    call screen qte_button #memanggil qte_button di qte.rpy

    $ cont = _return # return 1 jika tombol tertekan dengan tepat waktu dan 0 jika tidak





init python:
    #first we define our images of hangman 0 - 4 (5 images) (take out the comments when you put your own images in )
    #    for i in range(5):
    #        #images are named slide0.png...slide9.png
    #        renpy.image('hangman%d' % i, 'hangman%d.png' % i)

        def hangmanGame( word, hint, chapter ):        #membuat fungsi hangman
            hintword = hint                   #hint
            finishedWord = word               #kata yang ingin dimasukkan
            finishedWord = finishedWord.upper() #.upper membuat string menjadi uppercase
            lettersUsed = ""
            i = 0
            myString = ""
            while (i < len(finishedWord)):  #Fungsi pengulangan simbol * agar setara dengan panjang kata
                myString += "*"
                i+=1
            lettersUsed = ""

            while(finishedWord != myString) :
                ui.text("Jawaban:" + myString + " \nkata yang terpakai: " + lettersUsed + "\n Sisa tebakan:" +str(5 - len(lettersUsed)) + " \nHint: " + hintword )
                newLetter = renpy.input("Kata apa yang menurutmu tepat?", "", length=1)
                newLetter = newLetter.upper()
                foundSomething = False;
                i = 0
                while( i < len(finishedWord)) :
                    if(finishedWord[i] == newLetter[0]):
                        myString = myString[0:i] + newLetter[0]+ myString[i+1:]
                        foundSomething = True
                    i+=1
                if(foundSomething == False):
                    lettersUsed += newLetter[0]
                    # This is where I would show a new graphic if I had graphic files to show
                    # renpy.show('hangman%d' % len(lettersUsed))
                    if(len(lettersUsed) >= 5 and chapter == 1):
                        renpy.jump('homeworkhelp')
                    elif(len(lettersUsed) >= 5 and chapter == 2):
                        renpy.jump('trapped')







    # This ends the game.
            return
