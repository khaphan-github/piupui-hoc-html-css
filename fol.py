import os

titles = [
    "Chào mừng đến với khóa học HTML & CSS!",
    "Làm quen với thẻ HTML đầu tiên, thẻ Heading",
    "Tạo một trang báo!",
    "Thẻ chèn hình ảnh - <img>",
    "Khái niệm Nesting",
    "Nút bấm (Buttons)",
    "Thẻ nhập liệu",
    "Xây dựng trang Google!",
    "Thẻ liên kết (Anchor tags)",
    "Cấu trúc một trang HTML đúng chuẩn",
    "Danh sách (Lists)",
    "Xây dựng một trang web cá nhân",
    "Triển khai trang web cá nhân của bạn lên mạng",
    "Tổng kết phần 1: Build & Deploy Your First Website"
]

def create_folders(titles):
    for title in titles:
        folder_name = title.replace(" ", "_").replace(":", "").replace("&", "and").replace("!", "")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created.")
        else:
            print(f"Folder '{folder_name}' already exists.")

create_folders(titles)
