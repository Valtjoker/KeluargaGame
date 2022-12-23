screen qte_button:
    #button press qte

    button:
        action Return(0)   
        align 0.5, 0.5
        background "images/transparent.png" #background sebagai sensor klik diluar item



    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_button')])
    # Timer yang variabelnya akan digunakan oleh qte_setup

    vbox:
        xalign x_align yalign y_align spacing 25

        button:
            action Return(1) #jika player mengklik dengan tepat
            xalign 0.5
            xysize 100, 100 #ukuran tombol
            background Animation("#000", 0.5, "#fff", 0.5) #Warna tombol
            activate_sound "sounds/hit.mp3" #Suara saat tertekan


        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00" #merubah bar saat waktu tinggal sedikit
