import NguyenLeMinhHoa as main_module
# Test app:
import random
in_mes_delay_v = []
in_spd_network_v = []
in_spam_mail_val = random.sample(range(0, 10001), 1000)
for i in range(len(in_spam_mail_val)):
    in_mes_delay_val = round(random.uniform(0, 100))
    in_mes_delay_v.append(in_mes_delay_val)
    in_spd_network_val = round(random.uniform(1, 100))
    in_spd_network_v.append(in_spd_network_val)

my_test = open("my_test.txt", "w", encoding='utf-8')
my_test.writelines('|-----------------------------------------------------------------------------------|')
my_test.writelines('\n')
my_test.writelines(f'| {"Spam Mail(s)":<15} | {"Message Delay (%)":<15} | {"Speed Network (Mbps)":<15} | {"Quality Network":<20} |')
my_test.writelines('\n')
my_test.writelines('|-----------------|-------------------|----------------------|----------------------|')
my_test.writelines('\n')
good_state = 0
bad_state = 0
normal_state = 0
too_bad_state = 0
for i in range(len(in_spam_mail_val)):

    in_spam_mail = in_spam_mail_val[i]
    in_mes_delay = in_mes_delay_v[i]
    in_spd_network = in_spd_network_v[i]

    main_module.model.input["Số lượng thư rác"]                 = in_spam_mail
    main_module.model.input["Tỉ lệ gói tin bị gián đoạn"]       = in_mes_delay
    main_module.model.input["Tốc độ đường truyền tối thiểu"]    = in_spd_network
    a = '| {:<15} | {:<15}   | {:<15}      |' .format(in_spam_mail, in_mes_delay, in_spd_network)
    my_test.writelines(a)
    main_module.model.compute()
    out_result = main_module.model.output["Chất lượng của hệ thống mạng"]
    # quality_rate = {"Tốt": [8, 9, 10, 11],
    #                 "Bình Thường": [5, 6, 7, 8],
    #                 "Tệ": [2, 4, 5],
    #                 "Quá Yếu": [0, 1, 2]}
    if 10 >= out_result >= 8:
        mes_show = ' ==> Good'
        good_state += 1
    elif 8 > out_result >= 5:
        mes_show = ' ==> Normal'
        normal_state += 1
    elif 5 > out_result >= 2:
        mes_show = ' ==> Bad'
        bad_state += 1
    elif 2 > out_result >= 0:
        mes_show = ' ==> Too Bad'
        too_bad_state += 1

    b = str(round(out_result, 1)) + f'{"|":>20}' + mes_show + '\n'
    my_test.writelines(b)
    # my_test.writelines('\n')
    my_test.writelines('|-----------------|-------------------|----------------------|----------------------|')
    my_test.writelines('\n')

my_test.writelines('Tổng kết: Good có: %d, Normal có %d, Bad có %d, Too Bad có %d' %(good_state, normal_state, bad_state, too_bad_state))
my_test.close()
