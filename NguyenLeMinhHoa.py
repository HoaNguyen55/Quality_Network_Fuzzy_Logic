import numpy as np
import skfuzzy as fz
import skfuzzy.control as ctrl

# Dựa vào đề bài số 4, ta có 3 tiền đề và 1 kết luận
# 3 tiền đề bao gồm:
# - Số lượng thư rác: nhiều, vừa phải, ít
# - Tỷ lệ gói tin bị gián đoạn: nhiều, trung bình, ít
# - Tốc độ đường truyền tối thiểu: cao, trung bình, thấp
# 1 kết luận bao gồm:
# - Chất lượng hệ thống mạng: tốt, bình thường, tệ, quá yếu

# Tạo menu lựa chọn input hoặc đọc dữ liệu
# Người dùng input dữ liệu

# Người dùng đọc dữ liệu
# Khởi tạo không gian nền tiền đề
def quality_network():
    spam_mail   = np.arange(0, 10001, 1)
    mes_delay   = np.arange(0, 101, 1)
    spd_network = np.arange(0, 101, 1)
    antecen_spam_mail   = ctrl.Antecedent(spam_mail, "Số lượng thư rác")
    antecen_mes_delay   = ctrl.Antecedent(mes_delay, "Tỉ lệ gói tin bị gián đoạn")
    antecen_spd_network = ctrl.Antecedent(spd_network, "Tốc độ đường truyền tối thiểu")

    # Khởi tạo không gian nền kết luận
    quality_network     = np.arange(0, 11, 1)
    conseq_quality_network = ctrl.Consequent(quality_network, "Chất lượng của hệ thống mạng")

    # Xây dựng tập mờ
    # Số lượng thư rác có 3 tập mờ: Nhiều, Vừa phải, ít
    antecen_spam_mail['Nhiều']      = fz.trapmf(antecen_spam_mail.universe, [6000, 7000, 10000, 10000])
    antecen_spam_mail['Vừa Phải']   = fz.trapmf(antecen_spam_mail.universe, [3000, 4000, 5000, 6500])
    antecen_spam_mail['Ít']         = fz.trapmf(antecen_spam_mail.universe, [0, 0, 2000, 3500])
    # antecen_spam_mail.view()

    # Tỷ lệ gói tin bị gián đoạn: nhiều, trung bình, ít
    antecen_mes_delay['Nhiều']      = fz.trapmf(antecen_mes_delay.universe, [65, 80, 100, 100])
    antecen_mes_delay['Trung Bình'] = fz.trapmf(antecen_mes_delay.universe, [30, 40, 60, 70])
    antecen_mes_delay['Ít']         = fz.trapmf(antecen_mes_delay.universe, [0, 0, 30, 40])
    # antecen_mes_delay.view()

    # Tốc độ đường truyền tối thiểu: cao, trung bình, thấp
    antecen_spd_network['Cao']          = fz.trapmf(antecen_spd_network.universe, [60, 70, 100, 100])
    antecen_spd_network['Trung Bình']   = fz.trapmf(antecen_spd_network.universe, [30, 40, 60, 70])
    antecen_spd_network['Thấp']         = fz.trapmf(antecen_spd_network.universe, [0, 0, 20, 35])
    # antecen_spd_network.view()

    # Chất lượng của hệ thống mạng
    quality_rate = {"Tốt"           : [7, 8, 10, 10],
                    "Bình Thường"   : [5, 6, 7, 8],
                    "Tệ"            : [2, 3, 5, 6],
                    "Quá Yếu"       : [0, 0, 3, 4]}
    key_lst_quality = list(quality_rate.keys())
    val_lst_quality = list(quality_rate.values())
    conseq_quality_network[key_lst_quality[0]] = fz.trapmf(conseq_quality_network.universe, val_lst_quality[0])
    conseq_quality_network[key_lst_quality[1]] = fz.trapmf(conseq_quality_network.universe, val_lst_quality[1])
    conseq_quality_network[key_lst_quality[2]] = fz.trapmf(conseq_quality_network.universe, val_lst_quality[2])
    conseq_quality_network[key_lst_quality[3]] = fz.trapmf(conseq_quality_network.universe, val_lst_quality[3])
    # conseq_quality_network.view()

    '''- Nếu số lượng tin nhắn rác, tỉ lệ gói tin bị gián đoạn càng lớn và tốc độ truyền tải mạng càng nhỏ thì chất lượng mạng càng yếu
    - Chất lượng hệ thống mạng tỉ lệ nghịch với số lượng tin nhắn rác và tỉ lệ gói tin bị gián đoạn
    - Chất lượng hệ thống mạng tỉ lệ thuận với tốc độ mạng truyền tải
    '''
    R1  = ctrl.Rule(antecen_spam_mail["Nhiều"]     & antecen_mes_delay["Nhiều"]       & antecen_spd_network["Cao"]			, conseq_quality_network["Tệ"])
    R2  = ctrl.Rule(antecen_spam_mail["Nhiều"]     & antecen_mes_delay["Nhiều"]       & antecen_spd_network["Trung Bình"]	, conseq_quality_network["Quá Yếu"])
    R3  = ctrl.Rule(antecen_spam_mail["Nhiều"]     & antecen_mes_delay["Nhiều"]       & antecen_spd_network["Thấp"]			, conseq_quality_network["Quá Yếu"])

    R4  = ctrl.Rule(antecen_spam_mail["Vừa Phải"]  & antecen_mes_delay["Nhiều"]       & antecen_spd_network["Cao"]			, conseq_quality_network["Tệ"])
    R5  = ctrl.Rule(antecen_spam_mail["Vừa Phải"]  & antecen_mes_delay["Nhiều"]       & antecen_spd_network["Trung Bình"]	, conseq_quality_network["Quá Yếu"])
    R6  = ctrl.Rule(antecen_spam_mail["Vừa Phải"]  & antecen_mes_delay["Nhiều"]       & antecen_spd_network["Thấp"]			, conseq_quality_network["Quá Yếu"])
    R10 = ctrl.Rule(antecen_spam_mail["Nhiều"]     & antecen_mes_delay["Trung Bình"]  & antecen_spd_network["Cao"]			, conseq_quality_network["Tệ"])
    R11 = ctrl.Rule(antecen_spam_mail["Nhiều"]     & antecen_mes_delay["Trung Bình"]  & antecen_spd_network["Trung Bình"]	, conseq_quality_network["Quá Yếu"])
    R12 = ctrl.Rule(antecen_spam_mail["Nhiều"]     & antecen_mes_delay["Trung Bình"]  & antecen_spd_network["Thấp"]			, conseq_quality_network["Quá Yếu"])

    R7  = ctrl.Rule(antecen_spam_mail["Ít"]        & antecen_mes_delay["Nhiều"]       & antecen_spd_network["Cao"]			, conseq_quality_network["Bình Thường"])
    R8  = ctrl.Rule(antecen_spam_mail["Ít"]        & antecen_mes_delay["Nhiều"]       & antecen_spd_network["Trung Bình"]	, conseq_quality_network["Tệ"])
    R9  = ctrl.Rule(antecen_spam_mail["Ít"]        & antecen_mes_delay["Nhiều"]       & antecen_spd_network["Thấp"]			, conseq_quality_network["Quá Yếu"])
    R19 = ctrl.Rule(antecen_spam_mail["Nhiều"]     & antecen_mes_delay["Ít"]          & antecen_spd_network["Cao"]			, conseq_quality_network["Bình Thường"])
    R20 = ctrl.Rule(antecen_spam_mail["Nhiều"]     & antecen_mes_delay["Ít"]          & antecen_spd_network["Trung Bình"]	, conseq_quality_network["Tệ"])
    R21 = ctrl.Rule(antecen_spam_mail["Nhiều"]     & antecen_mes_delay["Ít"]          & antecen_spd_network["Thấp"]			, conseq_quality_network["Quá Yếu"])

    R13 = ctrl.Rule(antecen_spam_mail["Vừa Phải"]  & antecen_mes_delay["Trung Bình"]  & antecen_spd_network["Cao"]			, conseq_quality_network["Bình Thường"])
    R14 = ctrl.Rule(antecen_spam_mail["Vừa Phải"]  & antecen_mes_delay["Trung Bình"]  & antecen_spd_network["Trung Bình"]	, conseq_quality_network["Tệ"])
    R15 = ctrl.Rule(antecen_spam_mail["Vừa Phải"]  & antecen_mes_delay["Trung Bình"]  & antecen_spd_network["Thấp"]			, conseq_quality_network["Quá Yếu"])

    R16 = ctrl.Rule(antecen_spam_mail["Ít"]        & antecen_mes_delay["Trung Bình"]  & antecen_spd_network["Cao"]			, conseq_quality_network["Tốt"])
    R17 = ctrl.Rule(antecen_spam_mail["Ít"]        & antecen_mes_delay["Trung Bình"]  & antecen_spd_network["Trung Bình"]	, conseq_quality_network["Bình Thường"])
    R18 = ctrl.Rule(antecen_spam_mail["Ít"]        & antecen_mes_delay["Trung Bình"]  & antecen_spd_network["Thấp"]			, conseq_quality_network["Tệ"])
    R22 = ctrl.Rule(antecen_spam_mail["Vừa Phải"]  & antecen_mes_delay["Ít"]          & antecen_spd_network["Cao"]			, conseq_quality_network["Tốt"])
    R23 = ctrl.Rule(antecen_spam_mail["Vừa Phải"]  & antecen_mes_delay["Ít"]          & antecen_spd_network["Trung Bình"]	, conseq_quality_network["Bình Thường"])
    R24 = ctrl.Rule(antecen_spam_mail["Vừa Phải"]  & antecen_mes_delay["Ít"]          & antecen_spd_network["Thấp"]			, conseq_quality_network["Bình Thường"])

    R25 = ctrl.Rule(antecen_spam_mail["Ít"]        & antecen_mes_delay["Ít"]          & antecen_spd_network["Cao"]			, conseq_quality_network["Tốt"])
    R26 = ctrl.Rule(antecen_spam_mail["Ít"]        & antecen_mes_delay["Ít"]          & antecen_spd_network["Trung Bình"]	, conseq_quality_network["Tốt"])
    R27 = ctrl.Rule(antecen_spam_mail["Ít"]        & antecen_mes_delay["Ít"]          & antecen_spd_network["Thấp"]			, conseq_quality_network["Tốt"])

    rules = [R1, R2, R3, R4, R5, R6, R7, R8, R9,
             R10, R11, R12, R13, R14, R15, R16, R17, R18,
             R19, R20, R21, R22, R23, R24, R25, R26, R27]
    controlSys = ctrl.ControlSystem(rules)
    model = ctrl.ControlSystemSimulation(controlSys)
    return model
