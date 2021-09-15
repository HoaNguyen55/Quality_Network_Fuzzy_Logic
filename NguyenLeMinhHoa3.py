from NguyenLeMinhHoa import quality_network as main
m = main()
# Test app:
import random
in_mes_delay_v = []
in_spd_network_v = []
in_spam_mail_v = []

num_of_test = int(input('Nhập số lượng test case: '))

for i in range(0, num_of_test+1):
    in_spam_mail_val = round(random.uniform(0, 10001))
    in_spam_mail_v.append(in_spam_mail_val)
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
mes_show = 'Không biết'
for i in range(0, num_of_test+1):

    in_spam_mail = in_spam_mail_v[i]
    in_mes_delay = in_mes_delay_v[i]
    in_spd_network = in_spd_network_v[i]

    m.input["Số lượng thư rác"]                 = in_spam_mail
    m.input["Tỉ lệ gói tin bị gián đoạn"]       = in_mes_delay
    m.input["Tốc độ đường truyền tối thiểu"]    = in_spd_network
    a = f'| {in_spam_mail:<15} | {in_mes_delay:<15}   | {in_spd_network:<15}      |'
    my_test.writelines(a)
    m.compute()
    out_result = m.output["Chất lượng của hệ thống mạng"]

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

my_test.writelines('\nTổng kết:\n'
                   '\t- Số lượng testcases: %d\n'
                   '\t- Good có: %d\n'
                   '\t- Normal có %d\n'
                   '\t- Bad có %d\n'
                   '\t- Too Bad có %d' % (num_of_test, good_state, normal_state, bad_state, too_bad_state))
my_test.close()
