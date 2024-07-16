import tkinter as tk

# Tạo giao diện chính
root = tk.Tk()
root.title("Ứng dụng Ngân hàng")

# Khung cho nội dung
frame = tk.Frame(root)
frame.pack()

# Nhãn hiển thị số dư tài khoản
lbl_so_du = tk.Label(frame, text="Số dư tài khoản: 0đ")
lbl_so_du.pack()

# Hộp nhập số tiền
entry_so_tien = tk.Entry(frame)
entry_so_tien.pack()

# Nút nạp tiền
btn_nap_tien = tk.Button(frame, text="Nạp tiền")
btn_nap_tien.pack()

# Nút rút tiền
btn_rut_tien = tk.Button(frame, text="Rút tiền")
btn_rut_tien.pack()

# Chạy giao diện
root.mainloop()
