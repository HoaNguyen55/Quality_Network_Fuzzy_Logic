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
spam_mail = np.arrange(0, 11, 1)
mes_delay = np.arrange(0, 101, 1)
spd_network = np.arrange(1, 11, 1)
antecen_spam_mail = ctrl.Antecedent(spam_mail, "Số lượng thư rác")
antecen_mes_delay = ctrl.Antecedent(mes_delay, "Tỉ lệ gói tin bị gián đoạn")
antecen_spd_network = ctrl.Antecedent(spd_network, "Tốc độ đường truyền tối thiểu")

# Khởi tạo không gian nền kết luận
quality_network = np.arrange(1, 10, 1)
conseq_quality_network = ctrl.Consequent(spd_network, "Chất lượng của hệ thống mạng")

# Xây dựng tập mờ
# Số lượng thư rác có 3 tập mờ: Nhiều, Vừa phải, ít
spam_mail['Nhiều'] = fz.trapmf(spam_mail.universe, [6, 7, 8, 9, 10])
spam_mail['Vừa Phải'] = fz.trapmf(spam_mail.universe, [3, 4, 5, 6, 7])
spam_mail['Ít'] = fz.trapmf(spam_mail.universe, [0, 1, 2, 3, 4])
# Tỷ lệ gói tin bị gián đoạn: nhiều, trung bình, ít
mes_delay['Nhiều'] = fz.trapmf(mes_delay.universe, [70, 73, 74, 75, 78, 83, 93, 94, 98, 100])
mes_delay['Trung Bình'] = fz.trapmf(mes_delay.universe, [40, 46, 49, 51, 55, 56, 61, 65, 68, 70])
mes_delay['Ít'] = fz.trapmf(mes_delay.universe, [0, 5, 9, 12, 15, 21, 28, 29, 35, 40])
# Tốc độ đường truyền tối thiểu: cao, trung bình, thấp
spd_network['Cao'] = fz.trapmf(spd_network.universe, [60, 66, 68, 76, 78, 86, 90, 92, 96, 100])
spd_network['Trung Bình'] = fz.trapmf(spd_network.universe, [30, 35, 42, 44, 48, 55, 58, 60, 66, 70])
spd_network['Thấp'] = fz.trapmf(spd_network.universe, [0, 2, 5, 12, 18, 24, 28, 33, 35, 40])

# Neu 