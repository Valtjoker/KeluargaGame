screen pnc_button:


    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_button')])
    # Timer yang variabelnya akan digunakan oleh qte_setup

    vbox:
        xalign x_align yalign y_align spacing 25

        button:
            action Return(1) #jika player mengklik dengan tepat
            xalign 0.5
            yalign 0.25
            xysize 100, 100 #ukuran tombol
            background Animation("#000", 0.5, "#fff", 0.5) #Warna tombol

        button:
            action Return(1) #jika player mengklik dengan tepat
            xalign 0.5
            xysize 100, 100 #ukuran tombol
            background Animation("#000", 0.5, "#fff", 0.5) #Warna tombol
            activate_sound "sounds/hit.mp3" #Suara saat tertekan

        button:
            action Return(1) #jika player mengklik dengan tepat
            xalign 0.5
            yalign 0.5
            xysize 100, 100 #ukuran tombol
            background Animation("#000", 0.5, "#fff", 0.5) #Warna tombol

        button:
            action Return(1) #jika player mengklik dengan tepat
            xalign 0.5
            yalign 0.75
            xysize 100, 100 #ukuran tombol
            background Animation("#000", 0.5, "#fff", 0.5) #Warna tombol

        button:
            action Return(1) #jika player mengklik dengan tepat
            xalign 0.5
            yalign 1
            xysize 100, 100 #ukuran tombol
            background Animation("#000", 0.5, "#fff", 0.5) #Warna tombol
