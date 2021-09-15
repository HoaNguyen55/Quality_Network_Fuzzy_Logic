from NguyenLeMinhHoa import quality_network as main
m = main()
while True:
    in_spam_mail = int(input("Số lượng thư rác        [0, 10000]: "))
    if in_spam_mail < 0 or in_spam_mail > 10000:
        print('Giá trị Số lượng spam mail không đúng, vui lòng kiểm tra lại \n')
        continue
    in_mes_delay = float(input("Tỉ lệ độ trễ message    [0, 100]: "))
    if in_mes_delay < 0 or in_mes_delay > 100:
        print('Giá trị Tỉ lệ độ trễ không đúng, vui lòng kiểm tra lại \n')
        continue
    in_spd_network = int(input("Tốc độ mạng thực tế     [1, 100]: "))
    if in_spd_network < 0 or in_spd_network > 100:
        print('Giá trị Tốc độ mạng không đúng, vui lòng kiểm tra lại \n')
        continue
    m.input["Số lượng thư rác"]                 = in_spam_mail
    m.input["Tỉ lệ gói tin bị gián đoạn"]       = in_mes_delay
    m.input["Tốc độ đường truyền tối thiểu"]    = in_spd_network

    m.compute()

    out_result = m.output["Chất lượng của hệ thống mạng"]
    # print(out_result)
    print('|-----------------------------------------------------------------------------------|')
    print(f'| {"Spam Mail(s)":<15} | {"Message Delay (%)":<15} | {"Speed Network (Mbps)":<15} | {"Quality Network":<20} |')
    print('|-----------------|-------------------|----------------------|----------------------|')
    print(f'| {in_spam_mail:<15} | {in_mes_delay:<15}   | {in_spd_network:<15}      | {out_result:<20} |')
    print('|-----------------------------------------------------------------------------------|')
    print("\n\t\tChất lượng hệ thống mạng được đánh giá ở mức độ: %f \n" % out_result)
    quit_mess = input("<<< Nhấn phím bất kỳ để tiếp tục, hoặc nhấn q để thoát >>>\n"
                      "\t Lựa chọn của bạn: ")
    if quit_mess in ["q", "Q"]:
        break
    else:
        pass
