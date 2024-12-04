class PublicTransport:
    def __init__(self, loai_phuong_tien, tuyen_duong, so_cho_ngoi, tinh_trang):
        self.loai_phuong_tien = loai_phuong_tien
        self.tuyen_duong = tuyen_duong
        self.so_cho_ngoi = so_cho_ngoi
        self.tinh_trang = tinh_trang

    def hien_thi_thong_tin(self):
        print(f"Loại phương tiện: {self.loai_phuong_tien}")
        print(f"Tuyến đường: {self.tuyen_duong}")
        print(f"Số chỗ ngồi: {self.so_cho_ngoi}")
        print(f"Tình trạng: {self.tinh_trang}")


class Taxi(PublicTransport):
    def __init__(self, tuyen_duong, so_cho_ngoi, tinh_trang, gia_cuoc):
        super().__init__("Taxi", tuyen_duong, so_cho_ngoi, tinh_trang)
        self.gia_cuoc = gia_cuoc 

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f"Giá cước mỗi km: {self.gia_cuoc} VND")


class XeOmCongNghe(PublicTransport):
    def __init__(self, tuyen_duong, tinh_trang, ten_ung_dung):
        super().__init__("Xe ôm công nghệ", tuyen_duong, 1, tinh_trang)
        self.ten_ung_dung = ten_ung_dung  

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f"Ứng dụng: {self.ten_ung_dung}")




taxi = Taxi("Tuyến 21", 6, "Hoạt động", 4676)
taxi.hien_thi_thong_tin()


xe_om = XeOmCongNghe("Tuyến 6", "Hoạt động", "Be")
xe_om.hien_thi_thong_tin()






"""
Giải thích về kế thừa:
   Tái sử dụng mã: Các thuộc tính và phương thức của lớp cha PublicTransport sẽ được chia sẻ với tất cả các lớp con như Taxi hoặc XeOmCongNghe. Điều này giúp tiết kiệm thời gian vì không cần viết lại những thuộc tính hay phương thức cơ bản cho mỗi loại phương tiện.
   Mở rộng linh hoạt: Khi cần thêm các loại phương tiện mới, bạn chỉ cần tạo các lớp con kế thừa từ lớp cha và chỉ định các thuộc tính, phương thức riêng cho loại phương tiện đó.
   Bảo trì dễ dàng: Nếu có sự thay đổi ở phần chung, chỉ cần sửa ở lớp cha. Các lớp con sẽ tự động cập nhật theo.
"""

